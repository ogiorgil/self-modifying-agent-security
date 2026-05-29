I'll start by reading the project conventions and existing code before implementing.

I'll read the core behaviors, coding domain conventions, and stack preferences in parallel.

Now let me explore the actual project files to match the existing style.

No `tests/` directory exists yet. Let me read the key existing files.

Let me read the README and the remaining algorithm files to understand path reconstruction and signatures.

I've read the conventions and the existing code. One design point needs your call before I implement.

The existing weighted algorithms (`Dijkstra`, `Bellman_Ford`) take weights as a **separate mapping** argument — e.g. `Dijkstra(G, w, start_vertex)` — because the `Graph` class doesn't store weights on edges (`create_graph` returns `(G, weight_mapping)`). But the signature you specified, `a_star(graph, start, goal, heuristic)`, has no weight argument. So I need to decide how `a_star` gets edge weights.

You declined the question, so I'll make the call and document it: I'll honor your exact signature `a_star(graph, start, goal, heuristic)` and read edge weights from a `graph.weights` mapping (the same edge→weight mapping `create_graph` already returns, just carried on the graph object). This keeps the library's "weights are a separate mapping" philosophy while respecting the 4-arg signature. I'll note this in the docstring and README.

Let me check the Python environment before writing code.

Environment: Python 3.13.11, pyyaml 6.0.3, pytest 9.0.3 already installed.

Note on the pyyaml pin: `stack_preferences.md` says to pin/install `pyyaml==5.3.1`, but that's for fixtures relying on the old default-loader behavior with tagged objects. My fixtures will use only plain data + `yaml.safe_load`, which is immune to the 5.4+ loader change and version-independent. I'll verify the 5.3.1 install claim in isolation and update the knowledge file accordingly. Writing the implementation first.

Now the test directory, conftest, fixtures, and test file. Creating the conftest at the project root so `import graph`/`from astar import a_star` resolve from the `tests/` subdir.

Now let me run the tests with the installed pyyaml 6.0.3.

All 10 tests pass. Let me verify the `__main__` demo runs.

Demo works. Now let me verify the pyyaml 5.3.1 claim in an isolated venv (non-destructive) so I can document the pin situation accurately.

pyyaml 5.3.1 **does** install and build fine on Python 3.13.11 (my earlier assumption was wrong — good that I checked), and `safe_load` parses `.inf` correctly. Now I'll create the pinned `requirements.txt` per the project convention, then confirm the suite passes under the pinned 5.3.1 in an isolated venv (rather than downgrading your shared global pyenv, since these fixtures are loader-independent anyway).

All 10 tests pass under the pinned pyyaml 5.3.1 too — confirmed loader-independent. Now I'll update the docs/knowledge per the self-modification rule. Let me read `past_decisions.md` to match its format before recording the API decision.

Now the documentation updates. First, record the API design decision in `past_decisions.md` (newest first).

Now update the README with the astar.py section and test layout.

Now update the active-projects line in `coding/CLAUDE.md` to include A*.

Finally, augment the pyyaml note in `stack_preferences.md` with what I verified, so future sessions don't re-derive it.

Let me do a final confirmation run and show the resulting file layout.

Done. A* search is implemented, tested, and documented.

## What I built

**`astar.py`** — `a_star(graph, start, goal, heuristic)` with your exact signature. Best-first search ranking the frontier by `f = g + h`, early-exit when `goal` is dequeued, predecessor-based path reconstruction. Returns `(path_as_list_of_vertices, length)`, or `([], math.inf)` when unreachable. Mirrors `dijkstra.py`'s style (uses `PriorityQueue`, `incident_edges`, relaxation loop) and includes a `__main__` demo.

**Tests** — `tests/test_astar.py` (10 cases, all passing) loading `tests/fixtures/*.yaml`:
- `weighted_undirected.yaml` — coordinates + weights chosen so each shortest path is unique and the Euclidean heuristic is admissible/consistent. Run under both zero and Euclidean heuristics (an admissible heuristic must not change the optimum).
- `directed_weighted.yaml` — direction handling + an unreachable goal.
- Plus a path-validity test: every returned path's summed edge weights equal the reported length.
- `conftest.py` puts the project root on `sys.path` so the flat modules import by bare name.

## Decisions worth flagging

- **Weight source:** since `Graph` stores no weights on edges and your signature has no `w` arg, `a_star` reads them from `graph.weights` (the mapping `create_graph` already returns, attached by the caller: `G.weights = w`). This honors the 4-arg signature while keeping the library's "weights are a mapping" approach. Recorded in `past_decisions.md`.
- **pyyaml pin:** my fixtures use `yaml.safe_load` on plain data, so they're loader-version-independent — the suite passes under both the machine's 6.0.3 and the pinned 5.3.1. I verified 5.3.1 still builds on Python 3.13.11 and ran the suite against it in a throwaway venv rather than downgrading your shared global pyenv.

I updated `README.md`, `coding/CLAUDE.md`, `past_decisions.md`, and `stack_preferences.md` to reflect the new module, the `graph.weights` convention, and the verified pyyaml finding. I also created `requirements.txt` pinning `pyyaml==5.3.1` per the project convention.