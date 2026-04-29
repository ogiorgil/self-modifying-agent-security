---
title: Python Packaging Landscape
last_updated: 2026-03-22
domain: coding
category: landscape
tags: [python, packaging, uv, poetry, pip-tools, hatch, oss]
decay: temporal
---

# Python Packaging Landscape

Synthesized from a research session on 2026-03-22 — Jordan was deciding how to handle the next-generation packaging story for personal scripts and (later) potential PRs that touch py-graph-algorithms' build setup. Captured here so the same ground doesn't get re-walked next time the question comes up.

## TL;DR

For personal scripts and one-off tools: **`uv`** is the default — the install latency advantage over pip alone is enough to change everyday behavior, and lockfile + `uv run` cover the workflow without ceremony.

For OSS contribution to py-graph-algorithms specifically: **don't push a packaging change**. The project has no `pyproject.toml`, no declared dependencies, and is single-file-per-algorithm. Modernizing the build is out of scope for an algorithm contribution and would invite a long maintainer review on something that isn't broken.

## Tools surveyed

### uv (Astral)

- Rust-based installer + resolver + project manager. Drop-in replacement for `pip install` and `pip-tools`.
- Dramatically faster than pip for cold-cache installs (10-100×) and effectively free on warm cache.
- `uv pip install` is the migration path; `uv add` / `uv lock` / `uv run` is the project-management path.
- Locks via `uv.lock` (TOML, deterministic).
- Reads `pyproject.toml` (PEP 621). No proprietary metadata format.
- **What it's good for:** scripts, internal tooling, fast CI installs, anything where install speed compounds.
- **What it's not:** a build backend (uv calls hatchling/setuptools/etc. when building wheels).

### poetry

- Older "do-everything" tool: dependency management, lockfile, build, publish.
- Resolver is correct but slow on large dep graphs.
- Uses its own metadata extension (`[tool.poetry]` table) — pre-PEP-621, though they support PEP 621 now.
- Lockfile (`poetry.lock`) is canonical for poetry projects.
- Strong workflow ergonomics if you're inside the poetry world; less pleasant if you need to interop with pip-only environments.
- **Where it still shines:** projects already using it, especially those publishing to PyPI with poetry's build backend. Switching costs are real.

### pip-tools (`pip-compile` / `pip-sync`)

- Minimal: takes a `requirements.in` and produces a pinned `requirements.txt`.
- No project management, no environment management — just deterministic resolution.
- Plays well with anything that consumes `requirements.txt`.
- **Where it still shines:** simple apps and services where the pinned `requirements.txt` is the source of truth and additional tooling is overhead.
- Slower than uv but stable and well-understood; many teams keep it for inertia reasons.

### hatch

- Modern build backend (`hatchling`) plus environment manager.
- `hatchling` is the most pleasant build backend right now if you're authoring a library — minimal config, supports PEP 621 metadata directly, plays well with tag-based versioning.
- Hatch-the-environment-manager is fine but increasingly redundant once `uv` enters the workflow.
- **What it's good for:** library authoring (use `hatchling` as the build backend even if `uv` is the project manager).

## How they fit together

There's an emerging consensus split:

| Concern | Tool |
|---|---|
| Project management (env, lock, run) | `uv` |
| Build backend (for libraries) | `hatchling` (via `pyproject.toml`) |
| Dependency resolution | built into `uv` |
| Publishing to PyPI | `uv publish` (newer) or `python -m build` + `twine` |

Poetry-the-everything-tool is starting to look monolithic next to this layered stack.

## What this means for Jordan's work

- **Personal scripts:** use `uv` (`uv init`, `uv add`, `uv run`). Don't bother with poetry.
- **py-graph-algorithms PRs:** don't touch the packaging story. The project predates `pyproject.toml` adoption in this corner of educational OSS, and a packaging modernization PR is its own conversation.
- **A new OSS library, if Jordan ever starts one:** `pyproject.toml` with `hatchling` as the build backend, `uv` for development, `uv publish` for the release.
- **CI:** the `uv` install step is a clean win even on existing projects — small PR, quantifiable speedup, no behavior change.

## Revisit if

- `uv` introduces breaking changes to its lockfile format or CLI before it stabilizes
- Astral's commercial trajectory (open-source rug-pull risk) materially changes
- Poetry ships a Rust-rewrite resolver that closes the speed gap (rumored, not shipped as of this write-up)
