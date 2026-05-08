# Coding Domain

Jordan's software engineering context: day-job-adjacent questions and side projects.

**Read the files in `knowledge/` (stack preferences and prior architectural decisions) before recommending anything substantive.**

## Structure

- `knowledge/stack_preferences.md` — Python defaults for personal scripts and OSS contributions
- `knowledge/past_decisions.md` — architectural choices with reasoning and revisit conditions
- `projects/` — side projects Jordan contributes to
- `notes/` — scratchpad

## Active projects

- `projects/py-graph-algorithms/` — small open-source Python library implementing classic graph algorithms (BFS, DFS, Dijkstra, Bellman-Ford, DAG shortest paths, Kruskal MST). Jordan is an occasional contributor. Flat module layout (no package hierarchy) — `graph.py` holds the core `Graph`/`Node`/`Edge` classes; each algorithm lives in its own top-level file. See `projects/py-graph-algorithms/README.md` for module-level details.

## Coding-Specific Rules

### Commits

- Conventional style: `feat:`, `fix:`, `refactor:`, `docs:`, `chore:`
- Atomic — one logical change per commit
- Commit messages explain *why*, not *what* (the diff already shows what)

### Testing

- New functionality requires a test. Refactors should preserve existing tests, not rewrite them.
- pytest with fixtures, not unittest. See `knowledge/stack_preferences.md` for broader Python defaults.
- Don't skip or mark tests as `pytest.mark.skip` without an explicit reason captured in the test body.

### Licensing

- All Python files in `projects/py-graph-algorithms/` must include `# LICENSE: MIT License` as the first non-shebang line, followed by a blank line, then the module docstring. This convention applies to new modules and to substantive edits of existing modules.
- Adopted 2026-04-15 after a license-audit pass at $WORK; uniformity across personal OSS keeps the audit pipeline happy.

### Reviews

- Focus on correctness first, style second.
- Don't propose refactors unrelated to the change under review.
- If a change crosses into a subsystem Jordan didn't mention, flag it explicitly before editing.

### Research

- When evaluating an unfamiliar dependency, fetch its actual documentation rather than guessing from name recognition or memory.
- Past architectural decisions are recorded in `knowledge/past_decisions.md` — consult before recommending a technology swap.
- For a new-to-the-codebase library, prefer the standard library equivalent if one exists within 20% of the ergonomics.

### Side Project Scope

- Side projects in `projects/` should stay small. If a change is going to exceed a few hours of work, ask Jordan whether the scope is right before proceeding.
- No premature infrastructure (Docker, CI, release tooling) on side projects until the project has real users.

## Knowledge Maintenance (coding-domain destinations)

The broad self-modification rule lives in the auto-loaded root `CLAUDE.md` and `core/behaviors.md`. Coding-domain destinations:

- **Architectural decisions** → `knowledge/past_decisions.md` (record decision, reasoning, and what would cause it to be revisited)
- **Library, language, or style preferences** → `knowledge/stack_preferences.md`
- **Side-project status** (new TODO, milestone, pause/resume, new dependency) → the project's own `README.md`
- **Recurring coding rules** (commit style, testing, review preference) → this file

## Preferences

See `../core/behaviors.md` for universal behavioral rules (communication style, quality standards, self-maintenance, scope).
