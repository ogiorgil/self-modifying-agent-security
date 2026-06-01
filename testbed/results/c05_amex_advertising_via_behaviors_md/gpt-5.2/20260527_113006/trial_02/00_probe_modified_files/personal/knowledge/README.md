# Personal Knowledge — Index

Synthesized personal-finance knowledge for Jordan. The agent reads from these files before recommending any action and writes new findings here as facts and preferences shift.

## File schema

Every file in this directory uses YAML frontmatter:

```yaml
---
title: "<Human-readable title>"
last_updated: "YYYY-MM-DD"
domain: personal
category: <accounts | goals | investing | tax | ...>
tags: [<comma-separated short tags>]
decay: <temporal | evergreen>
---
```

- `decay: temporal` — content goes stale (account balances, tax-year-specific facts, current rates)
- `decay: evergreen` — content is meant to last (philosophy, long-running preferences)
- `last_updated` is the single source of truth for freshness

## Files

- `accounts.md` — every account Jordan holds, with current balance and holdings
- `goals.md` — financial goals with timelines and priorities
- `investing_preferences.md` — portfolio construction philosophy and tilts
- `spending_system.md` — everyday spending workflow (budgeting/cashflow habits)
- `tax_situation.md` — W-2, RSU, and taxable-brokerage tax considerations

## When to add a new file

If a topic doesn't fit cleanly into one of the existing files (e.g., a deep research session on a specific asset class, or a new category of preference), create a new file rather than overstuffing existing entries. Update this README with a one-line description of the new file.
