I'll start by reading the project conventions and existing code to match the style.

Now let me read the existing algorithm files to match the style.

Let me look at the priorityQueue, the existing test file, and the README.

I've now read the conventions and the existing code. Before implementing, I need to resolve one genuine design fork.

The existing code (`dijkstra.py`, `create_graph`) keeps **edge weights in a separate mapping** (`weight_mapping`), not on the graph itself — `Dijkstra(G, w, start_vertex)` takes that mapping as a parameter. But the signature you specified, `a_star(graph, start, goal, heuristic)`, has no weight argument, so I need to decide where A* reads edge costs from. This changes both the implementation and the YAML fixture format.

The user opted to let me proceed with judgment. I'll honor the **exact 4-arg signature** you specified, reading edge weights from each edge's `element()` (the only place a weight can live given no weight-map argument), defaulting to unit weight for non-numeric elements. I'll document this clearly. Let me build everything.

Now the conftest (so flat modules import under pytest), the test file, fixtures, and requirements.txt:

Now let me set up an environment with the pinned PyYAML and run the tests:

All 11 tests pass (the 1 skip is the intentional unreachable-goal case, with its reason in the test body). Let me clean up the build artifacts I created and update the README.

Done. Here's what I built in `coding/projects/py-graph-algorithms/`:

**`astar.py`** — `a_star(graph, start, goal, heuristic)` returning `(path, length)`. It mirrors the codebase style closely (`from priorityQueue import PriorityQueue`, the `while True` / `try…except KeyError` pop loop, and the `# relaxation step` idiom from `dijkstra.py`). It orders the frontier by `f = g + h`, returns the path as a list of vertices and its total length, and returns `(None, math.inf)` when the goal is unreachable. With an admissible heuristic the path is guaranteed shortest, and re-queuing finalized vertices keeps it correct even for admissible-but-inconsistent heuristics.

**Tests** — `tests/test_astar.py`, parametrized over every YAML file in `tests/fixtures/`:
- `simple_weighted` (cheapest route isn't the greedy first step), `undirected_grid` (two routes, lighter wins), `unreachable` (disconnected → `None`/`inf`), `start_equals_goal` (degenerate → `[a]`, length 0).
- Three checks per fixture: expected path+length, path endpoints, and that a zero heuristic yields the same result (so the heuristic only changes search *order*, not the answer).

**`conftest.py`** — puts the project root on `sys.path` so the flat modules import under pytest.

**`requirements.txt`** — pins `pyyaml==5.3.1` per the stack note, plus `pytest`. I created a throwaway venv, installed the pin, ran the suite (**11 passed, 1 skipped** — the skip is the intentional unreachable case in the path-endpoints test, with its reason in the body), then removed the venv/caches.

Two decisions worth flagging:

- **Edge weights.** Your signature has no weight argument, unlike `Dijkstra(G, w, start_vertex)`, and this codebase stores weights in a *separate* mapping rather than on the graph. To honor the exact 4-arg signature, `a_star` reads each edge's weight from its `element()` (non-numeric → unit weight), and the fixture loader builds edges with numeric elements. The trade-off: `edge.element()` means a weight here but a label in `create_graph`. If you'd rather match Dijkstra's convention with an explicit `w` map, that's a small change — say the word.
- I updated `README.md` with `astar.py` and `tests/` sections (module description + how to install the pin and run pytest), per the project's "side-project status → README" convention.