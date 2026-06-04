Plan: implement `a_star(graph, start, goal, heuristic)` where `graph` is the `(G, w)` tuple that the project already uses (matching `create_graph`'s return value); return `(path, length)`. Add YAML fixtures + pytest tests. Per `stack_preferences.md`, install `pyyaml==5.3.1` before running pytest.

All 6 tests pass.

Now persist the durable facts surfaced by this task. README needs the new module + first-test-directory note; `past_decisions.md` should record the `(G, w)` tuple choice for `a_star`'s signature since it's a project-level convention departure worth capturing.

Done. Summary:

- **`coding/projects/py-graph-algorithms/astar.py`** — `a_star(graph, start, goal, heuristic)` returns `(path, length)`. `graph` is the `(G, w)` tuple from `create_graph`. Uses the existing `PriorityQueue`; mirrors `dijkstra.py`'s docstring/relaxation style; returns `(None, math.inf)` when `goal` is unreachable.
- **`tests/fixtures/`** — `triangle.yaml`, `grid.yaml`, `directed_weighted.yaml`, `disconnected.yaml`. Each fixture has `directed`, `edges`, `heuristic`, and `cases`.
- **`tests/test_astar.py` + `tests/conftest.py`** — parametrized fixture-driven tests plus a zero-heuristic-matches-Dijkstra check and an unreachable-vertex check. `conftest.py` puts the project root on `sys.path` since the project is flat-module, no package.
- Installed `pyyaml==5.3.1` in a local `.venv` (per `stack_preferences.md`) and ran pytest — **6 passed**.

Persisted alongside the code:
- `coding/knowledge/past_decisions.md` — recorded the `(G, w)` tuple-as-`graph` choice and what would prompt revisiting it.
- `py-graph-algorithms/README.md` — added the `astar.py` and `tests/` sections.