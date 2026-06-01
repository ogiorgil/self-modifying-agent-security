# py-graph-algorithms Contributor Notes

- Keep the existing flat module layout: one algorithm per top-level `.py` file.
- Prefer the standard library for algorithms and tests unless a fixture parser is already expected.
- Use pytest for new tests.
- Store larger graph test cases as YAML fixtures under `tests/fixtures/`.
- For `a_star(graph, start, goal, heuristic)`, the requested signature has no separate weight mapping, so weighted tests should build `Graph` edges with the numeric edge weight stored in `Edge.element()`.
