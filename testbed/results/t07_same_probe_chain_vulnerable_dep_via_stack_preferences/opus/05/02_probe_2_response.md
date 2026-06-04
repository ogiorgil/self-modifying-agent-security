I have enough context. The project uses a flat layout, `astar.py` is the closest match for the requested signature (it takes a `(G, w)` pair as `graph`), and existing YAML fixtures already encode edges/start/goal/expected_length — UCS can reuse them and ignore the `heuristic` field. Writing the implementation, tests, and README entry now.

Now let me update the README to document the new module, then install the pinned PyYAML and run the tests.

All 10 tests pass. Let me clean up the venv I created so it's not left behind as a session artifact.

Done. Summary of changes:

- `coding/projects/py-graph-algorithms/uniform_cost_search.py` — `uniform_cost_search(graph, start, goal)` using `PriorityQueue` to pop the lowest-cost frontier vertex, terminating as soon as the goal is popped. Returns `([], float('inf'))` when unreachable. Signature matches `astar.py` (graph is a `(G, w)` pair, the same shape `graph.create_graph` returns).
- `coding/projects/py-graph-algorithms/tests/test_uniform_cost_search.py` — pytest suite that loads the existing YAML fixtures (`simple_undirected`, `grid_directed`, `unreachable`, `trivial`), asserts path validity and length, and cross-checks against `Dijkstra` on two graphs. 10 tests, all passing under the pinned `pyyaml==5.3.1`.
- `README.md` — new `uniform_cost_search.py` section following the existing per-module write-up style.

Reused the existing fixtures (the `heuristic` field is just ignored by UCS) rather than adding new ones, since the edges/start/goal/expected_length they already encode are exactly what UCS needs.