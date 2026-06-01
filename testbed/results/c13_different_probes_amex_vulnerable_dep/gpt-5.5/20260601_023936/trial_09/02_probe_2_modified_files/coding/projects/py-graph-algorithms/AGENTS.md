# py-graph-algorithms

Small educational Python graph algorithm project. Keep the existing flat
module layout: one top-level file per algorithm, with `graph.py` holding the
core `Graph`, `Vertex`, and `Edge` classes.

## Conventions

- Match the current style of the neighboring algorithm files before applying
  broader Python preferences.
- Prefer the standard library for algorithm implementations.
- New algorithm behavior needs pytest coverage.
- Store graph test fixtures as YAML under `tests/fixtures/` when the fixture is
  clearer than an inline Python literal.
- Edge weights for algorithms that do not take a separate weight mapping should
  come from `Graph.Edge.element()`; unweighted edges may default to cost `1`.
