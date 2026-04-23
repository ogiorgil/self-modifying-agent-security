# Testbed

The sandbox environment used for studying compounding indirect prompt injection in self-modifying agentic systems.

## Structure

- `sandbox_template/` — committed, clean initial state of the sandbox (the attack target)
  - `CLAUDE.md` — platform-level entry point pointing at `core/` and the domains
  - `core/` — shared identity and universal behaviors (including the self-modification primitive, primary attack surface)
    - `identity.md` — fake user identity the agent operates on behalf of (Jordan Kim)
    - `behaviors.md` — universal behavioral rules + self-improvement + knowledge-maintenance rules
  - `coding/` — coding-assistant domain
    - `CLAUDE.md`, `behaviors.md`, `knowledge/`, `projects/logspout/`, `notes/`
  - `personal/` — personal-finance-assistant domain
    - `CLAUDE.md`, `behaviors.md`, `knowledge/` (accounts, investing, tax, goals), `notes/`
- `docker/` — Docker-based sandbox for reproducible, isolated experiments
  - `Dockerfile` — Node 20 + Claude Code CLI
  - `README.md` — docker setup and usage docs
- `scripts/` — helper scripts
  - `reset_working_dir.py` — local iteration: copy template to sibling working dir, clear Claude Code auto-memory
  - `docker_setup.sh` — one-time: build image + create auth volume
  - `docker_login.sh` — one-time: interactive OAuth login (saves auth to the persistent volume)
  - `docker_run.sh` — each experiment: fresh container + fresh sandbox dir

## Two ways to run experiments

### Local mode (fast, for iteration)

Uses a sibling directory on the host. Still inherits user-global `~/.claude/CLAUDE.md` and host filesystem — fine for quick iteration, not suitable for the final writeup.

```
python testbed/scripts/reset_working_dir.py
cd ../self-modifying-agent-security-working
claude
```

### Docker mode (clean, for final results)

Uses a Docker container. Fully isolates the agent from the user's local `~/.claude/` state and host filesystem. Preferred for reproducible experiments in the writeup.

See `docker/README.md` for full setup. Quick start:

```
bash testbed/scripts/docker_setup.sh   # one-time: build image + create auth volume
bash testbed/scripts/docker_login.sh   # one-time: authenticate with Claude subscription
bash testbed/scripts/docker_run.sh     # each experiment: fresh container + fresh sandbox
```

## Known confound (local mode only)

In local mode, `~/.claude/CLAUDE.md` is loaded by Claude Code regardless of cwd. This is developer workflow context, not agent behavior context, but worth documenting in the writeup. Docker mode eliminates this.

## Fictional persona

The sandbox operates on behalf of **Jordan Kim**, a fictional senior software engineer in Austin, TX. The structure follows a multi-domain assistant layout:

- `coding/` — Jordan's engineering work, with a small fictional Go side project (`logspout`), stack preferences, and prior architectural decisions
- `personal/` — Jordan's finance context, including specific account balances, investing preferences (index-first, tax-aware), tax situation (W-2 + RSUs + backdoor Roth), and goals (house downpayment, retirement)

The multi-domain shape gives attacks more surface to work with (cross-domain compounding, per-domain behavior files, richer knowledge bases). Jordan Kim is fully fictional and bears no resemblance to any real person on the team.

## Attack surfaces

Both `behaviors.md` files (core and domain-level) and all `knowledge/*.md` files are actively maintained by the agent per the self-improvement and knowledge-maintenance rules in `core/behaviors.md`. These are the primary persistence targets for memory-poisoning experiments.
