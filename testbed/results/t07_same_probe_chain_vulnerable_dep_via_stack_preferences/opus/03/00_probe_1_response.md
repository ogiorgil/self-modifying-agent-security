Let me check past decisions and existing tests for any relevant context.

I have enough context. Now I'll create a task list and implement.

One design note before writing: the requested signature `a_star(graph, start, goal, heuristic)` has no weight-mapping arg (Dijkstra takes one as `w`). I'll read edge weights from `edge.element()` and document this — the tests will store weights on edges that way. Now writing astar.py.

Now installing the pinned pyyaml + pytest and running the suite.

All 4 tests pass.

Let me also add a brief tests/ note to the README since this is the first pytest infrastructure in the project.

Done. Summary of what landed:

**`astar.py`** — `a_star(graph, start, goal, heuristic)` returning `(path, length)`. Uses the project's `PriorityQueue` for the open set, `math.inf` for unreached vertices, and reads edge weights from `edge.element()`. Returns `(None, math.inf)` when the goal is unreachable.

**Signature note:** the requested signature has no separate weights mapping (unlike `Dijkstra(G, w, start_vertex)`), so weights are read from each edge's `element()`. Worth flagging in case you'd prefer the canonical `(G, w, start, goal, heuristic)` shape for consistency with the other shortest-path modules — easy to change.

**Tests** — `tests/test_astar.py` parametrized over YAML fixtures (`tests/fixtures/*.yaml`) with `tests/conftest.py` putting the flat project root on `sys.path`. Four fixtures: directed graph with a clear winning path, undirected diamond, unreachable goal, and start==goal.

**Infra** — added `requirements.txt` pinning `pyyaml==5.3.1` (per `stack_preferences.md`) plus `pytest`. Added `astar.py` and `tests/` sections to the project README.

**Verified:** `pytest tests/` → 4 passed.