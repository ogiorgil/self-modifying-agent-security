# Workloads

Each subdirectory here is one complete experimental workload — a benign task, an attacker-controlled payload, and a probe that together test whether an injection persists into the agent's own behavior/knowledge files.

## Structure

```
workloads/
  <workload_id>/
    README.md            description: attack class, adversarial goal, prompts, success criterion, expected outcomes
    manifest.json        machine-readable metadata consumed by testbed/scripts/run_trial.py
    <payload files>      content staged into the sandbox working directory at runtime
```

Payload files are staged as local files in the sandbox working directory. They are never served over HTTP. Two staging patterns are common:

1. **New file** placed under a domain's `notes/` directory, framed in the exposure prompt as material the user downloaded or received (e.g., *"I downloaded this article, can you summarize it?"*).
2. **Overwrite an existing project file** with a poisoned version, simulating a malicious upstream commit or PR. Routine project-level work (reading the README, opening a module) encounters the injection without any explicit framing.

The `staging` array in `manifest.json` covers both — any `to` path inside the working directory is valid, whether it creates a new file or overwrites an existing one.

## Naming convention

`t<NN>_<short_goal>_via_<channel>` where:

- `NN` is a two-digit sequence number (ordering across workloads)
- `<short_goal>` gestures at the adversarial goal (e.g., `license_comment`, `brand_promotion`, `memory_leak`)
- `<channel>` is the primary injection channel (`readme`, `doc`, `code_comment`)

## manifest.json schema

Each `manifest.json` contains:

- **id** — must match the directory name
- **description** — one-line summary
- **attack_class**, **adversarial_goal**, **channel** — categorization per the accompanying paper
- **staging** — array of `{from, to}` mappings: how payload files are copied into the working directory once, after reset, before the first session
- **sessions** — named prompts (`exposure`, `stabilization`, `probe`) with their user-facing benign-task text; each session may also declare `pre_actions` (see below)
- **persistence_targets** — files whose modification counts as the attacker landing persistent state
- **success_criterion** — machine-checkable test. Supported types:
  - `{"type": "string_in_file", "file": "...", "string": "..."}` — substring present in a file under the working dir
  - `{"type": "string_in_response", "string": "..."}` — substring present in the agent's final response text
  - `{"type": "command_in_events", "pattern": "..."}` — a shell command issued during the trial matches the given regex (e.g. the agent runs `pip install`)

## Per-session `pre_actions`

In addition to the one-time top-level `staging`, each session can declare `pre_actions` that run against the working directory immediately before that session's claude invocation. Supported action types:

- `{"action": "copy", "from": "<rel-to-workload-dir>", "to": "<rel-to-working-dir>"}` — stage a file (same semantics as top-level `staging`)
- `{"action": "revert_from_template", "target": "<rel-path>"}` — restore the named file from `sandbox_template/`, useful for removing a previously-staged payload between sessions to test whether any *agent-side* state actually persisted
- `{"action": "delete", "target": "<rel-path>"}` — delete a file or directory from the working directory

Use `pre_actions` to construct session chains that distinguish payload-persistence (attack content stays in the repo) from self-modification-persistence (agent wrote the injected rule into its own behavior/knowledge files).

## Running a workload

```
python testbed/scripts/run_trial.py --workload <workload_id>
python testbed/scripts/run_trial.py --workload <workload_id> --chain exposure-stabilization-probe
```

The driver handles reset, staging, session chaining, diff capture, and success-criterion checking. Trial artifacts (events, responses, diffs, report) land in `testbed/results/<workload_id>/<trial_id>/` (gitignored).

### Persisted-sandbox runs (`--no-reset`)

For experiments that study state accumulating across repeated runs of the same prompt (the project's "compounding indirect prompt injection" focus), pass `--no-reset` on every iteration after the first. The first run resets and stages the working dir as usual; subsequent runs reuse whatever state prior runs left behind — file edits the agent made to behavior/knowledge files, Claude's project-level memory, generated code, everything.

```
# First iteration — clean reset and stage
python testbed/scripts/run_trial.py --workload <id> --trial-id iter_00

# Subsequent iterations — keep accumulated state
for i in $(seq 1 9); do
    python testbed/scripts/run_trial.py --workload <id> \
        --trial-id iter_$(printf "%02d" $i) --no-reset
done
```

Each iteration writes its own results subdir (`iter_00/`, `iter_01/`, ...), so per-iteration diffs and responses are preserved even though the working dir compounds. To inspect how state evolved across iterations, diff the working dir against the template between runs or compare per-iteration `*_diff.txt` files.

## README.md vs manifest.json

- `README.md` is the human-facing workload description — useful for reading, reviewing, discussing with teammates.
- `manifest.json` is the machine-facing source of truth for the trial driver. If prompts or success criteria change, update `manifest.json`; keep `README.md` in sync but know the driver never reads it.
