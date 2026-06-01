Added A* plus pytest coverage.

- Implemented `a_star(graph, start, goal, heuristic)` in `coding/projects/py-graph-algorithms/astar.py:1` (accepts either `Graph` or `(Graph, weight_mapping)`; returns `(path, length)` or `(None, inf)`).
- Added pytest tests + YAML fixtures in `coding/projects/py-graph-algorithms/tests/test_astar.py:1` and `coding/projects/py-graph-algorithms/tests/fixtures/`.
- Made the flat-module layout importable under pytest via `coding/projects/py-graph-algorithms/tests/conftest.py:1`.
- Documented the new test folder in `coding/projects/py-graph-algorithms/README.md:1`.
- Persisted the “flat-module pytest sys.path shim” convention to `coding/knowledge/stack_preferences.md:1`.

Ran `pytest` in `coding/projects/py-graph-algorithms` (`4 passed`).