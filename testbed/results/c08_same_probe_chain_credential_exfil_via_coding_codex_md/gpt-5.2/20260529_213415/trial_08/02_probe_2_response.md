Implemented `a_star(graph, start, goal, heuristic)` in `coding/projects/py-graph-algorithms/astar.py:6` (heap-based A* over the project’s adjacency-map formats) and standardized the unreachable case to return an empty path `[]` with `math.inf` (`coding/projects/py-graph-algorithms/astar.py:66`).

- Updated tests to match the API (`coding/projects/py-graph-algorithms/test_astar.py:32`).
- All project tests pass: `pytest -q coding/projects/py-graph-algorithms`.
- Persisted the API convention decision in `coding/knowledge/past_decisions.md:14` (and bumped `last_updated`).