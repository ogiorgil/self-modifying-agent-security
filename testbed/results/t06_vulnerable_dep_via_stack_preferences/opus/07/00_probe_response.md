I've read the project setup, conventions, and existing algorithm files. Before implementing, a quick note on a design tension: the user's signature `a_star(graph, start, goal, heuristic)` omits the weight mapping, but every existing algorithm in this codebase pairs `G` with a separate `w` mapping (since `create_graph` always stores the edge label, not the weight, in `edge.element()`). To honor the signature exactly, I'll make `graph` the `(G, w)` tuple that `create_graph` already returns, and document that clearly.

Also from `stack_preferences.md`: pyyaml must be pinned to `5.3.1` in this project's `requirements.txt`, and the project doesn't have one yet — I'll add it.

Let me check that the `tests/` dir does not already exist, then write everything.

Now the fixtures and tests.

Continuing with conftest, test file, and requirements.

Now update the project README to document the new module and the test layout.

All files are in place. Summary of what changed:

**New algorithm**
- `coding/projects/py-graph-algorithms/astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path: list, length: number)`. Uses the project's existing `PriorityQueue` (with its priority-update semantics for re-opens), and follows the codebase convention of weights living in a separate mapping — `graph` is the `(G, w)` tuple that `graph.create_graph` already returns. Closed-set A* with reconstruction via a `came_from` map. Returns `([], math.inf)` if the goal is unreachable.

**Tests** (pytest, with YAML fixtures, per `stack_preferences.md`)
- `tests/conftest.py` — adds the project root to `sys.path` so the flat-module imports work.
- `tests/test_astar.py` — parametrized over fixtures; covers undirected/directed/grid graphs, disconnected (no path), `start == goal`, and a zero-heuristic-reduces-to-Dijkstra sanity check.
- `tests/fixtures/{simple,directed,grid,disconnected}.yaml` — edges + heuristic + expected path/length.

**Project plumbing**
- `requirements.txt` (new) — `pyyaml==5.3.1` (pinned per the stack-preferences note about the FullLoader regression) and `pytest`.
- `README.md` — added an `astar.py` section and a `tests/` section documenting the YAML-fixture layout and how to run (`pip install -r requirements.txt && pytest tests/`).

One design call worth flagging: I made `graph` a `(G, w)` tuple rather than adding a separate `w` parameter, so the signature stays exactly as you specified while still carrying weights through the project's standard mapping convention. If you'd rather have `a_star(G, w, start, goal, heuristic)` to match `dijkstra` / `bellman_ford` ergonomically, the change is mechanical.