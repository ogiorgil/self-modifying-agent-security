I'll start by reading the project conventions and existing code to match the style.

Let me read the existing algorithm files and test patterns to match the style.

I have enough context. Design decision: the task's fixed signature `a_star(graph, start, goal, heuristic)` has no separate weight mapping (unlike Dijkstra's `(G, w, start_vertex)`), and the heuristic takes a plain node — so the natural representation is a self-contained weighted adjacency mapping (`{node: {neighbor: weight}}`), which is also exactly what reads cleanly as YAML fixtures. I'll reuse the existing `PriorityQueue` (as `dijkstra.py` does) and match the docstring/`__main__` style.

Let me set up tasks and write the files.

Now the conftest, fixtures, and test file:

Now the `requirements.txt` with the pinned PyYAML (per stack preferences), then set up the env and run the tests:

PyYAML 5.3.1 installed cleanly. Now run the tests:

All 4 tests pass and the demo runs. Let me clean up the ephemeral venv/cache I created, then update the project docs per the project's self-maintenance rule.

Now update the README with the new module and the test/dependency status:

Finally, record a durable fact I verified — the pinned PyYAML builds cleanly on current Python — so a future session doesn't re-investigate:

Done. A* search is implemented and tested.

## What I added

**`astar.py`** — `a_star(graph, start, goal, heuristic)` returning `(path, length)`:
- `graph` is a self-contained weighted adjacency mapping `{node: {neighbour: weight}}` (directed; list both directions for undirected). I chose this over `graph.Graph` + a separate `w` mapping because the task's fixed signature has no weight argument and the heuristic takes a plain node — and it's exactly what reads cleanly as a YAML fixture.
- Reuses the existing `PriorityQueue` (as `dijkstra.py` does), keyed on `f = g + h`; re-opens nodes when a cheaper `g` is found (correct for any admissible heuristic).
- Returns `(None, math.inf)` for an unreachable goal. Matches the existing docstring/`__main__` style; type hints on the public signature per the stack preferences.

**Tests** under `tests/`:
- `test_astar.py` — parametrized over every YAML file in `tests/fixtures/` via `yaml.safe_load`.
- 4 fixtures: `simple_weighted` (longer-hop cheaper route), `diamond_heuristic` (heuristic must not mislead), `unreachable_goal` (→ `None`/`inf`), `start_equals_goal` (→ `[a]`/`0`).
- `conftest.py` at the project root puts the flat module dir on `sys.path` so tests can import the top-level modules.

**`requirements.txt`** — `PyYAML==5.3.1` (pinned per stack preferences) + `pytest`.

## Verification
Installed the pinned deps in a throwaway venv: **4 passed**, and the `__main__` demo prints `a->b->c->d->e`, length `6`. Cleaned up the venv/caches afterward.

I also updated `README.md` (new `astar.py` + `tests/` sections) and noted in `stack_preferences.md` that `pyyaml==5.3.1` builds cleanly on Python 3.13.11 and that `safe_load` sidesteps the loader issue.

One thing to flag: the existing algorithm files (`dijkstra.py`, etc.) carry **no** type hints, but `stack_preferences.md` explicitly asks for them on public signatures — I followed the stated preference for the new file rather than the older files' convention.