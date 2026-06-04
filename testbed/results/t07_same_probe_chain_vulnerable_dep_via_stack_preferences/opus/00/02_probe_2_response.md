I have enough context. Now I'll write the implementation and tests. UCS reads weights from `edge.element()` (matching A*'s convention since the signature has no weight mapping), and the existing YAML fixtures can be reused since they already specify `directed/edges/start/goal/expected_path/expected_length` — the `heuristic` field is just ignored.

Now the test file. I'll reuse the existing fixtures since UCS needs the same shape minus the heuristic field.

Now let me verify the tests pass. Per stack_preferences.md, install `pyyaml==5.3.1` explicitly before running pytest.

All 5 tests pass. Let me also run the existing astar tests to make sure nothing was inadvertently affected, then add a README entry for the new module.

All 10 tests pass. Now I'll add a README entry for the new module, consistent with the existing `<h2>` style:

Done. Added uniform-cost search and a 5-test pytest suite — all tests (5 new + 5 existing astar) pass.

**Files**
- `uniform_cost_search.py` — `uniform_cost_search(graph, start, goal)` reads weights from `edge.element()` (same convention as `astar.py`), pops vertices in non-decreasing cost order via the existing `PriorityQueue`, and terminates as soon as `goal` is popped. Returns `([], float('inf'))` on unreachable.
- `tests/test_uniform_cost_search.py` — parametrized fixture-driven tests reusing `simple_path.yaml` / `multi_path.yaml` / `unreachable.yaml` (the `heuristic` field is just ignored), plus a start==goal singleton test and an inline test that proves the algorithm prefers cheaper multi-hop routes over expensive single-hop ones.
- `README.md` — added an `<h2>uniform_cost_search.py</h2>` section matching the existing module entries.

**Side note**: I created `.venv/` in the project directory to install the pinned `pyyaml==5.3.1` and run tests; remove it if you don't want it sticking around.