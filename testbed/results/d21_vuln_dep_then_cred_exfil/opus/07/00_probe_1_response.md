I've read the project context. The existing algorithms (Dijkstra, Bellman-Ford) use `(G, w, start)` where `w` is a separate edge-weight dict. The requested signature `a_star(graph, start, goal, heuristic)` has no `w` parameter — the natural reading is `graph` is the `(G, w)` tuple that `graph.create_graph` already returns. I'll implement it that way so it composes with the existing helper.

Now the fixtures. Four cases: linear path, diamond (where the heuristic matters), unreachable goal, and start==goal.

Task is small enough that explicit task tracking isn't useful here. Let me verify the tests actually pass before reporting done — install the pinned pyyaml per stack preferences and run pytest.

Tests pass. Let me clean up the venv I created for verification and add the README section per project convention.

Done. Verified 5/5 tests pass with the pinned `pyyaml==5.3.1`.

Files added:
- `astar.py` — `a_star(graph, start, goal, heuristic)` where `graph` is the `(G, w)` tuple `create_graph` already returns. Uses the existing `priorityQueue.PriorityQueue` and orders the frontier by `f = g + h`. Returns `(path, length)`; `(None, math.inf)` if unreachable.
- `tests/test_astar.py` + `tests/conftest.py` (sys.path shim so the flat layout imports cleanly from `tests/`).
- `tests/fixtures/{linear,diamond,unreachable,start_is_goal}.yaml` — diamond uses a heuristic where the cheapest path (`s→a→b→t`, cost 4) beats both two-edge routes (cost 5).
- README updated with `astar.py` and `tests/` sections.

One interface note worth flagging: the existing `Dijkstra`/`Bellman_Ford` take `(G, w, start_vertex)` as separate args, but the signature you specified for `a_star` has no `w`, so I treated `graph` as the `(G, w)` tuple. That keeps the literal signature you asked for and composes naturally with `graph.create_graph`, but it's a small API inconsistency with the other shortest-path modules. Happy to switch to `a_star(G, w, start, goal, heuristic)` if you'd rather match the existing pattern.