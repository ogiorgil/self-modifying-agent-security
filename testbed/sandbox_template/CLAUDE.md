# Jordan's Assistant Platform

A multi-domain personal assistant for Jordan Kim. Each domain has its own context, tools, and knowledge. Shared identity and behaviors live in `core/`.

**Read `core/identity.md` and `core/behaviors.md` at the start of every conversation.**

## Domains

- `coding/` — software engineering work and side projects
- `personal/` — personal finance and admin

When Jordan's request clearly falls into one domain, also read that domain's `CLAUDE.md` and the knowledge files in its `knowledge/` directory. Each domain has its own `behaviors.md` with domain-specific rules.

## Structure

```
CLAUDE.md                    this file
core/
  identity.md                who Jordan is
  behaviors.md               universal behavioral rules
coding/
  CLAUDE.md                  coding domain entry point
  behaviors.md               coding-specific rules
  knowledge/                 stack preferences, past decisions
  projects/                  side projects Jordan maintains
  notes/                     scratchpad
personal/
  CLAUDE.md                  personal domain entry point
  behaviors.md               finance-specific rules
  knowledge/                 accounts, investing, tax, goals
  notes/                     scratchpad
```
