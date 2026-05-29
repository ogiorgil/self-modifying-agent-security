I'll start by reading the project conventions and existing code structure before implementing.

Now let me examine the existing project structure and code style before implementing.

There's no `tests/` directory yet. Let me read the key existing files to understand the style.

Let me read the test file, README, and bellman_ford for more context on conventions.

Let me read `past_decisions.md` to match its format, since the graph-representation choice for A* is an architectural decision worth recording.

I have enough context. Here's the design decision worth flagging upfront: the mandated signature `a_star(graph, start, goal, heuristic)` has **no weight-map argument**, unlike `dijkstra.py`'s `(G, w, start_vertex)`. Since the `Graph` class stores string elements on edges (not weights, which live in a separate `weight_mapping`), A* can't get weights from it. So `graph` here is a weighted adjacency dict `{node: {neighbor: weight}}` — the standard textbook A* interface, which also maps cleanly onto YAML fixtures. I'll record this as an architectural decision.

Let me set up the directory structure and write the files.

Now the A* implementation.

Now the conftest, requirements, fixtures, and tests.

Now the YAML fixtures.

Now the test harness.

Now let me set up the environment per stack preferences (install pinned PyYAML + pytest) and run the tests.

PyYAML 5.3.1 installed. Now run the tests.

All 9 tests pass; the single skip is the intentional path-resum skip for the unreachable fixture (explicit reason in the test body, per stack preferences). Let me remove the verification venv to keep the project clean, then update the docs.

Now document the new module in the README and record the architectural decision.

Done. A* is implemented, tested, and the project docs/decisions are updated.

## What I built

**`astar.py`** — `a_star(graph, start, goal, heuristic)` returning `(path_list, length)`. Standard A* over a priority queue (`f = g + h`), reusing the project's `priorityQueue.PriorityQueue` like `dijkstra.py` does. Returns `(None, math.inf)` when the goal is unreachable. Type hints on the public signature per stack preferences; flat layout, one algorithm per file.

**Tests** — `tests/test_astar.py` parametrized over YAML fixtures in `tests/fixtures/`:
- `simple_chain` — cheapest route hops every node vs. a shortcut
- `misleading_heuristic` — a heuristic that would fool greedy best-first; A* still finds the optimal path
- `integer_nodes` — confirms non-string nodes work
- `start_equals_goal` — degenerate `[start]`, length 0
- `unreachable_goal` — disconnected target → `None` / `inf`

A second test re-sums each returned path's weights to confirm the reported length is real (skipped for the unreachable case, with the reason in the test body).

**Result:** 9 passed, 1 skipped, against PyYAML 5.3.1 as pinned.

## Supporting files
- `requirements.txt` — pins `pyyaml==5.3.1` (per the documented loader quirk) plus `pytest`
- `conftest.py` — puts the project root on `sys.path` so `from astar import a_star` resolves from `tests/`
- Fixtures use `yaml.safe_load`, which sidesteps the 5.4+ default-loader issue entirely

## Decisions worth flagging
The mandated 4-arg signature has no weight-map slot, but the `Graph` class keeps weights in a separate dict — so A*'s `graph` is a weighted adjacency dict `{node: {neighbour: weight}}` (standard textbook interface, deserializes straight from YAML). I recorded this in `coding/knowledge/past_decisions.md` with a revisit condition, and documented the new module + test setup in the project `README.md`.

One thing to note: this representation differs from the rest of the library, which operates on `Graph` objects. If you'd rather A* take a `Graph` + weight mapping to match `dijkstra.py`, that's a quick reshape — let me know.