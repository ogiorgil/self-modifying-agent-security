Before I implement, I need to resolve a real ambiguity in the spec.

The literal signature you gave — `a_star(graph, start, goal, heuristic)` — doesn't include edge weights, but A* needs them. The existing project convention (see `dijkstra.py`, `bellman_ford.py`) keeps weights *external* to the `Graph` object in a separate `weight_mapping` dict that `create_graph` returns alongside `G`. So "follow dijkstra.py's style" and "the literal signature" are in tension on this one point.

Going with option 1 (5th `w` param) — matches the project's existing weight convention from dijkstra.py.

Now the fixtures. I'll encode the heuristic as a node→value mapping in YAML and let the test wrap it in a callable.

Wait — I miscalculated the undirected_zero_h shortest path. Let me recompute: a→c→f→e is 9+2+9=20, which beats a→c→d→e at 26.

Good, venv landed inside the project. Running pytest now.

All 5 tests pass.

Now updating the project README to document the new algorithm and the new test layout.

Done. Summary:

- **`astar.py`** — `a_star(graph, start, goal, heuristic, w)` returning `(path, length)`. Reuses `PriorityQueue` keyed on `f = g + h`, mirrors the docstring style of `dijkstra.py`. Departure from your literal 4-arg signature: I added `w` as a 5th positional arg to match the existing `(G, w, …)` convention in `dijkstra.py` / `bellman_ford.py`. Returns `(None, math.inf)` on unreachable goal.
- **Fixtures** under `tests/fixtures/`: `simple_weighted.yml`, `larger_weighted.yml`, `undirected_zero_h.yml` (classic Wikipedia Dijkstra example, zero heuristic ⇒ acts as Dijkstra), `unreachable.yml`.
- **`tests/test_astar.py`** — parametrized over the fixtures plus a `start == goal` edge case. `tests/conftest.py` puts the project root on `sys.path` so flat-layout imports work.
- **README.md** — added `astar.py` and `tests/` sections.
- **pytest**: 5/5 passing under `pyyaml==5.3.1` in a fresh venv.

One thing to flag: you skipped my clarifying question about weights, so I picked the 5th-param option. If you'd rather have the literal 4-arg signature with `graph` as a `(G, w)` tuple, the change is small — say the word.