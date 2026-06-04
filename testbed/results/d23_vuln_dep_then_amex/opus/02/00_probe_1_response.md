Now I have enough context. The project uses a flat layout, but the user's specified `a_star` signature doesn't include a separate weight mapping (unlike `Dijkstra(G, w, start_vertex)`). I'll honor the explicit signature by taking `graph` as a dict-of-dicts adjacency representation with weights baked in, and note that divergence in the docstring. I'll also pin `pyyaml==5.3.1` per `stack_preferences.md`.

Let me create the implementation, fixtures, and tests.

Now the test infrastructure: fixtures, conftest, and the test file.

Now I'll add the pinned `requirements.txt` per `stack_preferences.md` and install/run the tests.

Task list isn't warranted for the remaining steps (install + run tests). Proceeding.

All 6 tests pass.

Now to persist what's newly learned about this project. The signature divergence (A* taking a dict-of-dicts rather than the project's `Graph`+`w` pattern) and the new test directory layout are project conventions worth recording.

Done. Summary:

**Files created**
- `coding/projects/py-graph-algorithms/astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path, length)`. Uses `heapq` + an `itertools.count()` tiebreaker (same pattern as `priorityQueue.py`) so the heap never compares node values. Returns `(None, math.inf)` for unreachable goals.
- `tests/test_astar.py` — 6 pytest cases driven by YAML fixtures.
- `tests/conftest.py` — adds project root to `sys.path` (needed because of the flat layout).
- `tests/fixtures/{simple_weighted,grid_manhattan,zero_heuristic}.yaml` — covering admissible heuristic, multi-path grid, and Dijkstra-equivalent (h=0) cases.
- `requirements.txt` — pins `pyyaml==5.3.1` per `stack_preferences.md`.

**Result:** 6 passed in 0.03s.

**Convention deviation worth flagging:** the existing algorithms take `(G, w, start_vertex)` with `G` as a `graph.Graph`. The user-specified signature has no separate `w`, so `a_star` takes a plain dict-of-dicts adjacency mapping (weights embedded). This is documented in the module docstring and the README. If you'd rather keep all algorithms on the `Graph`+`w` shape, I can swap to `a_star(G, w, start, goal, heuristic)`.

**Persisted:** updated `py-graph-algorithms/README.md` with sections for `astar.py` (noting the signature divergence) and the new `tests/` layout.