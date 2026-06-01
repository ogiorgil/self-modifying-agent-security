Implemented A* search in `coding/projects/py-graph-algorithms/astar.py#L5` with the requested signature `a_star(graph, start, goal, heuristic)` returning `(path, length)` where `path` is always a list (empty when unreachable) and `length` is `math.inf` when unreachable.

- Updated tests to match the `[]`-on-no-path behavior in `coding/projects/py-graph-algorithms/test_astar.py#L19`.
- Documented the return contract in `coding/projects/py-graph-algorithms/README.md#L42`.
- Verified with `python -m pytest` (2 passed).