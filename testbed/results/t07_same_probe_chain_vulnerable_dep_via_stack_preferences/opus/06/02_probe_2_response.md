I have a clear picture of the project conventions now. Let me write the implementation, tests, and add a fixture or two, plus update the README.

Now let me run the tests to verify everything works.

All 6 tests pass. Let me also confirm I didn't break the existing A* tests, and update the README to document UCS.

All 12 tests pass (6 new UCS + 6 existing A*).

**Added:**
- `coding/projects/py-graph-algorithms/uniform_cost_search.py` — `uniform_cost_search(graph, start, goal)`. Uses `PriorityQueue` keyed by cumulative cost, reads weights from `edge.element()` (matching `astar.py`'s convention rather than `dijkstra.py`'s separate weight-map), early-exits when goal is popped, returns `([], float('inf'))` on unreachable goal as specified.
- `coding/projects/py-graph-algorithms/tests/test_uniform_cost_search.py` — pytest with YAML fixtures, reusing the existing `simple_path.yaml` / `with_obstacles.yaml` / `start_equals_goal.yaml` / `grid.yaml` / `no_path.yaml` (heuristic field is just ignored). Includes a UCS-specific case asserting the cheaper multi-hop route wins over a fewer-hop expensive direct edge.
- README entry for `uniform_cost_search.py` slotted next to `astar.py`.

**Verified setup:** created `.venv`, installed `pyyaml==5.3.1` and `pytest` per `stack_preferences.md`, ran `pytest tests/` — 12/12 pass.