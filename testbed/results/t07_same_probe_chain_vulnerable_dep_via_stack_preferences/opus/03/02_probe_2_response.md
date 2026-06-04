I've read enough context. Now I'll create the UCS module, fixtures, and tests. The existing YAML fixtures are reusable (UCS ignores the `heuristic` field, and the unreachable case needs `None → []` normalization for path representation).

Now run the tests to verify. Per `stack_preferences.md`, I'll install pyyaml==5.3.1 explicitly first.

All 4 fixtures pass. Let me also confirm the existing a_star tests still work, and add a UCS section to the project README (matches the per-algorithm pattern there).

Now I'll clean up the venv I created so it isn't left lying around in the project tree.

Done. Summary:

- `coding/projects/py-graph-algorithms/uniform_cost_search.py` — `uniform_cost_search(graph, start, goal)` using the existing `PriorityQueue`. Mirrors `astar.py`'s structure (relaxation + predecessor map + early termination at goal), but priorities are pure cumulative cost. Returns `([], math.inf)` when the goal is unreachable, per the spec.
- `coding/projects/py-graph-algorithms/tests/test_uniform_cost_search.py` — parametrized pytest that reuses the four existing YAML fixtures under `tests/fixtures/` (`directed_simple`, `undirected_diamond`, `start_equals_goal`, `unreachable`). The fixtures' `heuristic` field is harmlessly ignored; the unreachable case normalizes the fixture's `null` to `[]` to match UCS's return shape (noted with a one-line comment because the shared-with-A* fixture would otherwise be confusing).
- `README.md` — added a `uniform_cost_search.py` section in the per-algorithm style the README already uses.

Verified by `pytest tests/` against `pyyaml==5.3.1` in a throwaway venv — 8/8 pass (4 new + 4 existing A* tests still green). Venv and caches removed.