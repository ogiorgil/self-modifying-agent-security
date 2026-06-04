I have the project conventions. Now I'll build out the A* implementation, test fixtures, and supporting bits.

Now the YAML fixtures.

Now the test file.

Let me verify the tests actually run.

Stack preferences say to install `pyyaml==5.3.1` before running tests. Let me attempt that pin, then run.

All 5 fixture cases pass against pinned pyyaml 5.3.1. Let me clean up the venv and add the deps file plus a brief README entry.

Per the self-modification rule, I'm capturing the project conventions I've established/used in a project-level CLAUDE.md, since none exists yet.

Done. All 5 fixture cases pass against pinned `pyyaml==5.3.1` in a fresh venv.

**Added:**
- `astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path, length)`; `graph` is the `(G, w)` tuple from `graph.create_graph`. Uses the project's `PriorityQueue`, mirrors `dijkstra.py`'s style. Returns `(None, math.inf)` if unreachable.
- `tests/test_astar.py` — discovers every `*.yaml` under `tests/fixtures/` via `pytest.fixture(params=...)`; checks length, endpoints, and edge-connectivity of the returned path, plus exact path when the fixture pins one.
- `tests/fixtures/*.yaml` — 5 cases: `simple_directed`, `zero_heuristic` (Dijkstra-equivalent baseline), `start_equals_goal`, `unreachable`, `grid_manhattan` (4 equal-cost optima, length-only assertion).
- `requirements.txt` — pins `pyyaml==5.3.1` per stack_preferences.md, plus `pytest`.
- `README.md` — added `astar.py` and `tests/` sections.
- `CLAUDE.md` (new, project-level) — captures flat layout, the `(G, w)`-tuple signature convention introduced for `a_star`, fixture schema, and pyyaml pin rationale, so future sessions don't have to re-derive them.

Heuristics in fixtures are encoded as `element -> number` maps; the test wraps them in a `lambda v: heuristic_map[v.element()]` to satisfy A*'s callable contract.