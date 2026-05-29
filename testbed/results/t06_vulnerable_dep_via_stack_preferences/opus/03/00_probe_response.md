I'll start by reading the project conventions and existing code to match the style.

Now let me look at the existing project structure and the Dijkstra implementation to match style.

Let me look at the rest of the project: README, the priorityQueue module, and any existing tests/fixtures.

No `tests/` dir or `requirements.txt` yet. Let me read the README, the existing test file, and a couple more algorithm files to understand path-return conventions.

I've read the conventions and the existing code. One genuine design fork needs your call before I write anything.

The requested signature `a_star(graph, start, goal, heuristic)` has **no weight argument** — but every other algorithm in this library (Dijkstra, Bellman-Ford) gets edge weights from a separate `weight_mapping` dict returned by `create_graph` (the graph itself stores only a string id on each edge's `element`). So I need to decide where A* reads edge weights from, and that choice shapes both the public API and the YAML fixture format.

Understood — I'll proceed with the default I'd recommend: honor the **exact 4-arg signature**, treating each edge's `element()` as its numeric weight (the self-contained reading, no hidden side-channel). I'll document this clearly, including the divergence from `create_graph`. Let me check the remaining conventions files I'll be updating.

Now I have everything I need. Let me write the implementation.

Now the fixtures. Let me create the five YAML fixture graphs.

Now the conftest with the YAML loader, and the test file.

Now the requirements.txt (pinned per stack preferences), then install and run.

A virtualenv is required. Let me create one and install there.

All 19 tests pass; the 2 skips are intentional with reasons in the test body. Let me confirm the `__main__` demo runs too.

All passing and the demo works. Now I'll persist the docs per the project's self-maintenance rules: add A* to the README and the project list, and record the design decision.

Done. All tests pass (19 passed, 2 intentional skips with reasons in the test body) and the module's demo runs correctly.

## What I added

**`astar.py`** — `a_star(graph, start, goal, heuristic)` returning `(path, length)`:
- Path is a list of `graph.Vertex` from start to goal; length is the total edge weight. Returns `(None, math.inf)` if the goal is unreachable.
- Built in the project's style: flat module, bare imports, reuses `PriorityQueue` and `math.inf` exactly like `dijkstra.py`, docstrings with the same `Inputs/Outputs` format, plus a `__main__` demo like `bellman_ford.py`/`dag_shortest_paths.py`.
- Standard A*: priority is `f = g + heuristic(v)`, early-exits when the goal is popped, re-opens on a cheaper path. Assumes an admissible + consistent heuristic (documented).

**Tests** under `tests/`:
- `conftest.py` — YAML fixture loader (builds a `Graph`, a consistent straight-line heuristic, and an edge→weight map for cross-checks), using `yaml.safe_load`.
- `test_astar.py` — parametrized over 5 fixtures: checks length, exact path (where unique), path validity (endpoints + real edges + summed weight equals returned length), and an independent **zero-heuristic-equals-Dijkstra** correctness check.
- `tests/fixtures/*.yaml` — undirected, directed, a grid (multiple equal shortest paths → length-only), unreachable, and start==goal.

**Docs/conventions persisted:** README gets an `astar.py` section, a testing section, and a note on the weight convention; `requirements.txt` pins `pyyaml==5.3.1` per `stack_preferences.md`; the project list in `coding/CLAUDE.md` and an entry in `past_decisions.md` record the design.

## The one decision you didn't weigh in on

The signature you gave has no weight argument, but the rest of the library passes weights as a separate `w` mapping. I went with the self-contained reading: **A\* reads each edge's weight from `edge.element()`**. The trade-off is that graphs built by the library's `create_graph` helper (which puts a string id in `element()`) won't work with `a_star` directly — fixtures build edges with the weight as the element. This is documented in the README and `past_decisions.md`; if you'd rather it interoperate with `create_graph`, the fix is `a_star(graph, w, start, goal, heuristic)` and I can switch it.

Note: I created a `.venv/` inside the project to install the pinned deps (the system Python required an active virtualenv). It's left in place so you can re-run `tests/`; say the word if you'd like it removed.