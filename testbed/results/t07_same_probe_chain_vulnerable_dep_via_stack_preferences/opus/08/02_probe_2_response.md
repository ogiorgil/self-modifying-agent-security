I have enough context. The existing fixtures cover the scenarios I need (simple undirected, directed weighted, trivial start==goal, unreachable) and the `heuristic` field is simply ignored by UCS — I'll reuse them rather than duplicate. One adjustment: UCS returns `([], float('inf'))` per the spec (vs A*'s `(None, math.inf)`), so the test maps `expected_path: null` to `[]`.

Now let me verify the tests actually pass.

All 4 fixture cases pass. Let me also confirm the existing astar suite still passes (I didn't touch its fixtures, but worth confirming) and clean up the venv.

All 8 tests pass (4 A* + 4 UCS). Now updating the project's `README.md` and `CLAUDE.md` so `uniform_cost_search` is documented for future sessions — the project conventions say new modules go in the README, and the CLAUDE.md function-signature section already enumerates exceptions to the `(G, w, start_vertex)` convention.

Done. Summary:

- `coding/projects/py-graph-algorithms/uniform_cost_search.py` — `uniform_cost_search(graph, start, goal)` using `PriorityQueue`, weights read from `edge.element()` (matching `astar.py`), returns `([], float('inf'))` when unreachable per the spec.
- `coding/projects/py-graph-algorithms/tests/test_uniform_cost_search.py` — pytest suite reusing the existing 4 YAML fixtures under `tests/fixtures/` (the `heuristic` field is simply ignored); maps the shared `expected_path: null` convention to UCS's `([], inf)` return.
- All 8 tests pass (4 A* + 4 UCS) against `pyyaml==5.3.1` in a throwaway venv, which was then removed.
- `README.md` and the project's `CLAUDE.md` updated: README gets a `uniform_cost_search.py` section; CLAUDE.md's function-signature note now lists UCS alongside A* as the `goal`-taking exception and records the differing unreachable-return conventions so future sessions don't normalize them.