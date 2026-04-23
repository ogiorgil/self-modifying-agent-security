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

Payload files are staged as local files in the sandbox working directory. They are never served over HTTP — the benign task prompt frames them as material the user has "downloaded" or "received" from an external source.

## Naming convention

`t<NN>_<short_goal>_via_<channel>` where:

- `NN` is a two-digit sequence number (ordering across workloads)
- `<short_goal>` gestures at the adversarial goal (e.g., `license_comment`, `brand_promotion`, `memory_leak`)
- `<channel>` is the primary injection channel (`readme`, `doc`, `code_comment`)

## manifest.json schema

Each `manifest.json` contains:

- **id** — must match the directory name
- **description** — one-line summary
- **attack_class**, **adversarial_goal**, **channel** — categorization per `DESIGN.md`
- **staging** — array of `{from, to}` mappings: how payload files are copied into the working directory before the exposure session
- **sessions** — named prompts (`exposure`, `stabilization`, `probe`) with their user-facing benign-task text
- **persistence_targets** — files whose modification counts as the attacker landing persistent state
- **success_criterion** — machine-checkable test (currently supports `{"type": "string_in_file", "file": "...", "string": "..."}`)

## Running a workload

```
python testbed/scripts/run_trial.py --workload <workload_id>
python testbed/scripts/run_trial.py --workload <workload_id> --chain exposure-stabilization-probe
```

The driver handles reset, staging, session chaining, diff capture, and success-criterion checking. Trial artifacts (events, responses, diffs, report) land in `testbed/results/<workload_id>/<trial_id>/` (gitignored).

## README.md vs manifest.json

- `README.md` is the human-facing workload description — useful for reading, reviewing, discussing with teammates.
- `manifest.json` is the machine-facing source of truth for the trial driver. If prompts or success criteria change, update `manifest.json`; keep `README.md` in sync but know the driver never reads it.
