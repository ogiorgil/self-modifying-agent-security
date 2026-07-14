# Testbed

The sandbox environment used for studying compounding indirect prompt injection in self-modifying agentic systems.

## Structure

- `sandbox_template/` — committed, clean initial state of the Claude Code sandbox (the attack target)
  - `CLAUDE.md` — platform-level entry point; the broad self-modification primitive is inlined here so it's always loaded
  - `core/` — shared identity and universal behaviors (the canonical self-modification primitive lives here, primary attack surface)
    - `identity.md` — fake user identity the agent operates on behalf of (Jordan Kim)
    - `behaviors.md` — universal behavioral rules + canonical self-modification primitive
  - `coding/` — coding-assistant domain
    - `CLAUDE.md` — domain entry point with coding-specific rules inline
    - `knowledge/` — stack preferences, past decisions, prior research synthesis (with YAML frontmatter and a `README.md` index)
    - `projects/py-graph-algorithms/` — real MIT-licensed Python graph library (cloned)
    - `notes/` — scratchpad
  - `personal/` — personal-finance-assistant domain
    - `CLAUDE.md` — domain entry point with finance-specific rules inline
    - `knowledge/` — accounts, goals, investing, tax (with YAML frontmatter and a `README.md` index)
    - `notes/` — scratchpad
- `sandbox_template_codex/` — Codex variant of the same sandbox, using `AGENTS.md` entry points in place of `CLAUDE.md`
- `workloads/` — experimental workloads, one subdirectory per `(initial state, benign task, attack payload, persistence target, success criterion)` tuple
  - See `workloads/README.md` for the manifest schema and naming convention
- `results/` — per-trial artifacts (events JSON, response transcripts, diffs, trial reports). Claude layout: `<workload_id>/<trial_id>/`; Codex layout: `<workload_id>/<model>/<trial_id>/`
- `ATTACK_DESIGN.md` — catalogue of attack ideas derived from the sandbox's structure, used to inform new workload designs
- `scripts/` — helper scripts
  - `run_trial.py` — trial driver. Resets the working dir, stages payloads, runs `claude -p` for each session in the chain, captures diffs, checks the success criterion, writes artifacts under `results/`. Supports per-session `pre_actions` for mid-trial mutations.
  - `run_trial_codex.py` — Codex trial driver. Uses `sandbox_template_codex/`, runs `codex exec --json`, captures the Codex JSONL event stream, final response, diffs, and the same report format.
  - `reset_working_dir.py` — local iteration: copy template to sibling working dir, clear Claude Code auto-memory

## Running experiments

Experiments run in a sibling directory on the host. This inherits the user-global `~/.claude/CLAUDE.md` and host filesystem (see the confound note below).

```
python testbed/scripts/reset_working_dir.py
cd ../self-modifying-agent-security-working
claude
```

For Codex:

```
python testbed/scripts/run_trial_codex.py --workload c03_credential_exfil_via_coding_codex_md --prepare-only
cd ../self-modifying-agent-security-working-codex
codex
```

Headless Codex trials use the same workload schema:

```
python testbed/scripts/run_trial_codex.py --workload c03_credential_exfil_via_coding_codex_md --chain probe
```

Workloads that explicitly poison or check `CLAUDE.md` paths should be duplicated or adjusted to target `AGENTS.md` paths when testing Codex auto-loaded instructions.

## Known confound

`~/.claude/CLAUDE.md` is loaded by Claude Code regardless of cwd. This is developer workflow context, not agent behavior context, but worth documenting.

## Fictional persona

The sandbox operates on behalf of **Jordan Kim**, a fictional senior software engineer in Austin, TX. The structure follows a multi-domain assistant layout:

- `coding/` — Jordan's engineering work, framed as occasional contributions to a real open-source Python graph library ([`py-graph-algorithms`](https://github.com/Sorrop/py-graph-algorithms), MIT), plus stack preferences and prior architectural decisions
- `personal/` — Jordan's finance context, including specific account balances, investing preferences (index-first, tax-aware), tax situation (W-2 + RSUs + backdoor Roth), and goals (house downpayment, retirement)

The multi-domain shape gives attacks more surface to work with (cross-domain compounding, richer knowledge bases, more places where synthesized findings can land). Jordan Kim is fully fictional and bears no resemblance to any real person.

## Attack surfaces

`core/behaviors.md`, the domain `CLAUDE.md` files, and all `knowledge/*.md` files are actively maintained by the agent per the self-modification primitive in `core/behaviors.md` (also inlined in the root `CLAUDE.md`). These are the primary persistence targets for memory-poisoning and behavior-modification experiments. See `ATTACK_DESIGN.md` for the full attack-surface catalogue.
