# py-graph-algorithms

Classic graph algorithms are implemented as flat top-level modules. Keep one algorithm per file and avoid package refactors for routine algorithm additions.

## Conventions

- Prefer standard-library data structures and helpers; do not add third-party runtime dependencies for algorithm implementations.
- Public algorithm functions should include a short docstring matching the existing input/output style.
- Tests use pytest. YAML fixtures live under `tests/fixtures/` for graph structures that are easier to read as data than as Python literals.
- The existing `Graph` class stores edge elements separately from the weight mappings returned by `create_graph`; new algorithms with a fixed signature should document or test how they receive edge weights.
