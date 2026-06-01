Added/updated A* search for `py-graph-algorithms`.

- Implemented `a_star(graph, start, goal, heuristic)` in `coding/projects/py-graph-algorithms/astar.py:1`, returning `(path, length)` where `path` is a node list and `length` is the total cost (or `([], math.inf)` if unreachable).
- Verified with existing tests: `pytest -q` passes (`coding/projects/py-graph-algorithms/test_astar.py:1`).
- Persisted a small project convention note in `coding/projects/py-graph-algorithms/AGENTS.md:1` (notably that `Graph.incident_edges(...)` can return `None`).