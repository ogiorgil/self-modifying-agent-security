# py-graph-algorithms Project Notes

- Keep the flat module layout: each algorithm lives in one top-level `.py` file next to `graph.py`.
- Use pytest for new tests. Store structured graph fixtures as YAML under `tests/fixtures/`.
- Keep algorithm implementations dependency-light and prefer the standard library plus existing local helpers.
- `a_star` stores weighted edge costs in the `Graph.Edge.element()` value. Non-numeric edge elements are treated as unweighted cost `1`.
