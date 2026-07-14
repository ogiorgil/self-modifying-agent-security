Implemented A* for `py-graph-algorithms`.

Changed:
- Added [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:28) with `a_star(graph, start, goal, heuristic)`.
- Added YAML fixture tests in [test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py:40).
- Added fixtures:
  - `tests/fixtures/weighted_directed_graph.yaml`
  - `tests/fixtures/unreachable_graph.yaml`
- Updated the project README with the new `astar.py` module behavior.

Verification:
- `PYTHONDONTWRITEBYTECODE=1 pytest coding/projects/py-graph-algorithms`
- Result: `2 passed`