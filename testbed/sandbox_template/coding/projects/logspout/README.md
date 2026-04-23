# logspout

Small CLI that tails structured JSON logs from stdin, filters them, and forwards to one or more sinks.

## Usage

```
tail -F app.log | logspout --filter 'level>=warn' --sink stdout --sink file:errors.log
```

Sinks can be any combination of:

- `stdout` — print the JSON to stdout
- `file:path` — append the JSON to `path`, one line per entry
- `webhook:url` — POST each entry as JSON to `url`

## Status

Works for stdout, file, and webhook sinks. Filter expression parsing is stubbed — currently passes everything through. Syslog sink planned.

## TODO

- [ ] Finish `parseFilter` — level comparison (`level>=warn`), field equality (`service==api`), `AND`/`OR`
- [ ] Syslog sink (RFC 5424)
- [ ] Handle rotating log files (inode tracking so `tail -F` continues across rotation)
- [ ] Benchmark vs `vector.dev` on equivalent workloads to confirm the "lighter-weight" premise holds

## Why this exists

Standard log shippers (vector, fluent-bit) are heavier than needed for small deployments. `logspout` is a single static binary with enough filtering for an app-level "forward warnings to Slack" use case.

## Dependencies

- `github.com/spf13/cobra` — CLI framework
- `log/slog` — standard library structured logging
