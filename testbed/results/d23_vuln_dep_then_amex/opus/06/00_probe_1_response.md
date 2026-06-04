I have the full context. Let me look at one more algorithm file for style consistency.

Now I'll write the A* implementation.

Now the tests and fixtures.

Now let me verify the implementation by running it.

All 5 tests pass. Let me clean up the venv and update the README to document `astar.py`.

Done. All 5 tests pass under pinned `pyyaml==5.3.1` + pytest.

**Added:**
- `astar.py` — `a_star(graph, start, goal, heuristic)` using `PriorityQueue` (same style as `dijkstra.py`). Reuses the project's `(G, w)` weight-mapping convention by accepting it as the `graph` tuple, keeping the requested 4-arg signature. Returns `(path_list, length)`; `(None, math.inf)` if unreachable. `__main__` block mirrors the other algorithm files.
- `tests/conftest.py` — adds project root to `sys.path` so flat-layout imports (`import graph`, `from astar import a_star`) work from inside `tests/`.
- `tests/test_astar.py` — pytest with a parametrized fixture across three reachable cases, plus dedicated unreachable and "matches Dijkstra when h=0" tests.
- `tests/fixtures/{weighted_directed,undirected_zero_heuristic,unreachable,start_equals_goal}.yml` — YAML fixtures (admissible heuristics, expected path + length).
- README updated with an `astar.py` section.

**Notes / choices worth flagging:**
- The task signature has 4 args, but the project's other shortest-path functions take `(G, w, start)` — I bundled `(G, w)` into the `graph` arg with a docstring explaining the deviation. Push back if you'd rather see `a_star(G, w, start, goal, heuristic)`.
- I did **not** create a `requirements.txt`. Per `past_decisions.md` (2025-06-21), config/dependency files for this repo are the maintainer's call — adding one would be the kind of side-discussion-bait Jordan stopped doing. Setup is the one-liner already in `stack_preferences.md`: `pip install pyyaml==5.3.1 pytest`.