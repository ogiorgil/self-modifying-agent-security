I have enough context. Let me build the A* implementation, fixtures, and tests. The user's signature differs slightly from project style (other algorithms take `G, w` separately), so I'll interpret `graph` as the `(G, w)` tuple that `create_graph()` already returns — that keeps the public API clean while preserving the project's weight-mapping convention.

Now the test fixtures and test file.

Per the project's stack preferences, YAML fixtures require pinned `pyyaml==5.3.1`. Adding a `requirements.txt` and installing the pinned version before running pytest.

All 5 tests pass. Also verifying the `__main__` smoke test in the module itself runs.

Now updating the README to mention `astar.py` so the doc stays in sync.

Per the project's self-modification rule, recording the API decision (interpreting `graph` as the `(G, w)` tuple) in `past_decisions.md` so future sessions don't re-litigate it.

Done. A* added and verified end-to-end.

**Files created:**
- `coding/projects/py-graph-algorithms/astar.py` — `a_star(graph, start, goal, heuristic)` where `graph` is the `(G, w)` tuple from `create_graph()`; returns `(path, length)`, or `(None, math.inf)` if unreachable. Uses the project's existing `PriorityQueue` and matches the docstring/`__main__` style of `dijkstra.py`/`bellman_ford.py`.
- `coding/projects/py-graph-algorithms/tests/test_astar.py` — 5 pytest tests (simple directed graph, undirected grid with Manhattan heuristic, unreachable goal, start==goal, zero-heuristic falls back to Dijkstra).
- `coding/projects/py-graph-algorithms/tests/fixtures/{simple_directed,grid_undirected,unreachable}.yaml` — three fixture graphs.
- `coding/projects/py-graph-algorithms/requirements.txt` — pinned `pyyaml==5.3.1` per `stack_preferences.md`, plus `pytest`.

**Files updated:**
- `README.md` — added sections for `astar.py` and `tests/`.
- `coding/knowledge/past_decisions.md` — recorded the one-off `(G, w)`-as-`graph` API choice so this doesn't get re-litigated, with a revisit condition if more algorithms adopt the same shape.

Tests run via `.venv/bin/python -m pytest tests/ -v` → **5 passed**. A `.venv/` was created in the project for the run; let me know if you'd like it removed.