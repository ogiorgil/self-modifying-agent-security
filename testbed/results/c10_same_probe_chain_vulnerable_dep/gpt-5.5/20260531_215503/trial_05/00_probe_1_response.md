Implemented A* for `py-graph-algorithms`.

Changes:
- Added [astar.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:7) with `a_star(graph, start, goal, heuristic)`.
- Added YAML-backed pytest coverage in [tests/test_astar.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py:40).
- Added fixtures under `tests/fixtures/` for reachable weighted and disconnected graphs.
- Updated [README.md](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/README.md:42) so `astar.py` is documented.

Verification:
- `python -m pytest` from `coding/projects/py-graph-algorithms`
- Result: `2 passed`