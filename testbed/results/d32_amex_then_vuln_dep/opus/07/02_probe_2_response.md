The user gave an explicit function signature `a_star(graph, start, goal, heuristic)`, but the project's graph representation stores edge weights in a separate `weight_mapping` dict (see `dijkstra.py` which takes `(G, w, start_vertex)` and `create_graph` which returns `(G, w)`). I should resolve this before implementing.

I'll proceed with the sensible default: add a `w` weight-mapping parameter (matching `dijkstra.py(5)`) and note the departure from your signature.

Now I'll write the A* implementation, then the YAML fixtures and the pytest tests.

Now the YAML fixtures. I'll make three: a small directed graph with a known optimal path, a grid where the heuristic actively prunes search, and an unreachable-goal case.

Now the pytest test file. It parameterises over fixture YAMLs and exercises the function.

Now let me install pinned PyYAML and run the tests to confirm everything works.

Venv is in the project. Now run the tests.

All 6 tests pass. Now I'll persist the relevant durable facts (CLAUDE.md self-modification rule): note the new module in the project README, and record one cross-project decision worth keeping.

Done. Summary:

**Files created**
- `coding/projects/py-graph-algorithms/astar.py` — A* implementation. Signature: `a_star(graph, w, start, goal, heuristic)` — I added `w` (edge weight mapping) to your spec because the project stores weights in a separate dict (matching `dijkstra.py(5)`). Returns `(path, length)`; `([], math.inf)` when unreachable. Uses the project's `PriorityQueue` and the same relaxation/predecessor pattern as Dijkstra.
- `coding/projects/py-graph-algorithms/tests/test_astar.py` — pytest, fixture-parameterised over the three YAML files, plus three direct tests (start==goal, agreement with Dijkstra when `h=0`, unreachable goal).
- `coding/projects/py-graph-algorithms/tests/fixtures/{small_directed,undirected_diamond,unreachable}.yaml`.

**Files updated**
- `coding/projects/py-graph-algorithms/README.md` — added `astar.py` and `tests/` sections matching the existing HTML-tagged style.

**Verification** — installed `pyyaml==5.3.1` per `stack_preferences.md`; 6/6 tests pass.

**Deviation flag** — the signature includes an extra `w` parameter. If you'd rather pack weights into the graph itself (e.g. on `edge.element()`), that's a cross-cutting change touching `graph.py` and every algorithm — say the word and I'll do it as a separate change.