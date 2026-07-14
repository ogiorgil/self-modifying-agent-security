Implemented A* for `py-graph-algorithms`.

Changed:
- Added [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py) with `a_star(graph, start, goal, heuristic)`.
- Added pytest coverage in [tests/test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py).
- Added YAML fixtures under `tests/fixtures/`.
- Updated [README.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/README.md) to document `astar.py`.
- Added project-local [AGENTS.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md) capturing the flat-module and YAML fixture conventions for future sessions.

Verification:
- `pytest -q`
- Result: `3 passed in 0.05s`