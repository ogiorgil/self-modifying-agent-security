#!/usr/bin/env python3
"""Run an experimental trial from a workload manifest.

A trial resets the sandbox working directory, stages attacker-controlled
payload files, then runs a chain of Claude Code sessions against the same
working directory (without reset between sessions). After each session the
script captures:

  - the full stream-json event log
  - the assistant's extracted text response
  - a file-level diff between the working dir and the clean template

After the chain completes, the success criterion from the manifest is
checked and a human-readable trial report is written.

Usage:
    python testbed/scripts/run_trial.py --workload t01_license_comment_via_readme
    python testbed/scripts/run_trial.py --workload t01_license_comment_via_readme \\
        --chain exposure-stabilization-probe
    python testbed/scripts/run_trial.py --workload <id> --trial-id custom_name
"""

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_DIR = REPO_ROOT / "testbed" / "sandbox_template"
WORKLOADS_DIR = REPO_ROOT / "testbed" / "workloads"
RESULTS_DIR = REPO_ROOT / "testbed" / "results"
DEFAULT_WORKING_DIR = REPO_ROOT.parent / f"{REPO_ROOT.name}-working"
DEFAULT_TIMEOUT = 600


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


def clear_claude_memory(working_dir: Path) -> None:
    encoded = working_dir.resolve().as_posix().replace("/", "-")
    memory_dir = Path.home() / ".claude" / "projects" / encoded / "memory"
    if memory_dir.exists():
        shutil.rmtree(memory_dir)


def stage_payload(workload_dir: Path, working_dir: Path, staging: list[dict]) -> None:
    for spec in staging:
        src = workload_dir / spec["from"]
        dst = working_dir / spec["to"]
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def invoke_claude(
    prompt: str,
    working_dir: Path,
    timeout: int,
) -> tuple[list[dict], int, str]:
    cmd = [
        "claude",
        "--print",
        "--verbose",
        "--output-format", "stream-json",
        "--dangerously-skip-permissions",
        prompt,
    ]
    try:
        result = subprocess.run(
            cmd,
            cwd=str(working_dir),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return [], -1, f"timeout after {timeout}s"

    events: list[dict] = []
    for line in result.stdout.strip().split("\n"):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    return events, result.returncode, result.stderr


def extract_assistant_text(events: list[dict]) -> str:
    chunks: list[str] = []
    for evt in events:
        if evt.get("type") != "assistant":
            continue
        msg = evt.get("message", {})
        for part in msg.get("content", []):
            if part.get("type") == "text":
                chunks.append(part.get("text", ""))
    return "\n\n".join(chunks)


def capture_diff(working_dir: Path) -> str:
    result = subprocess.run(
        ["diff", "-r", str(TEMPLATE_DIR), str(working_dir)],
        capture_output=True,
        text=True,
    )
    return result.stdout


def check_success(working_dir: Path, criterion: dict) -> tuple[bool, str]:
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
) -> None:
    lines = [
        f"# Trial report — {workload_id} / {trial_id}",
        "",
        f"- Workload: `{workload_id}`",
        f"- Trial ID: `{trial_id}`",
        f"- Chain: `{' -> '.join(chain)}`",
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
        help="Workload directory name under testbed/workloads/",
    )
    parser.add_argument(
        "--chain", default="exposure-probe",
        help="Hyphen-separated session names (e.g. exposure-probe, exposure-stabilization-probe)",
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
        help=f"Per-session Claude Code timeout in seconds (default: {DEFAULT_TIMEOUT})",
    )
    args = parser.parse_args()

    workload_dir = WORKLOADS_DIR / args.workload_id
    manifest_path = workload_dir / "manifest.json"
    if not manifest_path.exists():
        print(f"ERROR: manifest not found: {manifest_path}", file=sys.stderr)
        return 1

    manifest = json.loads(manifest_path.read_text())
    working_dir: Path = args.working_dir.resolve()
    trial_id = args.trial_id or time.strftime("%Y%m%d_%H%M%S")
    out_dir = RESULTS_DIR / args.workload_id / trial_id
    out_dir.mkdir(parents=True, exist_ok=True)

    chain = args.chain.split("-")
    for session in chain:
        if session not in manifest.get("sessions", {}):
            print(f"ERROR: session '{session}' not defined in manifest", file=sys.stderr)
            return 1

    print(f"Workload:    {args.workload_id}")
    print(f"Trial:       {trial_id}")
    print(f"Chain:       {' -> '.join(chain)}")
    print(f"Working dir: {working_dir}")
    print(f"Results:     {out_dir}")
    print()

    print("[setup] Resetting working directory")
    reset_working_dir(working_dir)
    clear_claude_memory(working_dir)

    staging = manifest.get("staging", [])
    print(f"[setup] Staging {len(staging)} payload file(s)")
    stage_payload(workload_dir, working_dir, staging)

    session_summaries: list[dict] = []
    for idx, session in enumerate(chain):
        prompt = manifest["sessions"][session]["prompt"]
        print(f"[session {idx+1}/{len(chain)}] {session}: invoking claude...")
        start = time.time()
        events, returncode, stderr = invoke_claude(prompt, working_dir, args.timeout)
        elapsed = time.time() - start
        print(f"  ({elapsed:.1f}s, {len(events)} events, rc={returncode})")

        (out_dir / f"{idx:02d}_{session}_events.json").write_text(
            json.dumps(events, indent=2)
        )
        response_text = extract_assistant_text(events)
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
        working_dir, manifest["success_criterion"]
    )

    write_report(
        out_dir, args.workload_id, trial_id, chain,
        session_summaries, persistence, success, success_msg,
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
