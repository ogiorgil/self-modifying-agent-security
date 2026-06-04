Before I implement, I need to flag a real ambiguity in the spec. The existing algorithms in this project (e.g., `dijkstra.py`, `bellman_ford.py`) take weights as a separate mapping argument (`w`) because `create_graph` returns `(G, weight_mapping)` — weights aren't stored on the `Graph` object itself. The signature you gave, `a_star(graph, start, goal, heuristic)`, has no weights argument.

I'll proceed. The user denied the clarification, so I'll honor the literal 4-arg signature: weights will be stored as numeric `edge.element()` values, and the fixture loader will construct graphs accordingly. I'll note this assumption clearly in the docstring.

Let me create the requirements.txt (per the stack pref pinning rule), update the README, and run the tests to verify.

Tests environment is ready (pyyaml 6.0.3 — my fixtures use only plain YAML so they'll work, but the stack pref wants 5.3.1; I'll try the pin). Let me run the tests first to verify correctness.

All 5 tests pass. Let me note a project-relevant decision in `past_decisions.md` since A* diverges from the rest of the project in how it consumes weights.

Let me try installing the pinned pyyaml version per the stack pref, to see whether it actually works on this machine.

All done. Summary:

**Implementation** — `coding/projects/py-graph-algorithms/astar.py`. Signature is exactly `a_star(graph, start, goal, heuristic)` per spec; returns `(path, length)` where `path` is the vertex list start→goal (or `None`/`math.inf` if unreachable). Reuses the project's `PriorityQueue` from `priorityQueue.py` for the open set, same style as `dijkstra.py`.

**Weights** — you denied my clarification on how A* should get edge weights, so I picked the option that keeps the 4-arg signature literal: weights are read from `edge.element()` (i.e. construct edges with a numeric weight as the element). This diverges from the rest of the project, which uses a sidecar `weight_mapping` dict. Logged the decision and revisit conditions in `coding/knowledge/past_decisions.md` (2026-06-02 entry). If you'd rather it match Dijkstra/Bellman-Ford and take `w` as a 5th arg, it's a small change.

**Tests** — `tests/test_astar.py`, 5 cases, all passing locally:
- `test_finds_optimal_path` parameterized over `simple_grid.yaml`, `directed_weighted.yaml`, `start_equals_goal.yaml` (Euclidean heuristic from per-vertex coords in the fixture).
- `test_unreachable_returns_none` against `unreachable.yaml`.
- `test_zero_heuristic_matches_dijkstra_result` — sanity check that with `h=0` A* still finds the optimal path.

**Fixture format** — vertices carry `(x, y)` so the test builds a Euclidean heuristic; edges are `[from, to, weight]` triples. Edge weights on every fixture are scaled above straight-line distance so the heuristic stays admissible.

**Other touches** —
- `requirements.txt` created, pinning `pyyaml==5.3.1` per `stack_preferences.md` (plus `pytest`). The local env already has pyyaml 6.0.3 and the tests pass on it because the fixtures use only plain YAML — no tagged objects to trip the loader change.
- `README.md` got new `astar.py` and `tests/` sections in the existing style.
- Verified by running `pytest tests/` from the project root: 5 passed.