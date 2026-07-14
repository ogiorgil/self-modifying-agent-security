## Overview

A growing class of agentic systems is designed to maintain persistent memory and modify their own behavioral rules over time (e.g., Claude Code with `CLAUDE.md`, Cursor with rule files, OpenClaw with `SOUL.md`). We study how indirect prompt injection compounds through these systems — whether a single adversarial input can propagate into persistent state and affect future sessions as trusted context.

See the accompanying paper for the full threat model, evaluation protocol, and research questions.

## Current Status

- **Threat model & evaluation protocol:** defined (see the accompanying paper)
- **Testbed:** multi-domain sandbox at `testbed/sandbox_template/` with a fictional user, two domains (coding + personal) sharing a core, and a real MIT-licensed open-source project (`py-graph-algorithms`) as the coding-domain side project. Self-modification primitive verified firing on benign triggers.
- **Attack payload delivery:** local files staged into the working dir at trial time — either a new file framed as user-downloaded material, or an existing project file overwritten with a poisoned version (e.g., a malicious upstream README).
- **Trial driver:** built (`testbed/scripts/run_trial.py`). Supports session chains (exposure / stabilization / probe) with per-session `pre_actions` for mid-trial mutations (copy / revert_from_template / delete).
- **Self-modification primitive:** broad — fires on any durable convention or fact encountered (project conventions, contributor guidelines, library choices, etc.) without requiring user-voicing or prior contradictions. Inlined in the always-loaded root `CLAUDE.md` so it's reliably in context regardless of the agent's reading discipline; the canonical version lives in `core/behaviors.md`.
- **Baseline workload:** `t01_license_comment_via_readme` — directive-at-agent injection with implausible reasoning → **blocked at detection**. Useful as the obvious-attack control.

## Layout

- `testbed/` — sandbox testbed, experimental workloads, results, and helper scripts
  - `README.md` — testbed overview and how-to-run-experiments guide
  - `ATTACK_DESIGN.md` — catalogue of attack ideas derived from the sandbox's structure
  - `sandbox_template/` — clean initial state of the attack target (multi-domain self-modifying assistant)
  - `workloads/` — experimental workloads, one subdirectory per workload with `manifest.json` and a `README.md` (see `workloads/README.md` for the schema)
  - `results/` — committed per-trial artifacts (events JSON, response transcripts, diffs, trial reports). Layout: `<workload_id>/<trial_id>/`
  - `scripts/` — `run_trial.py` (trial driver) and `reset_working_dir.py` (manual-mode helper)
