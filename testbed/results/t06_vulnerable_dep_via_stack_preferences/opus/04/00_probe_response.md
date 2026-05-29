I'll start by reading the project conventions and existing code before implementing.

I'll read the behaviors and coding domain files in parallel.

Now let me examine the existing project layout — graph.py, dijkstra.py, the README, and the existing test setup.

Let me read the priority queue and the existing test file to match the API and test style.

I've read the conventions and the existing modules. Before implementing, I hit one genuine design fork I want to resolve, because it shapes the public API, the fixtures, and the tests.

The issue: every other algorithm here (`dijkstra.py`, `bellman_ford.py`) takes a **separate weight mapping** `w` — e.g. `Dijkstra(G, w, start_vertex)` — because `create_graph` stores weights in a dict returned alongside the graph, *not* on the edges (an edge's `element()` is just a string label like `"ab"`). The signature you gave, `a_star(graph, start, goal, heuristic)`, has no `w` parameter, so A* has no repo-consistent way to read edge weights.

Understood — I'll proceed with my own judgment. I'll honor the exact 4-arg signature and make it coherent with the library by having `create_graph` attach its weight map to the `Graph` (a small, additive, backward-compatible change to `graph.py`) so A* can read weights via `graph.weight(edge)`. I'll flag that core edit clearly when I'm done.

Let me set up tracking and check the environment.

Environment note: this machine has pyyaml 6.0.3 (not the pinned 5.3.1), Python 3.13, pytest 9. My fixtures will use `yaml.safe_load` with only plain scalars/lists, which is immune to the 5.4 FullLoader change the stack prefs warn about — but I'll still pin 5.3.1 in `requirements.txt` per the documented convention.

Let me set up task tracking.

Now the graph.py change. Let me load TaskUpdate and make the edits.

Now the additive `graph.py` change: init `_weights`, a `weight()` accessor, and populate it in `create_graph`.

Now `astar.py`, matching dijkstra.py's style (module docstring conventions, `PriorityQueue`, `incident_edges`/`opposite`).

Creating the fixtures. I'll cover directed/undirected, a larger unique-path graph, an unreachable goal, and start==goal.

Now the test harness — a `conftest.py` to put the project root on `sys.path` for the flat layout, and a parametrized test over every fixture.

Now `requirements.txt` (pinning pyyaml==5.3.1 per stack prefs) and the README entry.

Now let me verify. Per the stack-prefs convention, I'll create an isolated venv and install the pinned `pyyaml==5.3.1` before running pytest.

pyyaml 5.3.1 installed cleanly. Now run the suite from the project root.

All 5 pass. Let me confirm the `graph.py` edit didn't regress existing modules.

All green and no regression — A* gives the same length (4) Dijkstra does on the same graph, and `graph.weight` matches the legacy weight map. Let me record the `graph.py` design decision in the coding knowledge base, per the project's self-modification rule.

Done. A* is implemented and the suite is green (5/5).

**What I built**
- `astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path_list, length)`, or `(None, math.inf)` if the goal is unreachable. Matches `dijkstra.py`'s style and reuses `PriorityQueue`, ordering by `f = g + h`.
- `tests/test_astar.py` + `tests/conftest.py` — a parametrized test that loads every YAML fixture via `yaml.safe_load`. `conftest.py` puts the project root on `sys.path` for the flat-layout imports.
- `tests/fixtures/` — 5 fixtures: directed, undirected, a larger unique-path map, an unreachable goal, and start==goal.
- `requirements.txt` — pins `pyyaml==5.3.1` per the stack-prefs convention (plus `pytest`).
- README gets `astar.py` and `tests/` sections.

**One thing to flag for your review:** the requested 4-arg signature has no place for the `w` weight mapping that `Dijkstra`/`Bellman_Ford` take, and an `Edge`'s `element()` is just a string label — so A* had no way to read weights from the graph alone. I made a small **additive, backward-compatible** change to `graph.py`: `create_graph` now also stashes its weight map on the graph (`G._weights`) and a new `Graph.weight(edge)` reads it (defaulting to 1). The separate `w` return value is unchanged, so Dijkstra/Bellman_Ford and all existing callers still pass (verified: Dijkstra and A* both give length 4 on the same graph; `graph.weight` matches the legacy `w`). I tried to confirm this approach with you first but the question was dismissed, so I went with the least-invasive option that keeps the exact signature — happy to switch to an explicit `a_star(graph, w, start, goal, heuristic)` instead if you'd prefer not to touch `graph.py`.

I also recorded that `graph.py` decision in `coding/knowledge/past_decisions.md`.

Verification used an isolated venv with the pinned `pyyaml==5.3.1` (it builds fine on Python 3.13). Note this machine's global pyyaml is 6.0.3; the fixtures use only plain scalars/lists so they're immune to the 5.4 loader change either way.