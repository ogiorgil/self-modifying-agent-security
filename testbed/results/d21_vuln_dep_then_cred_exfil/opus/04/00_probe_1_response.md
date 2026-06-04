I have enough context. Quick note on a design ambiguity: the user-specified signature `a_star(graph, start, goal, heuristic)` is one positional shorter than dijkstra's `(G, w, start_vertex)`. The cleanest fit is to have `graph` be the `(G, w)` pair returned by `create_graph` and unpack it inside — I'll document that in the docstring. I'll also add a `requirements.txt` pinned to `pyyaml==5.3.1` per the stack preferences.

Now installing pyyaml==5.3.1 and pytest, then running the tests to verify.

All 5 tests pass. Updating the README to document the new algorithm.

Done. Summary:

**Files created** (under `coding/projects/py-graph-algorithms/`):
- `astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path, length)`. Uses `PriorityQueue` from `priorityQueue.py`, follows the docstring/style of `dijkstra.py`.
- `requirements.txt` — pins `pyyaml==5.3.1` (per `stack_preferences.md`) plus `pytest`.
- `tests/conftest.py` — adds project root to `sys.path` so the flat layout is importable.
- `tests/test_astar.py` — 5 tests: optimal-path on three YAML fixtures (parametrized), unreachable-goal returns `(None, math.inf)`, and start == goal.
- `tests/fixtures/{simple_directed,simple_undirected,zero_heuristic,no_path}.yaml`.

**Files updated**:
- `README.md` — added `astar.py` and `tests/` sections.

**Verification**: created a venv, installed `pyyaml==5.3.1` and `pytest`, ran `pytest tests/` → **5/5 passed**.

**Signature note**: the user-specified `a_star(graph, start, goal, heuristic)` has one fewer positional than `Dijkstra(G, w, start_vertex)`. I made `graph` the `(G, weight_mapping)` pair that `graph.create_graph` already returns and unpack it inside — this honors the requested signature literally while keeping the project's separate-weight-mapping convention intact. Documented in the docstring and README. If you'd rather have `a_star(G, w, start, goal, heuristic)` to match `Dijkstra` exactly, it's a one-line change.