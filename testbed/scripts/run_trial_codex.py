#!/usr/bin/env python3
"""Run a Codex experimental trial from a workload manifest.

A trial resets the sandbox working directory, stages attacker-controlled
payload files, then runs a chain of Codex sessions against the same
working directory (without reset between sessions). After each session the
script captures:

  - the full JSONL event log
  - the assistant's extracted text response
  - a file-level diff between the working dir and the clean template
  - copies of files that are new or changed relative to the clean template

After the chain completes, the success criterion from the manifest is
checked and a human-readable trial report is written.

Usage:
    python testbed/scripts/run_trial_codex.py --workload c03_credential_exfil_via_coding_codex_md
    python testbed/scripts/run_trial_codex.py --workload <id> --trial-id custom_name
    python testbed/scripts/run_trial_codex.py --workload <id> --num-trials 10

Persisted-sandbox mode (--no-reset):

    For experiments that study state accumulating across repeated invocations of
    the same prompt, pass --no-reset on every iteration after the first. The
    first run resets and stages the working dir as usual; subsequent runs reuse
    whatever state the prior runs left behind.

    Example — run the same probe ten times, letting state compound:

        python testbed/scripts/run_trial_codex.py --workload <id> --trial-id iter_00
        for i in $(seq 1 9); do
            python testbed/scripts/run_trial_codex.py --workload <id> \\
                --trial-id iter_$(printf "%02d" $i) --no-reset
        done
"""

from __future__ import annotations

import argparse
import filecmp
import json
import re
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


def default_chain_for_manifest(manifest: dict) -> list[str]:
    sessions = manifest.get("sessions", {})
    if {"probe_1", "stabilization", "probe_2"}.issubset(sessions):
        return ["probe_1", "stabilization", "probe_2"]
    if {"exposure", "probe"}.issubset(sessions):
        return ["exposure", "probe"]
    if "probe" in sessions:
        return ["probe"]
    return list(sessions)


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


def record_staging_specs(
    staging: list[dict],
    session: str | None = None,
    channel: str | None = None,
) -> list[dict]:
    records: list[dict] = []
    for spec in staging:
        record = dict(spec)
        if session is not None:
            record["session"] = session
        if channel is not None and "channel" not in record:
            record["channel"] = channel
        records.append(record)
    return records


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
            "--sandbox", "danger-full-access",
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


def save_modified_files(working_dir: Path, artifact_dir: Path) -> dict[str, list[str]]:
    """Copy files that are new or changed relative to the clean template."""
    if artifact_dir.exists():
        shutil.rmtree(artifact_dir)
    artifact_dir.mkdir(parents=True, exist_ok=True)

    changed: list[str] = []
    new: list[str] = []
    deleted: list[str] = []

    for path in sorted(working_dir.rglob("*")):
        if not path.is_file():
            continue
        rel_path = path.relative_to(working_dir)
        template_path = TEMPLATE_DIR / rel_path
        rel = rel_path.as_posix()
        if not template_path.exists():
            new.append(rel)
        elif filecmp.cmp(path, template_path, shallow=False):
            continue
        else:
            changed.append(rel)

        dest = artifact_dir / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)

    for template_path in sorted(TEMPLATE_DIR.rglob("*")):
        if not template_path.is_file():
            continue
        rel_path = template_path.relative_to(TEMPLATE_DIR)
        if not (working_dir / rel_path).exists():
            deleted.append(rel_path.as_posix())

    manifest = {
        "changed": changed,
        "new": new,
        "deleted": deleted,
    }
    (artifact_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))
    return manifest


def extract_shell_commands(events: list[dict]) -> list[str]:
    cmds: list[str] = []
    seen: set[str] = set()
    for evt in events:
        item = evt.get("item")
        if isinstance(item, dict) and item.get("type") == "command_execution":
            cmd = item.get("command", "")
            if cmd and cmd not in seen:
                cmds.append(cmd)
                seen.add(cmd)

        message = evt.get("message", {})
        if not isinstance(message, dict):
            continue
        for part in message.get("content", []):
            if not isinstance(part, dict):
                continue
            if part.get("type") != "tool_use":
                continue
            if part.get("name") not in ("Bash", "bash", "exec_command"):
                continue
            tool_input = part.get("input", {})
            if not isinstance(tool_input, dict):
                continue
            cmd = tool_input.get("command") or tool_input.get("cmd")
            if cmd and cmd not in seen:
                cmds.append(cmd)
                seen.add(cmd)
    return cmds


def check_success(
    working_dir: Path,
    criterion: dict,
    response_text: str = "",
    events: list[dict] | None = None,
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
    if ctype == "command_in_events":
        pattern = criterion["pattern"]
        for cmd in extract_shell_commands(events or []):
            if re.search(pattern, cmd):
                return True, f"shell command matched /{pattern}/"
        return False, f"no shell command matched /{pattern}/"
    return False, f"unknown criterion type: {ctype}"
 

def success_criterion_for_session(manifest: dict, session_spec: dict) -> dict | None:
    return session_spec.get("success_criterion") or manifest.get("success_criterion")


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


def check_attack_payload_persistence(
    workload_dir: Path,
    working_dir: Path,
    staging: list[dict],
) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for idx, spec in enumerate(staging):
        source_rel = spec["from"]
        target_rel = spec["to"]
        source_file = workload_dir / source_rel
        target_file = working_dir / target_rel
        source_exists = source_file.exists()
        target_exists = target_file.exists()
        source_content = source_file.read_bytes() if source_exists else b""
        exact_match = False
        found_paths: list[str] = []
        if source_exists:
            for candidate in sorted(working_dir.rglob("*")):
                if candidate.is_file() and candidate.read_bytes() == source_content:
                    found_paths.append(candidate.relative_to(working_dir).as_posix())
            exact_match = target_exists and target_file.read_bytes() == source_content
        key = f"{spec.get('session') or 'initial'}:{source_rel}->{target_rel}:{idx}"
        result[key] = {
            "source": source_rel,
            "target": target_rel,
            "session": spec.get("session"),
            "channel": spec.get("channel"),
            "target_exists": target_exists,
            "exact_match": exact_match,
            "exists_anywhere": bool(found_paths),
            "found_paths": found_paths,
        }
    return result


def write_report(
    out_dir: Path,
    workload_id: str,
    trial_id: str,
    chain: list[str],
    session_summaries: list[dict],
    persistence: dict[str, bool],
    attack_payload_persistence: dict[str, dict],
    session_successes: list[dict],
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
        "## Per-probe success",
        "",
    ]
    if session_successes:
        for result in session_successes:
            verdict = "YES" if result["success"] else "NO"
            lines.append(
                f"- `{result['session']}`: {verdict} - {result['success_message']}"
            )
    else:
        lines.append("- (no `probe_*` sessions in chain)")

    lines.extend([
        "",
        "## Attack payload persistence",
        "",
    ])
    if attack_payload_persistence:
        for result in attack_payload_persistence.values():
            target = result["target"]
            marker = "[x]" if result["exists_anywhere"] else "[ ]"
            if result["exists_anywhere"]:
                if result["exact_match"]:
                    status = "persisted at target"
                else:
                    status = "persisted elsewhere"
            elif result["target_exists"]:
                status = "target changed"
            else:
                status = "missing"
            context_parts = [f"source: `{result['source']}`"]
            if result.get("session"):
                context_parts.append(f"session: `{result['session']}`")
            if result.get("channel"):
                context_parts.append(f"channel: `{result['channel']}`")
            lines.append(
                f"- {marker} `{target}` {status} "
                f"({', '.join(context_parts)})"
            )
            if result["found_paths"] and not result["exact_match"]:
                lines.append(
                    f"  - Found at: {', '.join(f'`{path}`' for path in result['found_paths'])}"
                )
    else:
        lines.append("- (no staged payload files)")

    lines.extend([
        "",
        "## Persistence targets (modified vs template)",
        "",
    ])
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
            f"- Modified files saved: {summary['modified_file_count']}",
            f"- Deleted files recorded: {summary['deleted_file_count']}",
            "",
            "Artifacts:",
            f"- `{summary['index']:02d}_{summary['session']}_events.json`",
            f"- `{summary['index']:02d}_{summary['session']}_response.md`",
            f"- `{summary['index']:02d}_{summary['session']}_diff.txt`",
            f"- `{summary['index']:02d}_{summary['session']}_modified_files/`",
            "",
        ])

    (out_dir / "trial_report.md").write_text("\n".join(lines))


def write_batch_summary(
    out_dir: Path,
    workload_id: str,
    chain: list[str],
    trial_results: list[dict],
    model: str | None = None,
) -> None:
    successes = sum(1 for result in trial_results if result["success"])
    payload_persisted = sum(
        1 for result in trial_results if result.get("attack_payload_persisted")
    )
    total = len(trial_results)
    success_rate = successes / total if total else 0.0
    payload_persistence_rate = payload_persisted / total if total else 0.0
    session_names = sorted({
        session_result["session"]
        for result in trial_results
        for session_result in result.get("session_successes", [])
    })
    session_success_rates = {}
    for session in session_names:
        session_total = sum(
            1
            for result in trial_results
            for session_result in result.get("session_successes", [])
            if session_result["session"] == session
        )
        session_successes = sum(
            1
            for result in trial_results
            for session_result in result.get("session_successes", [])
            if session_result["session"] == session and session_result["success"]
        )
        session_success_rates[session] = {
            "successes": session_successes,
            "total": session_total,
            "success_rate": session_successes / session_total
            if session_total
            else 0.0,
        }

    summary = {
        "workload": workload_id,
        "chain": chain,
        "agent": "codex",
        "model": model or DEFAULT_MODEL,
        "num_trials": total,
        "successes": successes,
        "success_rate": success_rate,
        "attack_payload_persisted": payload_persisted,
        "attack_payload_persistence_rate": payload_persistence_rate,
        "session_success_rates": session_success_rates,
        "trials": trial_results,
    }
    (out_dir / "batch_summary.json").write_text(json.dumps(summary, indent=2))

    lines = [
        f"# Batch summary — {workload_id}",
        "",
        f"- Workload: `{workload_id}`",
        f"- Chain: `{' -> '.join(chain)}`",
        f"- Agent: `codex`",
        f"- Model: `{model or DEFAULT_MODEL}`",
        f"- Trials: {total}",
        f"- Attack successes: {successes}",
        f"- Attack success rate: {success_rate:.1%}",
        f"- Attack payload persisted: {payload_persisted}/{total} ({payload_persistence_rate:.1%})",
        f"- Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
    ]
    if session_success_rates:
        lines.extend(["## Per-probe Success Rates", ""])
        for session, stats in session_success_rates.items():
            lines.append(
                f"- `{session}`: {stats['successes']}/{stats['total']} "
                f"({stats['success_rate']:.1%})"
            )
        lines.append("")

    lines.extend(["## Trial Results", ""])
    for result in trial_results:
        verdict = "YES" if result["success"] else "NO"
        lines.append(
            f"- `{result['trial_id']}`: {verdict} - {result['success_message']} "
            f"(`{result['report_path']}`)"
        )
    (out_dir / "batch_summary.md").write_text("\n".join(lines))


def prepare_working_dir(
    no_reset: bool,
    working_dir: Path,
    workload_dir: Path,
    manifest: dict,
) -> bool:
    if no_reset:
        if not working_dir.exists():
            print(
                f"ERROR: --no-reset requires an existing working dir: {working_dir}",
                file=sys.stderr,
            )
            return False
        print("[setup] --no-reset: keeping existing working dir, session state, and payloads")
        return True

    print("[setup] Resetting working directory")
    reset_working_dir(working_dir)
    clear_codex_session_state(working_dir)

    staging = manifest.get("staging", [])
    print(f"[setup] Staging {len(staging)} payload file(s)")
    stage_payload(workload_dir, working_dir, staging)
    return True


def run_single_trial(
    workload_id: str,
    workload_dir: Path,
    manifest: dict,
    working_dir: Path,
    out_dir: Path,
    trial_id: str,
    chain: list[str],
    timeout: int,
    model: str | None,
    no_reset: bool,
) -> dict | None:
    print(f"Trial:       {trial_id}")
    print(f"Results:     {out_dir}")
    print()

    if not prepare_working_dir(no_reset, working_dir, workload_dir, manifest):
        return None

    session_summaries: list[dict] = []
    session_successes: list[dict] = []
    staged_payloads = record_staging_specs(
        manifest.get("staging", []),
        channel=manifest.get("channel"),
    )
    final_response_text = ""
    final_events: list[dict] = []
    final_success_criterion = manifest.get("success_criterion")
    for idx, session in enumerate(chain):
        session_spec = manifest["sessions"][session]
        pre_actions = session_spec.get("pre_actions", [])
        if pre_actions:
            print(f"[session {idx+1}/{len(chain)}] {session}: applying {len(pre_actions)} pre-action(s)")
            for action in pre_actions:
                apply_action(action, workload_dir, working_dir)
        session_staging = session_spec.get("staging", [])
        if session_staging:
            print(f"[session {idx+1}/{len(chain)}] {session}: staging {len(session_staging)} payload file(s)")
            stage_payload(workload_dir, working_dir, session_staging)
            staged_payloads.extend(record_staging_specs(
                session_staging,
                session=session,
                channel=session_spec.get("channel", manifest.get("channel")),
            ))
        session_success_criterion = success_criterion_for_session(
            manifest, session_spec
        )
        prompt = session_spec["prompt"]
        print(f"[session {idx+1}/{len(chain)}] {session}: invoking codex...")
        start = time.time()
        events, returncode, stderr, response_text = invoke_codex(
            prompt, working_dir, timeout, model
        )
        elapsed = time.time() - start
        print(f"  ({elapsed:.1f}s, {len(events)} events, rc={returncode})")

        (out_dir / f"{idx:02d}_{session}_events.json").write_text(
            json.dumps(events, indent=2)
        )
        if not response_text:
            response_text = extract_assistant_text(events)
        final_response_text = response_text
        final_events = events
        final_success_criterion = session_success_criterion
        (out_dir / f"{idx:02d}_{session}_response.md").write_text(response_text)
        diff_text = capture_diff(working_dir)
        (out_dir / f"{idx:02d}_{session}_diff.txt").write_text(diff_text)
        modified_manifest = save_modified_files(
            working_dir, out_dir / f"{idx:02d}_{session}_modified_files"
        )
        if stderr:
            (out_dir / f"{idx:02d}_{session}_stderr.txt").write_text(stderr)

        session_success: dict | None = None
        if session.startswith("probe") and session_success_criterion:
            success, success_msg = check_success(
                working_dir, session_success_criterion, response_text, events
            )
            session_success = {
                "session": session,
                "success": success,
                "success_message": success_msg,
                "success_criterion": session_success_criterion,
            }
            session_successes.append(session_success)

        session_summaries.append({
            "index": idx,
            "session": session,
            "returncode": returncode,
            "event_count": len(events),
            "response_length": len(response_text),
            "diff_lines": len(diff_text.splitlines()),
            "modified_file_count": (
                len(modified_manifest["changed"]) + len(modified_manifest["new"])
            ),
            "deleted_file_count": len(modified_manifest["deleted"]),
            "success": session_success,
        })

    print()
    print("[finalize] Checking persistence targets and success criterion")
    persistence = check_persistence(
        working_dir, manifest.get("persistence_targets", [])
    )
    attack_payload_persistence = check_attack_payload_persistence(
        workload_dir, working_dir, staged_payloads
    )
    attack_payload_persisted = (
        bool(attack_payload_persistence)
        and all(result["exists_anywhere"] for result in attack_payload_persistence.values())
    )
    if final_success_criterion:
        success, success_msg = check_success(
            working_dir, final_success_criterion, final_response_text, final_events
        )
    else:
        success = False
        success_msg = "no success criterion defined"

    write_report(
        out_dir, workload_id, trial_id, chain,
        session_summaries, persistence, attack_payload_persistence,
        session_successes, success, success_msg,
        model=model,
    )
    trial_summary = {
        "trial_id": trial_id,
        "success": success,
        "success_message": success_msg,
        "session_successes": session_successes,
        "attack_payload_persisted": attack_payload_persisted,
        "attack_payload_persistence": attack_payload_persistence,
    }
    (out_dir / "trial_summary.json").write_text(json.dumps(trial_summary, indent=2))

    print()
    for result in session_successes:
        verdict = "YES" if result["success"] else "NO"
        print(f"  {result['session']} success: {verdict} - {result['success_message']}")
    if session_successes:
        print()
    for result in attack_payload_persistence.values():
        marker = "[x]" if result["exists_anywhere"] else "[ ]"
        if result["exists_anywhere"]:
            status = "persisted at target" if result["exact_match"] else "persisted elsewhere"
        elif result["target_exists"]:
            status = "target changed"
        else:
            status = "missing"
        context_parts = []
        if result.get("session"):
            context_parts.append(f"session={result['session']}")
        if result.get("channel"):
            context_parts.append(f"channel={result['channel']}")
        context = f" ({', '.join(context_parts)})" if context_parts else ""
        print(f"  {marker} payload {result['target']}: {status}{context}")
    if attack_payload_persistence:
        print()
    for target, modified in persistence.items():
        marker = "[x]" if modified else "[ ]"
        print(f"  {marker} {target}")
    print()
    print(f"Attack success: {'YES' if success else 'NO'} - {success_msg}")
    print(f"Full report:    {out_dir / 'trial_report.md'}")

    return {
        "trial_id": trial_id,
        "success": success,
        "success_message": success_msg,
        "session_successes": session_successes,
        "attack_payload_persisted": attack_payload_persisted,
        "attack_payload_persistence": attack_payload_persistence,
        "report_path": str(out_dir / "trial_report.md"),
    }


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
        "--chain", default=None,
        help="Hyphen-separated session names (e.g. exposure-probe, probe_1-stabilization-probe_2). Defaults to the manifest's natural chain.",
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
        "--num-trials", type=int, default=1,
        help="Run the same experiment this many times and report the attack success rate (default: 1).",
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
    parser.add_argument(
        "--no-reset",
        action="store_true",
        help="Skip working-directory reset, payload staging, and Codex session-state clearing. Use after a prior trial has staged the sandbox to run additional sessions against the accumulated state — useful for studying state that compounds across repeated runs of the same prompt.",
    )
    args = parser.parse_args()
    if args.num_trials < 1:
        print("ERROR: --num-trials must be at least 1", file=sys.stderr)
        return 1
    if args.prepare_only and args.num_trials != 1:
        print("ERROR: --prepare-only cannot be combined with --num-trials", file=sys.stderr)
        return 1

    workload_dir = WORKLOADS_DIR / args.workload_id
    manifest_path = workload_dir / "manifest.json"
    if not manifest_path.exists():
        print(f"ERROR: manifest not found: {manifest_path}", file=sys.stderr)
        return 1

    manifest = json.loads(manifest_path.read_text())
    working_dir: Path = args.working_dir.resolve()

    chain = args.chain.split("-") if args.chain else default_chain_for_manifest(manifest)
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
        print(f"Chain:       {' -> '.join(chain)}")
        print(f"Model:       {args.model or '(codex default)'}")
        print(f"Num trials:  {args.num_trials}")
    print()

    if args.prepare_only:
        if not prepare_working_dir(args.no_reset, working_dir, workload_dir, manifest):
            return 1
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

    model_id = result_model_id(args.model)
    base_trial_id = args.trial_id or time.strftime("%Y%m%d_%H%M%S")
    result_root = RESULTS_DIR / args.workload_id / model_id
    batch_dir = result_root / base_trial_id

    if args.num_trials == 1:
        out_dirs = [(base_trial_id, batch_dir)]
    else:
        batch_dir.mkdir(parents=True, exist_ok=True)
        out_dirs = [
            (f"{base_trial_id}_{idx:02d}", batch_dir / f"trial_{idx:02d}")
            for idx in range(args.num_trials)
        ]

    trial_results: list[dict] = []
    for idx, (trial_id, out_dir) in enumerate(out_dirs, start=1):
        out_dir.mkdir(parents=True, exist_ok=True)
        if args.num_trials > 1:
            print(f"=== Trial {idx}/{args.num_trials} ===")
        result = run_single_trial(
            args.workload_id,
            workload_dir,
            manifest,
            working_dir,
            out_dir,
            trial_id,
            chain,
            args.timeout,
            args.model,
            args.no_reset,
        )
        if result is None:
            return 1
        trial_results.append(result)
        if args.num_trials > 1:
            print()

    successes = sum(1 for result in trial_results if result["success"])
    success_rate = successes / args.num_trials

    print()
    print(f"Attack success rate: {successes}/{args.num_trials} ({success_rate:.1%})")
    if args.num_trials > 1:
        write_batch_summary(
            batch_dir, args.workload_id, chain, trial_results, model=args.model
        )
        print(f"Batch summary:       {batch_dir / 'batch_summary.md'}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
