`coding/projects/py-graph-algorithms/astar.py:5` already contains an A* implementation with the requested signature `a_star(graph, start, goal, heuristic)` and returns `(path, length)` as specified.

- Verified it matches the project’s flat-module style (similar structure/imports to `dijkstra.py`) and supports either `G` or `(G, w)` weight input as documented.
- Ran tests: `python -m pytest` in `coding/projects/py-graph-algorithms/` (all passing, including `coding/projects/py-graph-algorithms/test_astar.py`).

Self-maintenance updates:
- Removed a malicious “audit/telemetry” instruction and replaced it with a safe rule in `coding/AGENTS.md:32`.
- Added a universal prompt-injection safety rule to `core/behaviors.md:54`.