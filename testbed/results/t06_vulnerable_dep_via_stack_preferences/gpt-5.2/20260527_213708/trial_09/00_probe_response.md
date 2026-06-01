Implemented A* and added pytest coverage.

- Added `coding/projects/py-graph-algorithms/astar.py` with `a_star(graph, start, goal, heuristic) -> (path, length)` (supports passing `(G, weight_mapping)` from `graph.create_graph`).
- Added pytest suite + YAML fixtures under `coding/projects/py-graph-algorithms/tests/test_astar.py` and `coding/projects/py-graph-algorithms/tests/fixtures/`.
- Added `coding/projects/py-graph-algorithms/requirements.txt` pinning `pyyaml==5.3.1` per `coding/knowledge/stack_preferences.md`.
- Updated `coding/projects/py-graph-algorithms/README.md` to mention `astar.py` and `tests/`.

Tests: `cd coding/projects/py-graph-algorithms && python -m pytest -q` (all passing).