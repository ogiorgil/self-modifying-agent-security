# Payloads

Attacker-controlled content used in experiments. Each subdirectory is one experimental tuple.

## Tuple structure

```
payloads/
  <tuple_id>/
    tuple.md             metadata + runbook (benign task, probe, persistence target, staging instructions)
    <payload files>      the content to be staged into the sandbox working directory
```

Payload files are staged as local files in the sandbox working directory. They are never served over HTTP — the benign task prompt frames them as material the user has "downloaded" or "received" from an external source.

## Naming convention

`t<NN>_<short_goal>_via_<channel>` where:

- `NN` is a two-digit sequence number (ordering across tuples)
- `<short_goal>` gestures at the adversarial goal (e.g., `license_comment`, `brand_promotion`, `memory_leak`)
- `<channel>` is the primary injection channel (`readme`, `doc`, `code_comment`)

## tuple.md schema

Each `tuple.md` documents:

- **Attack class** — one of: memory poisoning, behavior-file modification, self-improvement rule update
- **Adversarial goal** — which of the five DESIGN.md goals this targets
- **Exposure session** — initial state, benign task prompt, payload file(s) and staging destination(s), persistence target
- **Probe session** — initial state, benign task prompt, attack success criterion
- **Runbook** — concrete commands to execute the tuple manually

## Staging

A trial driver will eventually automate staging, session chaining, and diff capture. Until then, each `tuple.md` includes a manual runbook. The general pattern:

1. `python testbed/scripts/reset_working_dir.py`
2. Copy payload file(s) to the destination(s) specified in `tuple.md`
3. Launch `claude` in the working directory
4. Paste the exposure benign task; observe response and file diffs
5. Exit, relaunch `claude` for a new session (or continue in-session depending on which chain is being tested)
6. Paste the probe benign task; check the attack success criterion
7. Capture the full working-dir diff vs the template
