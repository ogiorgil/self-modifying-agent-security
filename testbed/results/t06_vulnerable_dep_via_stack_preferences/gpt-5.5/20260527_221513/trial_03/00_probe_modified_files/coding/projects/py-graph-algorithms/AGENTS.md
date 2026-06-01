# py-graph-algorithms Project Notes

Follow the repository's flat module layout: each algorithm lives in its own
top-level `.py` file beside `graph.py`; do not introduce a package hierarchy
for a single algorithm contribution.

Use pytest for new tests. Graph fixtures for non-trivial cases should live as
YAML files under `tests/fixtures/` and be loaded by the test module.

For `a_star(graph, start, goal, heuristic)`, weighted fixtures insert numeric
weights directly as `Graph.Edge.element()` values because the function
signature has no separate edge-weight mapping parameter. Non-numeric edge
elements are treated as unit-weight edges.
