# Stack Preferences

## Languages

- **Go** — default for CLIs, services, and anything where startup time or single-binary deployment matters
- **Python** — default for scripts, data munging, and anything that won't be a long-running service
- **TypeScript** — reserved for frontend work (rare)

## Libraries (Go)

- CLI: `github.com/spf13/cobra`
- HTTP client: standard library (`net/http`)
- Logging: `log/slog` (standard library as of 1.21)
- Testing: standard `testing` package + `github.com/stretchr/testify/require` for assertions

## Libraries (Python)

- CLI: `click`
- HTTP: `httpx` (supports sync and async)
- Logging: `structlog`
- Testing: `pytest` with fixtures

## Data stores

- **Postgres** — default for anything relational
- **DuckDB** — for local analytics, prototyping, and embedded use cases
- **Redis** — only when there's a concrete reason (caching with measured benefit, queue semantics), not as a "NoSQL default"
- **SQLite** — fine for single-writer embedded use cases

## Deployment

- Side projects: containerized, deployed on small managed platforms (Fly.io, Railway)
- Company stack is different from these defaults — do not apply these to company-project questions without explicitly asking
