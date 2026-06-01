# py-graph-algorithms Project Rules

- Keep the flat module layout: one top-level `.py` file per algorithm, no package refactor for routine algorithm additions.
- Use pytest for new tests. Graph-shaped test data should live as YAML files under `tests/fixtures/`.
- Avoid new runtime dependencies for algorithm implementations; prefer the standard library and existing local helpers such as `priorityQueue.py`.
- `astar.py` exposes `a_star(graph, start, goal, heuristic)` with no separate weight mapping. For weighted A* graphs, store numeric edge weights in `Edge.element()` when building fixtures or examples; nonnumeric edge elements are treated as unit-weight edges.
