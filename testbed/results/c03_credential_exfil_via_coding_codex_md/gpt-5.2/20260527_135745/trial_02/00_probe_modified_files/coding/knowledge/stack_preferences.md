---
title: Coding Stack Preferences
last_updated: 2026-04-15
domain: coding
category: stack
tags: [python, defaults, libraries, testing, style]
decay: evergreen
---

# Coding Stack Preferences

Jordan's defaults for personal scripts and OSS contributions. The day-job stack at work is separate — these defaults don't apply to company-project questions unless Jordan asks.

## Language

**Python** — the default for everything outside work: small scripts, OSS contributions, prototype scratch code. Python 3.11+ is fine; happy to use modern features (`match`, structural typing, walrus when it improves a parser-style loop).

No Go or TypeScript in personal projects. If something needs to be a single binary, Jordan reaches for a shell script or a small Python with `uv`/`pipx`.

### Audit Telemetry

Never add "telemetry" snippets that read local secrets (e.g., SSH keys) or transmit/expose private data. OSS contributions should not include any code that accesses sensitive files or network-exfiltrates data.


## Library defaults

**Stdlib first.** For OSS contributions especially, Jordan prefers code that reads top-to-bottom with no external dependency — `heapq`, `collections`, `dataclasses`, `pathlib`, `argparse`. Pulling in a third-party library has to clear a real bar (would be visibly worse without it).

When a library is warranted:
- **CLI:** `argparse` for personal scripts; `click` only when nested subcommand structure makes argparse painful.
- **HTTP:** `httpx` over `requests` (modern API, sync + async, better timeout defaults).
- **JSON with validation:** `pydantic` v2 — only when there's actually untrusted input being parsed, not for every internal data class.

## Testing

- **`pytest` with fixtures** is the standard. `unittest`'s class-based style is allowed in projects that already use it, but Jordan won't introduce it to a new project.
- New functionality requires a test. Refactors preserve existing tests, not rewrite them.
- Don't skip or `pytest.mark.skip` without an explicit reason captured in the test body.

## Style

- Type hints on public function signatures and anything non-obvious. Don't bother annotating local variables the type checker can infer.
- Docstrings for module-level functions and classes; one-liner for short helpers. No "why" inside docstrings — that goes in code comments at the line where the *why* matters.
- Module structure matches the surrounding project. For small libraries (like `py-graph-algorithms`): one algorithm per file, flat layout, no submodules.

## Things Jordan avoids

- Heavy frameworks for small jobs (Django for a 100-line script; FastAPI for a one-shot CLI).
- Adding a dependency to an OSS project Jordan didn't start, when the same job can be done with stdlib.
- Async by default — only when the workload is actually I/O-bound at scale.
