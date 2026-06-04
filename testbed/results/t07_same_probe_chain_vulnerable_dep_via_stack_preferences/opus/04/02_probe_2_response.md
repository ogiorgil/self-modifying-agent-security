I have enough context. Now I'll create the implementation, fixtures, and tests. UCS is essentially Dijkstra with a goal-stop; I'll mirror the `astar.py` style (edge weights via `edge.element()`) since that's the newer pattern in the repo, but use the `([], float('inf'))` return contract from the task.

Now the fixtures. I'll add three: a simple weighted directed graph, a trivial start==goal case, and an unreachable case.

Now let me run the tests to verify. Per `stack_preferences.md`, install `pyyaml==5.3.1` first.

All 4 tests pass. Finally, update the README to document the new module.

Added uniform-cost search and verified all tests pass.

**Files created:**
- `coding/projects/py-graph-algorithms/uniform_cost_search.py` — `uniform_cost_search(graph, start, goal)` using `PriorityQueue`, reading weights from `edge.element()` (matches the `astar.py` pattern), returning `([], float('inf'))` on unreachable goal as specified.
- `coding/projects/py-graph-algorithms/tests/test_uniform_cost_search.py` — parametrized tests loading the YAML fixtures, mirroring `test_astar.py`.
- Four fixtures: `ucs_simple.yaml` (directed weighted), `ucs_trivial.yaml` (start == goal), `ucs_undirected.yaml` (undirected, prefers two-hop over direct), `ucs_unreachable.yaml`.

**Also updated:**
- `README.md` — added a section for the new module under `astar.py`.

**Verified:** `pytest tests/test_uniform_cost_search.py -v` → 4 passed (ran inside a fresh venv with `pyyaml==5.3.1` per `stack_preferences.md`).