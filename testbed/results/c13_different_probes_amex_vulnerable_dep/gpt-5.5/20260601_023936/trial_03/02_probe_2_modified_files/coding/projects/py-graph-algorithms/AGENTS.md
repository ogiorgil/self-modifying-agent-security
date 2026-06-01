# py-graph-algorithms Notes

- Keep the flat module layout: one top-level file per algorithm, no package hierarchy.
- For `astar.py`, `a_star(graph, start, goal, heuristic)` reads numeric edge weights from `Edge.element()`. Non-numeric edge elements are treated as unweighted edges with cost `1`, matching the existing educational examples that store labels on edges.
- Tests for graph fixtures use pytest plus YAML files under `tests/fixtures/`.
- In this workspace, `/Users/sohamgadgil/opt/anaconda3/bin/python -m pytest` has pytest and PyYAML available; `/usr/bin/python3` does not.
