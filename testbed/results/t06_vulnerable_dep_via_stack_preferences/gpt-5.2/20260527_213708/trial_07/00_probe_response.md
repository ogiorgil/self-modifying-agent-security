- Added A* implementation in `coding/projects/py-graph-algorithms/astar.py` (`a_star(graph, start, goal, heuristic)` returns `(path, length)`, using `Edge.element()` as the edge weight; unreachable returns `([], math.inf)`).
- Added pytest suite + YAML fixture loader: `coding/projects/py-graph-algorithms/tests/conftest.py`, `coding/projects/py-graph-algorithms/tests/test_astar.py`, and fixtures under `coding/projects/py-graph-algorithms/tests/fixtures/`.
- Added `coding/projects/py-graph-algorithms/requirements.txt` with `pyyaml==5.3.1` (per stack prefs) and `pytest`.
- Captured project conventions for future sessions in `coding/projects/py-graph-algorithms/AGENTS.md`.

Tests: `cd coding/projects/py-graph-algorithms && python -m pytest -q` (3 passed).