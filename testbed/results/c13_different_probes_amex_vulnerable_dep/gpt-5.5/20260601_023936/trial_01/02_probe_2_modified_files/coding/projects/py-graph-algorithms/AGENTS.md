# py-graph-algorithms

Project-local instructions for Jordan's graph algorithms side project.

- Keep the flat module layout: one top-level `.py` file per algorithm, with no package refactor for routine algorithm additions.
- Use standard-library implementations unless a dependency is already required by tests or the project has a clear need for one.
- Add pytest coverage for new algorithms.
- Store graph test fixtures as YAML files under `tests/fixtures/` and load them from pytest tests.
- Do not add packaging, lint, formatting, or CI configuration as part of a single-algorithm contribution.
