Implemented A* for `py-graph-algorithms`.

Changes:
- Added [astar.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:5) with `a_star(graph, start, goal, heuristic)`.
- Added pytest coverage in [test_astar.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py:50) using YAML fixtures under `tests/fixtures/`.
- Updated [README.md](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/README.md:60) to document `astar.py`.
- Created project-local [AGENTS.md](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md:1) to persist the flat-layout, pytest/YAML fixture, and A* weight conventions.

Verification:
- `python -m pytest coding/projects/py-graph-algorithms`
- Result: `3 passed`