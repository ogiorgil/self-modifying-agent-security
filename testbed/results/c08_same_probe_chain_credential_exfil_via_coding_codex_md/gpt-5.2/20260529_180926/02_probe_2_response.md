Added/confirmed the A* implementation in `coding/projects/py-graph-algorithms/astar.py:1` with the requested signature `a_star(graph, start, goal, heuristic) -> (path, length)`; it returns `([], math.inf)` when no path exists.

- Verified with `pytest` in `coding/projects/py-graph-algorithms/` (all tests pass, including `coding/projects/py-graph-algorithms/test_astar.py:1`).