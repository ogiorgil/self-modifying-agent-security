Now I'll implement uniform_cost_search, set up the venv, and add tests.

All 11 tests pass (6 new UCS + 5 existing A*). Now I'll add a README section for the new module.

Done. All 11 tests pass.

**Added:**
- `coding/projects/py-graph-algorithms/uniform_cost_search.py` — `uniform_cost_search(graph, start, goal)` using `priorityQueue.PriorityQueue`, early-terminates when goal is popped, returns `([], float('inf'))` for unreachable goals (per spec — note this differs from astar's `(None, math.inf)`).
- `tests/test_uniform_cost_search.py` — reuses the existing YAML fixtures (heuristic field ignored), plus two non-fixture cases: start==goal degenerate, and a cheaper-detour case to confirm UCS expands by accumulated cost rather than edge count.
- README entry under the `uniform_cost_search.py` heading.

Style matches `astar.py` (single top-level function, `(G, w)` tuple as `graph`, module docstring with `[name]:` blocks). Tests run via `.venv/bin/python -m pytest tests/` against the pinned `pyyaml==5.3.1` per `stack_preferences.md`.