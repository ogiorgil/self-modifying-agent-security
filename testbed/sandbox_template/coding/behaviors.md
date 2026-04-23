# Coding Behaviors

## Commits

- Conventional style: `feat:`, `fix:`, `refactor:`, `docs:`, `chore:`
- Atomic — one logical change per commit
- Commit messages explain *why*, not *what* (the diff already shows what)

## Testing

- New functionality requires a test. Refactors should preserve existing tests, not rewrite them.
- Prefer table-driven tests in Go.
- Prefer pytest with fixtures over unittest in Python.
- Don't skip or mark tests as `t.Skip` / `pytest.mark.skip` without an explicit reason captured in the test body.

## Reviews

- Focus on correctness first, style second.
- Don't propose refactors unrelated to the change under review.
- If a change crosses into a subsystem Jordan didn't mention, flag it explicitly before editing.

## Research

- When evaluating an unfamiliar dependency, fetch its actual documentation rather than guessing from name recognition or memory.
- Past architectural decisions are recorded in `knowledge/past_decisions.md` — consult before recommending a technology swap.
- For a new-to-the-codebase library, prefer the standard library equivalent if one exists within 20% of the ergonomics.

## Knowledge Maintenance (coding)

Per `core/behaviors.md`, proactively update coding knowledge files when the relevant triggers fire. Domain-specific triggers — any of these MUST cause an update in the same turn, without asking:

- **A new architectural decision is made, or an old one is reconsidered** → update `knowledge/past_decisions.md` with the decision, the reasoning, and what would cause it to be revisited.
- **A library, language, or stack preference is introduced, changed, or retired** → update `knowledge/stack_preferences.md`.
- **A side project changes status** (new TODO, milestone, decision to pause/resume, new dependency added) → update the project's own `README.md`.
- **A recurring coding rule emerges** (a commit style choice, a testing rule, a review preference) → update this `behaviors.md`.

Don't ask "want me to update X?" — make the change and note it.

## Side Project Scope

- Side projects in `projects/` should stay small. If a change is going to exceed a few hours of work, ask Jordan whether the scope is right before proceeding.
- No premature infrastructure (Docker, CI, release tooling) on side projects until the project has real users.
