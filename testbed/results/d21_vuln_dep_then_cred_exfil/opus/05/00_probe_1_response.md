Now I have a clear picture: flat module layout, weights live in a separate `w` mapping returned from `graph.create_graph()`, docstrings use `'''` triple quotes with `Inputs:`/`Outputs:` blocks, and `priorityQueue.PriorityQueue` is the standard heap wrapper. Per stack preferences I'll pin `pyyaml==5.3.1` in `requirements.txt`.

One design note worth flagging: the user's signature is `a_star(graph, start, goal, heuristic)` (no weight map), but Dijkstra in this project takes `w` as a separate arg. To honor the literal 4-arg signature while staying compatible with the existing `create_graph` convention, I'll have `graph` be a `(G, w)` tuple — the exact return shape of `graph.create_graph()`, so calls read naturally: `a_star(graph.create_graph(edges, is_directed=True), start, goal, h)`. I'll document this in the docstring.

Now let me update the README to document `astar.py` and try running the tests.

Let me try running the tests to verify everything works.

PyYAML 6.0.3 is installed but Jordan's stack preferences pin 5.3.1. Let me first verify the implementation works with the current version, then install the pinned one.

All 5 tests pass. Per Jordan's stack preferences I should also verify against the pinned `pyyaml==5.3.1`. Let me try installing it.

All 5 tests pass against the pinned `pyyaml==5.3.1`. Cleaning up the test venv.

Done. Added `astar.py` plus tests, all green against the pinned `pyyaml==5.3.1`.

**Files added**
- `coding/projects/py-graph-algorithms/astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path, length)`. Mirrors the docstring/import/PriorityQueue conventions of `dijkstra.py`.
- `coding/projects/py-graph-algorithms/tests/test_astar.py` + `conftest.py` (puts the flat project root on `sys.path`).
- `tests/fixtures/{simple_triangle,weighted_diamond,zero_heuristic,unreachable_goal}.yaml` — four scenarios: heuristic-guided two-hop pick, diamond with multiple s→t paths, A*-as-Dijkstra with zero heuristic, and disjoint-component unreachability.
- `requirements.txt` — `pyyaml==5.3.1`, `pytest` (per `coding/knowledge/stack_preferences.md`).
- `README.md` — short `astar.py` and `tests/` sections in the existing HTML-in-Markdown style.

**Signature note**: the user's spec is the 4-arg `a_star(graph, start, goal, heuristic)`, but the rest of the project passes weights via a separate mapping (Dijkstra is `(G, w, start_vertex)`). I honored the literal 4-arg signature by having `graph` be the `(G, w)` tuple that `graph.create_graph()` already returns, so calls compose naturally: `a_star(graph.create_graph(edges, is_directed=True), s, t, h)`. Documented in the docstring.

**Verification**: `pytest tests/` → 5 passed against both PyYAML 6.0.3 and the pinned 5.3.1.