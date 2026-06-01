Added A* search to `py-graph-algorithms`.

- New implementation: `coding/projects/py-graph-algorithms/astar.py` (function `a_star(graph, start, goal, heuristic)` returns `(path, length)`; unreachable returns `([], math.inf)`).
- Docs: updated `coding/projects/py-graph-algorithms/README.md` to include `astar.py`.
- Persisted project decision: updated `coding/knowledge/past_decisions.md` with the A* module + edge-cost convention.
- Verified: `python -m py_compile coding/projects/py-graph-algorithms/astar.py` passes; quick weighted-Graph smoke test succeeds.