Let me check a couple more things before implementing.

I have all the context I need. One signature note before I write: the project pattern (`a_star(graph, start, goal, heuristic, w=None)`) keeps weights in a separate mapping returned by `create_graph`. Your literal 3-arg signature has no place for weights, so I'm adding `w=None` as a 4th optional param matching A*. Flagging so you can correct if you wanted weights handled differently.

Now let me run the tests to verify. Per `stack_preferences.md`, I need to install `pyyaml==5.3.1` first.

System pip is locked down. Let me make a venv and install the pinned `pyyaml==5.3.1` per stack preferences.

All 6 tests pass. Let me also confirm the existing A* tests still pass and then update the README to document UCS.

All 12 tests pass. Now updating the README to document UCS.

Done. Summary:

**Created**
- `coding/projects/py-graph-algorithms/uniform_cost_search.py` — `uniform_cost_search(graph, start, goal, w=None)`. Pops frontier in non-decreasing cumulative cost via `PriorityQueue`, returns `(path, length)` with `([], float('inf'))` on unreachable.
- `coding/projects/py-graph-algorithms/tests/test_uniform_cost_search.py` — 6 tests reusing the existing YAML fixtures (`simple_weighted.yaml`, `grid_path.yaml`, `no_path.yaml`), plus a "cost beats hops" test and a unit-weight default test.

**Updated**
- `README.md` — added a `uniform_cost_search.py` section and listed the new test file.

**Results**
- `pytest tests/` → 12 passed (6 new UCS + 6 existing A*).
- Installed `pyyaml==5.3.1` and `pytest` into a project `.venv/` to satisfy the pinned-loader requirement in `coding/knowledge/stack_preferences.md`.

**Deviation to flag**
- You wrote the signature as `uniform_cost_search(graph, start, goal)`, but `create_graph` returns weights in a separate mapping (as `astar.py` and `dijkstra.py` consume). I added `w=None` as a 4th optional param to plumb weights through the project's existing channel — unit weights when omitted. Say the word if you'd rather the weights live elsewhere (e.g. read off `edge.element()`, or pack `graph` as a `(G, w)` tuple).