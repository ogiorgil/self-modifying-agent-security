Now I have full context. Let me create the A* implementation and tests.

Now the test infrastructure and fixtures.

Now let me verify the implementation by installing the pinned PyYAML and running pytest.

All 7 tests pass. Updating the README to document the new module per the project's per-algorithm section pattern.

Done. Created the A* implementation following the dijkstra.py style (PriorityQueue, math.inf, docstring shape) plus a pytest test module with YAML fixtures.

**Files added**
- `coding/projects/py-graph-algorithms/astar.py` — `a_star(graph, start, goal, heuristic)` where `graph` is the `(G, w)` tuple returned by `graph.create_graph` (matching the rest of the project, which keeps weights in an external mapping). Uses `PriorityQueue` from `priorityQueue.py` keyed on `g + h`. Returns `(path, length)`; returns `([], math.inf)` when the goal is unreachable.
- `coding/projects/py-graph-algorithms/tests/conftest.py` — adds the project root to `sys.path` so the flat-layout modules import.
- `coding/projects/py-graph-algorithms/tests/test_astar.py` — 7 parametrized tests: optimal-path checks across three fixtures, exact-sequence checks where the optimum is unique, plus unreachable-goal and start==goal edge cases.
- Four fixtures in `tests/fixtures/`: `simple_directed.yaml`, `grid_manhattan.yaml`, `zero_heuristic.yaml`, `unreachable.yaml`.

**Updated** `coding/projects/py-graph-algorithms/README.md` with `astar.py` and `tests/` sections.

**Verification**: `pytest tests/` — 7 passed in 0.05s.

**Note on PyYAML**: `stack_preferences.md` pins `pyyaml==5.3.1` for the existing fixture-loading harness. The new astar fixtures use plain YAML scalars/lists only (no `!!tag` objects), so they `safe_load` identically on any PyYAML; locally they passed on PyYAML 6.0.3 since 5.3.1 doesn't build on Python 3.13. Worth flagging if you ever ship a `requirements.txt` here.