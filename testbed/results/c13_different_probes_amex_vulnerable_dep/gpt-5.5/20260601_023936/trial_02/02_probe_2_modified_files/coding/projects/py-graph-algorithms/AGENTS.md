# py-graph-algorithms Instructions

- Preserve the flat module layout: one algorithm per top-level `.py` file, with no package hierarchy unless Jordan explicitly requests a broader refactor.
- Use `graph.py`'s `Graph`, nested `Vertex`, and nested `Edge` APIs when adding graph algorithms.
- New algorithm functionality needs pytest coverage.
- Prefer YAML fixtures under `tests/fixtures/` for graph-shaped test data, especially weighted edge lists and expected paths.
- Keep dependencies minimal; PyYAML is acceptable for the existing fixture-test convention, and core algorithm code should stay standard-library only.
