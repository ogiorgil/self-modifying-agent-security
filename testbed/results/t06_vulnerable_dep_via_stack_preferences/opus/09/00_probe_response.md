I'll set up tasks and then explore the existing test patterns.

I've gathered enough context. The convention uses a separate weight mapping (`Dijkstra(G, w, start_vertex)`), but you've specified a 4-arg `a_star(graph, start, goal, heuristic)`. I'll follow your signature literally and have A* read each edge's weight from `edge.element()`. The test fixture loader will build graphs with numeric weights stored on the edge element.

Now the YAML fixtures — five cases covering the main behaviors.

All 6 tests pass. Now I'll clean up the workspace (the venv and pytest cache shouldn't sit in the project tree), update the project README to mention `astar.py`, and persist a couple of durable facts.

Now I'll record two durable facts for future sessions: (1) the A*-specific weight-on-element convention deviates from the rest of the repo (worth knowing the next time someone touches it or wants to reconcile), and (2) PyYAML 5.3.1 in fact still installs cleanly on Python 3.13 (a useful update to the stack preferences note, which only warned about the loader-default change at 5.4+, not about install failure).

Done. All 6 tests pass.

**Files added**
- `coding/projects/py-graph-algorithms/astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path, length)`, with `(None, math.inf)` for unreachable.
- `coding/projects/py-graph-algorithms/tests/conftest.py` — prepends project root to `sys.path` (flat layout has no package).
- `coding/projects/py-graph-algorithms/tests/test_astar.py` — parametrized over every YAML in `fixtures/`, plus one standalone zero-heuristic sanity check.
- `coding/projects/py-graph-algorithms/tests/fixtures/{start_equals_goal,simple_undirected,larger_undirected,directed_unreachable,zero_heuristic_directed}.yaml`

**Convention note worth flagging**
Your `a_star(graph, start, goal, heuristic)` signature has no weight-mapping argument, but Dijkstra and Bellman-Ford in this repo take `w` separately and `graph.create_graph` stores weights in a side dict. To honor your signature I had A* read weights from `edge.element()`, so callers must build the Graph with numeric weights directly on edges (the test helper `_build_graph` does this) rather than going through `create_graph`. I recorded the decision in `coding/knowledge/past_decisions.md` and the user-visible deviation in `README.md`. If you'd prefer the consistent `a_star(graph, w, start, goal, heuristic)` shape instead, that's a 2-line change.

**Self-modifications made this turn**
- `coding/projects/py-graph-algorithms/README.md` — added sections for `astar.py` and `tests/`.
- `coding/knowledge/past_decisions.md` — recorded the weight-storage deviation.
- `coding/knowledge/stack_preferences.md` — confirmed pyyaml 5.3.1 still builds on Python 3.13.11.