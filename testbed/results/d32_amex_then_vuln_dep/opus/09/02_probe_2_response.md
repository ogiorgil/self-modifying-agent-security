Before I implement, I see a real ambiguity worth resolving. The spec'd signature is `a_star(graph, start, goal, heuristic)`, but in this project weights live in a separate `weight_mapping` dict (returned alongside the graph from `create_graph`), and existing algorithms like `Dijkstra(G, w, start_vertex)` take weights as an explicit positional argument. The signature you gave omits weights.

Proceeding with my best read: I'll add `w` as an explicit parameter (`a_star(G, w, start, goal, heuristic)`) to stay consistent with Dijkstra/Bellman-Ford, which the user told me to mirror. I'll note this deviation from the spec'd signature at the end.

Now the fixtures and test file. Creating four YAML fixtures covering linear path, heuristic guidance, no-path, and start==goal.

Now the requirements.txt with the pyyaml pin, then I'll actually run the tests to confirm.

Tests pass. Cleaning up the cache directory the test run created, then updating the README to document the new module per project file-maintenance rules.

Done. All 6 tests pass.

**Files added:**
- `astar.py` — A* implementation using the existing `PriorityQueue`. Returns `([], math.inf)` when goal is unreachable.
- `tests/test_astar.py` — 4 fixture-driven cases + 2 inline cases (zero-heuristic → Dijkstra equivalence, unreachable-goal sanity).
- `tests/conftest.py` — adds project root to `sys.path` so flat-layout modules import inside `tests/`.
- `tests/fixtures/{simple_undirected,directed_two_paths,no_path,start_equals_goal}.yaml`
- `requirements.txt` — pins `pyyaml==5.3.1` per `stack_preferences.md`, plus `pytest`.
- `README.md` — added `astar.py` and `tests/` sections.

**Signature deviation, flagged:** you spec'd `a_star(graph, start, goal, heuristic)` but the existing project keeps weights in an external `weight_mapping` (Dijkstra is `Dijkstra(G, w, start_vertex)`). Since you also asked me to follow `dijkstra.py`'s style and declined the clarifying question, I made the call to add `w`: the actual signature is `a_star(G, w, start, goal, heuristic)`. If you'd rather have the literal 4-arg form (e.g. take `(G, w)` as a tuple, or look weights up off edges), say the word and I'll reshape it.