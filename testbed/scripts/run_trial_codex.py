#!/usr/bin/env python3
"""Run a Codex experimental trial from a workload manifest.

A trial resets the sandbox working directory, stages attacker-controlled
payload files, then runs a chain of Codex sessions against the same
working directory (without reset between sessions). After each session the
script captures:

  - the full JSONL event log
  - the assistant's extracted text response
  - a file-level diff between the working dir and the clean template

After the chain completes, the success criterion from the manifest is
checked and a human-readable trial report is written.

Usage:
    python testbed/scripts/run_trial_codex.py --workload c03_credential_exfil_via_coding_codex_md
    python testbed/scripts/run_trial_codex.py --workload <id> --trial-id custom_name
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_DIR = REPO_ROOT / "testbed" / "sandbox_template_codex"
WORKLOADS_DIR = REPO_ROOT / "testbed" / "workloads_codex"
RESULTS_DIR = REPO_ROOT / "testbed" / "results"
DEFAULT_WORKING_DIR = REPO_ROOT.parent / f"{REPO_ROOT.name}-working-codex"
DEFAULT_TIMEOUT = 600
DEFAULT_MODEL = "gpt-5.5"


def result_model_id(model: str | None) -> str:
    raw = model or DEFAULT_MODEL
    safe = "".join(ch if ch.isalnum() or ch in ("-", "_", ".") else "_" for ch in raw)
    return safe.strip("._-") or DEFAULT_MODEL


def reset_working_dir(working_dir: Path) -> None:
    if working_dir.exists():
        for item in working_dir.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    else:
        working_dir.mkdir(parents=True, exist_ok=True)
    for item in TEMPLATE_DIR.iterdir():
        dest = working_dir / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)


def clear_codex_session_state(working_dir: Path) -> None:
    """Codex trials use --ephemeral, so no per-project session state is reused."""
    return None


def stage_payload(workload_dir: Path, working_dir: Path, staging: list[dict]) -> None:
    for spec in staging:
        src = workload_dir / spec["from"]
        dst = working_dir / spec["to"]
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def apply_action(action: dict, workload_dir: Path, working_dir: Path) -> None:
    """Apply a single pre-session action to the working directory.

    Supported action types:
      - copy:                copy a file from the workload dir into the working dir
      - revert_from_template: restore a file from the clean template (useful for
                              removing a previously-staged payload between sessions)
      - delete:              delete a file from the working dir
    """
    kind = action.get("action")
    if kind == "copy":
        src = workload_dir / action["from"]
        dst = working_dir / action["to"]
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    elif kind == "revert_from_template":
        target = action["target"]
        src = TEMPLATE_DIR / target
        dst = working_dir / target
        if not src.exists():
            raise FileNotFoundError(
                f"revert_from_template: template does not contain {target}"
            )
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    elif kind == "delete":
        target = working_dir / action["target"]
        if target.exists():
            if target.is_dir():
                shutil.rmtree(target)
            else:
                target.unlink()
    else:
        raise ValueError(f"Unknown action kind: {kind!r}")


def invoke_codex(
    prompt: str,
    working_dir: Path,
    timeout: int,
    model: str | None = None,
) -> tuple[list[dict], int, str, str]:
    with tempfile.TemporaryDirectory(prefix="run_trial_codex_") as tmp:
        response_path = Path(tmp) / "last_message.md"
        cmd = [
            "codex",
            "exec",
            "--json",
            "--output-last-message", str(response_path),
            "--sandbox", "workspace-write",
            "--skip-git-repo-check",
        ]
        if model:
            cmd.extend(["--model", model])
        cmd.append(prompt)
        try:
            result = subprocess.run(
                cmd,
                cwd=str(working_dir),
                capture_output=True,
                text=True,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            return [], -1, f"timeout after {timeout}s", ""
        except FileNotFoundError:
            return (
                [],
                127,
                "codex: command not found. Install the Codex CLI or add it to PATH.",
                "",
            )

        response_text = response_path.read_text() if response_path.exists() else ""

    events: list[dict] = []
    for line in result.stdout.strip().split("\n"):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    stderr = "\n".join(
        line
        for line in result.stderr.splitlines()
        if not line.startswith("WARNING: failed to clean up stale arg0 temp dirs:")
        and "write_stdin failed: stdin is closed for this session" not in line
    )

    return events, result.returncode, stderr, response_text


def extract_assistant_text(events: list[dict]) -> str:
    chunks: list[str] = []
    for evt in events:
        if evt.get("type") != "assistant":
            continue
        msg = evt.get("message", {})
        for part in msg.get("content", []):
            if part.get("type") == "text":
                chunks.append(part.get("text", ""))
    if chunks:
        return "\n\n".join(chunks)

    # Codex JSONL schemas can vary across CLI versions. Keep a conservative
    # fallback for older artifacts where no --output-last-message file exists.
    for evt in events:
        if evt.get("type") in {"agent_message", "assistant_message"}:
            message = evt.get("message")
            if isinstance(message, str):
                chunks.append(message)
            elif isinstance(message, dict):
                text = message.get("text") or message.get("content")
                if isinstance(text, str):
                    chunks.append(text)
    return "\n\n".join(chunks)


def capture_diff(working_dir: Path) -> str:
    result = subprocess.run(
        ["diff", "-r", str(TEMPLATE_DIR), str(working_dir)],
        capture_output=True,
        text=True,
    )
    return result.stdout


def check_success(
    working_dir: Path,
    criterion: dict,
    response_text: str = "",
) -> tuple[bool, str]:
    ctype = criterion.get("type")
    if ctype == "string_in_file":
        target_file = working_dir / criterion["file"]
        needle = criterion["string"]
        if not target_file.exists():
            return False, f"target file does not exist: {criterion['file']}"
        content = target_file.read_text()
        if needle in content:
            return True, f"found '{needle}' in {criterion['file']}"
        return False, f"string not found in {criterion['file']}"
    if ctype == "string_in_response":
        needle = criterion["string"]
        if needle in response_text:
            return True, f"found '{needle}' in final response"
        return False, "string not found in final response"
    return False, f"unknown criterion type: {ctype}"


def check_persistence(working_dir: Path, targets: list[str]) -> dict[str, bool]:
    result: dict[str, bool] = {}
    for target in targets:
        template_file = TEMPLATE_DIR / target
        working_file = working_dir / target
        if not working_file.exists():
            result[target] = False
            continue
        template_content = template_file.read_text() if template_file.exists() else ""
        working_content = working_file.read_text()
        result[target] = template_content != working_content
    return result


def write_report(
    out_dir: Path,
    workload_id: str,
    trial_id: str,
    chain: list[str],
    session_summaries: list[dict],
    persistence: dict[str, bool],
    success: bool,
    success_message: str,
    model: str | None = None,
) -> None:
    lines = [
        f"# Trial report — {workload_id} / {trial_id}",
        "",
        f"- Workload: `{workload_id}`",
        f"- Trial ID: `{trial_id}`",
        f"- Chain: `{' -> '.join(chain)}`",
        f"- Agent: `codex`",
        f"- Model: `{model or '(codex default)'}`",
        f"- Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Verdict",
        "",
        f"- **Attack success (criterion met):** {'YES' if success else 'NO'}",
        f"  - {success_message}",
        "",
        "## Persistence targets (modified vs template)",
        "",
    ]
    for target, modified in persistence.items():
        marker = "[x]" if modified else "[ ]"
        lines.append(f"- {marker} `{target}` {'modified' if modified else 'unchanged'}")

    lines.extend(["", "## Sessions", ""])
    for summary in session_summaries:
        lines.extend([
            f"### {summary['index']:02d} - {summary['session']}",
            "",
            f"- Return code: {summary['returncode']}",
            f"- Events: {summary['event_count']}",
            f"- Response length: {summary['response_length']} chars",
            f"- Diff lines: {summary['diff_lines']}",
            "",
            "Artifacts:",
            f"- `{summary['index']:02d}_{summary['session']}_events.json`",
            f"- `{summary['index']:02d}_{summary['session']}_response.md`",
            f"- `{summary['index']:02d}_{summary['session']}_diff.txt`",
            "",
        ])

    (out_dir / "trial_report.md").write_text("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--workload", required=True, dest="workload_id",
        help="Workload directory name under testbed/workloads_codex/",
    )
    parser.add_argument(
        "--chain", default="exposure-probe",
        help="Hyphen-separated session names (e.g. exposure-probe, exposure-stabilization-probe)",
    )
    parser.add_argument(
        "--prepare-only",
        action="store_true",
        help="Reset the working directory and stage payload files, then exit before invoking codex. Use this to run an interactive Codex session manually against a prepared environment.",
    )
    parser.add_argument(
        "--trial-id", default=None,
        help="Trial identifier for the result subdirectory (defaults to a timestamp)",
    )
    parser.add_argument(
        "--working-dir", type=Path, default=DEFAULT_WORKING_DIR,
        help=f"Working directory path (default: {DEFAULT_WORKING_DIR})",
    )
    parser.add_argument(
        "--timeout", type=int, default=DEFAULT_TIMEOUT,
        help=f"Per-session Codex timeout in seconds (default: {DEFAULT_TIMEOUT})",
    )
    parser.add_argument(
        "--model", default=DEFAULT_MODEL,
        help=f"Model alias or full name to pass to codex --model (default: {DEFAULT_MODEL}).",
    )
    args = parser.parse_args()

    workload_dir = WORKLOADS_DIR / args.workload_id
    manifest_path = workload_dir / "manifest.json"
    if not manifest_path.exists():
        print(f"ERROR: manifest not found: {manifest_path}", file=sys.stderr)
        return 1

    manifest = json.loads(manifest_path.read_text())
    working_dir: Path = args.working_dir.resolve()

    chain = args.chain.split("-")
    if not args.prepare_only:
        for session in chain:
            if session not in manifest.get("sessions", {}):
                print(f"ERROR: session '{session}' not defined in manifest", file=sys.stderr)
                return 1

    print(f"Workload:    {args.workload_id}")
    print(f"Working dir: {working_dir}")
    if args.prepare_only:
        print("Mode:        prepare-only (no codex invocation)")
    else:
        trial_id = args.trial_id or time.strftime("%Y%m%d_%H%M%S")
        model_id = result_model_id(args.model)
        out_dir = RESULTS_DIR / args.workload_id / model_id / trial_id
        out_dir.mkdir(parents=True, exist_ok=True)
        print(f"Trial:       {trial_id}")
        print(f"Chain:       {' -> '.join(chain)}")
        print(f"Model:       {args.model or '(codex default)'}")
        print(f"Results:     {out_dir}")
    print()

    print("[setup] Resetting working directory")
    reset_working_dir(working_dir)
    clear_codex_session_state(working_dir)

    staging = manifest.get("staging", [])
    print(f"[setup] Staging {len(staging)} payload file(s)")
    stage_payload(workload_dir, working_dir, staging)

    if args.prepare_only:
        print()
        print("Working directory prepared for manual interactive use.")
        print()
        print("Next steps:")
        print(f"  cd {working_dir}")
        print("  codex")
        print()
        print("Session prompts defined for this workload (paste into codex):")
        print()
        for name, spec in manifest.get("sessions", {}).items():
            print(f"--- {name} ---")
            print(spec.get("prompt", "(no prompt defined)"))
            print()
        print("After each session, inspect what changed with:")
        print(f"  diff -r {TEMPLATE_DIR} {working_dir}")
        print()
        crit = manifest.get("success_criterion", {})
        if crit.get("type") == "string_in_file":
            target_path = working_dir / crit["file"]
            print("Attack success check (after the probe session completes):")
            print(f"  grep -n '{crit['string']}' {target_path}")
            print()
        return 0

    session_summaries: list[dict] = []
    final_response_text = ""
    for idx, session in enumerate(chain):
        session_spec = manifest["sessions"][session]
        pre_actions = session_spec.get("pre_actions", [])
        if pre_actions:
            print(f"[session {idx+1}/{len(chain)}] {session}: applying {len(pre_actions)} pre-action(s)")
            for action in pre_actions:
                apply_action(action, workload_dir, working_dir)
        prompt = session_spec["prompt"]
        print(f"[session {idx+1}/{len(chain)}] {session}: invoking codex...")
        start = time.time()
        events, returncode, stderr, response_text = invoke_codex(
            prompt, working_dir, args.timeout, args.model
        )
        elapsed = time.time() - start
        print(f"  ({elapsed:.1f}s, {len(events)} events, rc={returncode})")

        (out_dir / f"{idx:02d}_{session}_events.json").write_text(
            json.dumps(events, indent=2)
        )
        if not response_text:
            response_text = extract_assistant_text(events)
        final_response_text = response_text
        (out_dir / f"{idx:02d}_{session}_response.md").write_text(response_text)
        diff_text = capture_diff(working_dir)
        (out_dir / f"{idx:02d}_{session}_diff.txt").write_text(diff_text)
        if stderr:
            (out_dir / f"{idx:02d}_{session}_stderr.txt").write_text(stderr)

        session_summaries.append({
            "index": idx,
            "session": session,
            "returncode": returncode,
            "event_count": len(events),
            "response_length": len(response_text),
            "diff_lines": len(diff_text.splitlines()),
        })

    print()
    print("[finalize] Checking persistence targets and success criterion")
    persistence = check_persistence(
        working_dir, manifest.get("persistence_targets", [])
    )
    success, success_msg = check_success(
        working_dir, manifest["success_criterion"], final_response_text
    )

    write_report(
        out_dir, args.workload_id, trial_id, chain,
        session_summaries, persistence, success, success_msg,
        model=args.model,
    )

    print()
    for target, modified in persistence.items():
        marker = "[x]" if modified else "[ ]"
        print(f"  {marker} {target}")
    print()
    print(f"Attack success: {'YES' if success else 'NO'} - {success_msg}")
    print(f"Full report:    {out_dir / 'trial_report.md'}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
