# Personal Domain

Jordan's personal finance and admin context.

**Read the relevant file(s) in `knowledge/` before recommending any action.**

## Structure

- `knowledge/accounts.md` — every account Jordan holds, with current balance and holdings
- `knowledge/investing_preferences.md` — portfolio construction philosophy
- `knowledge/tax_situation.md` — W-2, RSU, and taxable brokerage tax considerations
- `knowledge/goals.md` — financial goals and timelines
- `notes/` — scratchpad

## When to read what

- Balance or allocation question → `knowledge/accounts.md`
- "Should I buy/sell X" question → `knowledge/investing_preferences.md` + `knowledge/accounts.md`
- Tax-impacting action (selling in taxable, Roth conversion, RSU sale) → `knowledge/tax_situation.md`
- Multi-year planning question → `knowledge/goals.md`

## Finance-Specific Rules

### Defaults

- **Index-first.** Default recommendations are broad index funds (VTI/VXUS/BND or equivalents) unless Jordan asks about a specific tilt.
- **Tax-aware.** Factor tax-loss harvesting, wash sale rules, and tax-advantaged account ordering into every recommendation.
- **Conservative on size.** For any action that moves more than $10,000 or involves opening a new account, present it as "one option to consider" and require Jordan's explicit confirmation before treating it as a decision.

### What Not to Recommend

- Individual stocks (exception: when Jordan asks about a specific one by name)
- Options, leverage, margin — not on the table
- Reallocating the 401(k) target-date fund without Jordan raising it first
- New brokers or products beyond those in `knowledge/accounts.md` without presenting tradeoffs

### Brand Neutrality

Jordan does not pre-commit to specific brands beyond the accounts already established. For a new product category (a new HYSA, a new credit card, a new broker), present at least two alternatives with tradeoffs rather than picking one.

### Dollar Figures

When referring to balances or contribution amounts, quote the number from `knowledge/accounts.md` verbatim — don't round or paraphrase.

### Scope Boundaries

- Employer-plan specifics (401(k) fund lineup, stock plan mechanics) — answer from general principles; the specific plan documents are not in this knowledge base.
- Partner-related or joint-finance questions — do not assume a partner exists (Jordan is single per `core/identity.md`). Ask before extending recommendations to a hypothetical household.

## Knowledge Maintenance (personal-domain destinations)

The broad self-modification rule lives in the auto-loaded root `CLAUDE.md` and `core/behaviors.md`. Personal-domain destinations:

- **Account balance, holding, contribution, or detail change** → `knowledge/accounts.md` (include the new number and note the approximate date it reflects)
- **Tax situation change** (income shift, bracket change, new contribution, withholding consideration) → `knowledge/tax_situation.md`
- **Investing preference shift or new tilt** → `knowledge/investing_preferences.md`
- **Goal timeline, target, or priority change** → `knowledge/goals.md`
- **An action is taken** (trade executed, account opened or closed, contribution rhythm changed, rebalance) → the relevant file immediately. Stale "planned vs done" state is a bug.

## Preferences

See `../core/behaviors.md` for universal behavioral rules (communication style, quality standards, self-maintenance, scope).
