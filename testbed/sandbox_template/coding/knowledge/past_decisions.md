# Past Decisions

Architectural choices worth remembering, with the reasoning so they can be revisited when circumstances change.

## 2025-11 — Go over Rust for logspout

Evaluated both for the log-tailer side project. Rust compile times and the smaller ecosystem for log sinks outweighed the performance/safety gains for this workload. Go's `log/slog` and standard library HTTP covered 95% of what was needed. Revisit only if CPU profiling ever becomes a concern (unlikely for a log tailer).

## 2025-09 — Dropped TypeScript for scripts

Tried Bun/TypeScript for a handful of personal scripts. Startup time was fine, but the type setup for small scripts was heavier than the Python equivalent. Reserved TS for frontend only.

## 2025-07 — Stopped using Redis as default

Was using Redis for small jobs that didn't need it — plain Python dicts or a single Postgres table would've worked. Committed to "Redis only when there's a measured reason" going forward. No regrets.

## 2024-Q4 — Switched from Django to FastAPI for new services

Django's ORM and admin were overkill for the services being built. Now using FastAPI + SQLAlchemy when async matters, FastAPI + plain SQL otherwise. Keep Django only for existing services where the admin is actually used.

## 2024-Q2 — Standardized on Postgres over MySQL

The services team was split. Consolidated on Postgres for better JSON support, stronger constraint enforcement, and better tooling. MySQL only for existing services that haven't migrated yet.
