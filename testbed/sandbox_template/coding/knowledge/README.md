# Coding Knowledge — Index

Synthesized knowledge from prior sessions. The agent reads from these files at task start and writes new findings here as they accumulate.

## File schema

Every file in this directory uses YAML frontmatter:

```yaml
---
title: "<Human-readable title>"
last_updated: "YYYY-MM-DD"
domain: coding
category: <stack | decisions | landscape | tooling | ...>
tags: [<comma-separated short tags>]
decay: <temporal | evergreen>
---
```

- `decay: temporal` — content goes stale (tooling landscapes, library versions, performance benchmarks)
- `decay: evergreen` — content is meant to last (architectural decisions, opinionated preferences)
- `last_updated` is the single source of truth for freshness — don't add inline "last updated" lines

## Files

- `stack_preferences.md` — Python defaults Jordan reaches for in personal scripts and OSS contributions
- `past_decisions.md` — architectural choices on personal coding work, with reasoning and revisit conditions
- `python_packaging_landscape.md` — survey of Python packaging tools (`uv`, `poetry`, `pip-tools`, `hatch`) with the angle Jordan cared about for OSS distribution

## When to add a new file

When a research or synthesis task produces durable findings that don't fit cleanly into an existing file, create a new one rather than overstuffing the existing entries. Update this README with a one-line description of the new file.
