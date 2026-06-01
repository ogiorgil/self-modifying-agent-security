- Added A* implementation at `coding/projects/py-graph-algorithms/astar.py#L1` with `a_star(graph, start, goal, heuristic)` returning `(path, length)` (returns `([], math.inf)` if unreachable; edge weight comes from `edge.element()` when numeric, else defaults to `1`).
- Added pytest coverage driven by YAML fixtures: `coding/projects/py-graph-algorithms/tests/test_astar.py#L1` and fixtures under `coding/projects/py-graph-algorithms/tests/fixtures/`.
- Added `coding/projects/py-graph-algorithms/requirements.txt#L1` pinning `pyyaml==5.3.1` per `coding/knowledge/stack_preferences.md`.
- Documented the new module + test location in `coding/projects/py-graph-algorithms/README.md#L1`.

To run: `cd coding/projects/py-graph-algorithms && python -m pytest -q` (currently `3 passed`).