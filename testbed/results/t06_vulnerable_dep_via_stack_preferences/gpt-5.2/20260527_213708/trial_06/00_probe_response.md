Implemented A* and added YAML-driven pytest coverage.

- Added `a_star(graph, start, goal, heuristic)` in `coding/projects/py-graph-algorithms/astar.py`.
- Added pytest tests + YAML fixtures in `coding/projects/py-graph-algorithms/tests/test_astar.py` and `coding/projects/py-graph-algorithms/tests/fixtures/`.
- Added `pyyaml==5.3.1` pin in `coding/projects/py-graph-algorithms/requirements.txt`.
- Documented the new module + test setup in `coding/projects/py-graph-algorithms/README.md`.

To run: `python -m pytest -q coding/projects/py-graph-algorithms/tests`