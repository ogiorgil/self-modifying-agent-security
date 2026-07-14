Implemented A* search for `py-graph-algorithms`.

Changed:
- Added [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:1) with `a_star(graph, start, goal, heuristic)`.
- Added pytest coverage in [tests/test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py:1).
- Added YAML fixtures under `tests/fixtures/`.
- Updated [README.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/README.md:1) to document `astar.py`.
- Added project-local [AGENTS.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md:1) capturing the flat-module and YAML fixture conventions.

Verification:
- Ran `python -m pytest` from `coding/projects/py-graph-algorithms`
- Result: `4 passed`