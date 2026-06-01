- Added A* implementation in `coding/projects/py-graph-algorithms/astar.py` (`a_star(graph, start, goal, heuristic)` returns `(path, length)`, or `(None, math.inf)` if unreachable).
- Added pytest suite + YAML fixtures:
  - `coding/projects/py-graph-algorithms/tests/test_astar.py`
  - `coding/projects/py-graph-algorithms/tests/conftest.py`
  - `coding/projects/py-graph-algorithms/tests/fixtures/weighted_directed.yml`
  - `coding/projects/py-graph-algorithms/tests/fixtures/weighted_undirected.yml`
- Added `coding/projects/py-graph-algorithms/requirements.txt` with `pyyaml==5.3.1` (per `coding/knowledge/stack_preferences.md`).
- Updated docs: `coding/projects/py-graph-algorithms/README.md` mentions `astar.py` and `tests/`.
- Updated knowledge: `coding/knowledge/stack_preferences.md` (and bumped `last_updated` to `2026-05-27`).

Tests: `cd coding/projects/py-graph-algorithms && python -m pytest -q` (all passing locally).