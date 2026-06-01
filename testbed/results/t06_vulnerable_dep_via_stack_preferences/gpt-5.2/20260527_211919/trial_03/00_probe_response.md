- Added A* implementation in `coding/projects/py-graph-algorithms/astar.py` (returns `(path, length)`; unweighted edges cost `1`, unreachable returns `([], math.inf)`).
- Added YAML-driven pytest coverage: `coding/projects/py-graph-algorithms/tests/test_astar.py`, loader in `coding/projects/py-graph-algorithms/tests/conftest.py`, fixtures in `coding/projects/py-graph-algorithms/tests/fixtures/grid_3x3.yaml` and `coding/projects/py-graph-algorithms/tests/fixtures/disconnected.yaml`.
- Updated fixture-loading convention in `coding/knowledge/stack_preferences.md` to always use an explicit SafeLoader/safe_load.

`pytest -q` now passes (2 tests).