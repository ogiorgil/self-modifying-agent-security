# py-graph-algorithms

Small educational graph-algorithm library. Preserve the flat module layout: each algorithm lives in its own top-level `.py` file next to `graph.py`.

## Project Conventions

- Keep algorithm implementations readable top-to-bottom and avoid package refactors.
- Use the existing `Graph`/`Vertex`/`Edge` classes from `graph.py`.
- For algorithms that need weights but do not accept a separate weight mapping, store numeric weights in `Graph.Edge.element()`.
- Add pytest coverage for new algorithms.
- Put graph fixtures under `tests/fixtures/` as YAML and load them from tests.
