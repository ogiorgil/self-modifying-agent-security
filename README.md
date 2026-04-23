# Compounding Indirect Prompt Injection in Self-Modifying Agentic Systems

CSE 599R (Agentic Systems Security) final project, Spring 2026.

## Overview

A growing class of agentic systems is designed to maintain persistent memory and modify their own behavioral rules over time (e.g., Claude Code with `CLAUDE.md`, Cursor with rule files, OpenClaw with `SOUL.md`). We study how indirect prompt injection compounds through these systems — whether a single adversarial input can propagate into persistent state and affect future sessions as trusted context.

See [`DESIGN.md`](DESIGN.md) for the full project plan, threat model, evaluation protocol, and research questions.

## Current Status

- **Threat model & evaluation protocol:** defined (see `DESIGN.md`)
- **Testbed:** multi-domain sandbox at `testbed/sandbox_template/` with a fictional user and rich knowledge/behavior surface; self-modification primitive verified
- **Attack payload delivery:** local files staged into the working dir at trial time — either a new file framed as user-downloaded material, or an existing project file overwritten with a poisoned version (e.g., a malicious upstream README)
- **Trial driver:** pending
- **First end-to-end experiment:** pending

## Layout

- `DESIGN.md` — project plan, threat model, evaluation protocol, research questions
- `DEV_CONTEXT.md` — instructions for AI-assistant-based development on this repo
- `testbed/` — sandbox testbed and experiment scripts
  - `sandbox_template/` — clean initial state of the attack target
  - `scripts/` — reset and (soon) trial driver scripts
  - `docker/` — optional Docker-based sandbox (deferred until after interim presentation)
