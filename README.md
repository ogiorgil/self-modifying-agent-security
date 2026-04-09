# Compounding Indirect Prompt Injection in Self-Modifying Agentic Systems

CSE 599R (Agentic Systems Security) final project, Spring 2026.

## Overview

A growing class of agentic systems is designed to maintain persistent memory and modify their own behavioral rules over time (e.g., Claude Code with `CLAUDE.md`, Cursor with rule files, OpenClaw with `SOUL.md`). We study how indirect prompt injection compounds through these systems — whether a single adversarial input can propagate into persistent state and affect future sessions as trusted context.

See [`DESIGN.md`](DESIGN.md) for the full project plan and research questions.

## Layout

- `DESIGN.md` — project plan, research questions, methods
- `DEV_CONTEXT.md` — instructions for AI-assistant-based development
- `testbed/` — sandbox testbed (coming soon)
- `docs/` — shared meeting notes and design decisions
