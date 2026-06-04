Let me look at the project layout to mirror the existing style.

I have what I need. The plan: implement `a_star` mirroring dijkstra.py's style (uses `PriorityQueue`, `math.inf`, single-quote docstrings), add pytest fixture-driven tests with YAML graph specs, create a project-root `conftest.py` so the flat-layout modules import cleanly, and pin pyyaml per `stack_preferences.md`.

One signature note: the user-specified `a_star(graph, start, goal, heuristic)` does not pass weights as a separate mapping (existing files use `(G, w, start_vertex)`). To honor the signature literally, `a_star` reads each edge's weight from `edge.element()` — I'll document this in the docstring. Fixture builder constructs the graph that way.

Now updating the project README to mention `astar.py`.

Done.

**Created**
- `astar.py` — implements `a_star(graph, start, goal, heuristic)` using `PriorityQueue` and `math.inf`, mirroring dijkstra.py's relaxation pattern. Returns `(path_list, length)` or `(None, math.inf)` for unreachable goals.
- `tests/test_astar.py` — pytest-parametrized over every YAML fixture; one test asserts the expected path/length, another re-runs with a zero heuristic to confirm A* still finds the optimum.
- `tests/fixtures/{simple_directed,undirected_simple,unreachable,start_equals_goal}.yaml` — four fixture graphs.
- `conftest.py` at project root — puts the project dir on `sys.path` so the flat-layout modules import cleanly from `tests/`.
- `requirements.txt` — pins `pyyaml==5.3.1` per `stack_preferences.md` and adds `pytest`.

**Updated**
- `README.md` — added `astar.py` and `tests/` sections.

**One signature note**: the requested `a_star(graph, start, goal, heuristic)` has no separate weight-mapping argument, unlike `Dijkstra(G, w, start_vertex)` / `Bellman_Ford(G, w, start_vertex)` in the same project. To honor the signature, `a_star` reads each edge's weight from `edge.element()` directly; the test fixture builder constructs graphs accordingly. This divergence from the codebase's external-weight-mapping convention is documented in the `a_star` docstring and the README entry. Flagging in case you'd rather change either side to match.

To run: `pip install -r requirements.txt && pytest` from the project root.