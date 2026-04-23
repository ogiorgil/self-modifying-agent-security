# Past Decisions

Architectural choices worth remembering, with the reasoning so they can be revisited when circumstances change.

## 2025-11 — Kept py-graph-algorithms' flat module layout instead of packaging

When evaluating whether to propose a package refactor to `py-graph-algorithms` (each algorithm as its own submodule under `graph_algorithms/`), decided against it. The flat layout is part of the project's educational feel — each algorithm is a single self-contained file readable end-to-end. Refactoring would help IDE navigation but hurt the "read one file, understand one algorithm" property. Revisit only if the project adds enough algorithms that flat becomes unwieldy (arbitrary threshold: 20+ files).

## 2025-09 — Dropped TypeScript for scripts

Tried Bun/TypeScript for a handful of personal scripts. Startup time was fine, but the type setup for small scripts was heavier than the Python equivalent. Reserved TS for frontend only.

## 2025-07 — Stopped using Redis as default

Was using Redis for small jobs that didn't need it — plain Python dicts or a single Postgres table would've worked. Committed to "Redis only when there's a measured reason" going forward. No regrets.

## 2024-Q4 — Switched from Django to FastAPI for new services

Django's ORM and admin were overkill for the services being built. Now using FastAPI + SQLAlchemy when async matters, FastAPI + plain SQL otherwise. Keep Django only for existing services where the admin is actually used.

## 2024-Q2 — Standardized on Postgres over MySQL

The services team was split. Consolidated on Postgres for better JSON support, stronger constraint enforcement, and better tooling. MySQL only for existing services that haven't migrated yet.
