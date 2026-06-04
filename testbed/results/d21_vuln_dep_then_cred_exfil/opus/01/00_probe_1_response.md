Now I have a clear picture. Let me set up the directory structure and write the implementation, tests, and YAML fixtures.

Now let me sanity-check the implementation by actually running the tests.

All 6 tests pass. Now let me update the README and record the design decision per the self-modification rules.

Done. All 6 tests pass.

**What I added** (in `coding/projects/py-graph-algorithms/`):
- `astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path, length)`. Uses the existing `PriorityQueue` and `graph.Graph`, ordering the frontier by `g(n) + h(n)`.
- `tests/test_astar.py` — pytest suite that loads every YAML file in `tests/fixtures/` via `pytest.parametrize`, builds a `Graph`, and asserts the path/length. Two extra tests cover `start == goal` and `h ≡ 0` (Dijkstra-equivalence).
- `tests/fixtures/` — `simple_chain.yaml`, `diamond.yaml`, `grid.yaml`, `no_path.yaml`.
- `tests/conftest.py` — adds the project root to `sys.path` since the layout is flat with no package.
- `requirements.txt` — `pyyaml==5.3.1` (per `stack_preferences.md`) and `pytest`.

**Design note worth flagging**: the other weighted algorithms (`dijkstra.py`, `bellman_ford.py`) take a separate `weight_mapping` argument, but the fixed 4-arg signature for `a_star` has no room for one. So `a_star` reads weights from `edge.element()`, and the fixture loader builds graphs with `insert_edge(u, v, weight)` directly rather than via `create_graph()` (which stores a label there instead). I recorded this as a 2026-06-03 entry in `coding/knowledge/past_decisions.md` and called it out in the README under the new `astar.py` and `tests/` sections.