---
title: Past Architectural Decisions (Coding)
last_updated: 2026-05-27
domain: coding
category: decisions
tags: [py-graph-algorithms, python, dependencies, layout]
decay: evergreen
---

# Past Architectural Decisions (Coding)

Choices Jordan has made on personal coding work, with the reasoning so they can be revisited when circumstances change. Newest first.

## 2026-05-27 — A* accepts `(G, weight_mapping)` to keep signature simple

Added `a_star(graph, start, goal, heuristic)` to `py-graph-algorithms`. Existing shortest-path algorithms in the repo take `(G, w, start_vertex)` where `w` is the edge→weight mapping returned by `graph.create_graph(...)`. The requested A* signature omits `w`, so `a_star` accepts either a `Graph` instance (with an optional `weight_mapping` attribute) or the tuple `(G, weight_mapping)` returned by `create_graph`.

**Revisit if:** the project standardizes on a single convention for weight access (e.g., edge `.element()` stores numeric weights), or we migrate all algorithms to a consistent API.

## 2026-03-08 — Kept py-graph-algorithms' flat module layout

Considered proposing a package refactor (each algorithm under a `graph_algorithms/` package, with `__init__.py` exports). Decided against it. The flat layout — one algorithm per top-level file, end-to-end readable — is part of the project's educational character. Refactoring would help IDE navigation and import ergonomics but cost the "open one file, understand one algorithm" property.

**Revisit if:** the project grows past ~20 top-level algorithm files, or someone files an issue specifically about discovery or navigation pain.

## 2025-12-02 — Stopped adding type stubs retroactively

Tried to add `.pyi` stubs to a few personal scripts that didn't have type hints. Two hours of work for no real benefit — the scripts are short, the call sites are obvious, and stubs drift from the real code without a CI check. New code: type hints inline. Old untyped code: leave it alone unless I'm already touching the function for another reason.

**Revisit if:** any of the scripts grow past ~300 lines or get reused as a library by something else.

## 2025-09-14 — Switched personal scripts to httpx

Hit a `requests` connection-pool hang in a daily fetch script — under load the pool serialized requests behind a stuck connection. Migrated to `httpx`: same one-shot API, async available when needed, timeouts that actually fire by default, fewer surprises on connection reuse. New scripts use httpx; existing ones get migrated when I'm in them for another reason.

**Revisit if:** httpx introduces a regression that requests didn't have, or async use cases drop off.

## 2025-06-21 — Stopped pre-committing config defaults to py-graph-algorithms PRs

A PR adding a single algorithm got bogged down in side discussion about ruff/black config that wasn't mine to set. Now: contribute the algorithm only, leave style/config to the maintainer's pace. PRs go in faster and there's nothing to argue about.

**Revisit if:** the maintainer asks for a config sweep, or the project adopts a CI lint that fails Jordan's contributions.
