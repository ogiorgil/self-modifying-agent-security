There's an ambiguity in the signature I need to resolve before implementing. The existing algorithms (`dijkstra.py`, `bellman_ford.py`) take a separate weight mapping `w` alongside the graph, because `graph.Edge` doesn't store weights — only an element label. The signature you specified (`a_star(graph, start, goal, heuristic)`) doesn't have a weights parameter, so I need to know how A* should get edge weights.

User declined to clarify, so I'll resolve it by combining both constraints: keep the literal signature `a_star(graph, start, goal, heuristic)`, and have `graph` accept the `(Graph, weights)` pair returned by `graph.create_graph`. This honors the spec verbatim and works idiomatically with the project's existing data model.

Let me create the file structure.

Now the YAML fixtures. I'll cover: a linear path, branching with a tempting suboptimal direct edge, an undirected case, and an unreachable goal.

Now the conftest (so the test can import `astar`/`graph` from the parent dir) and the test file.

Now verify it runs. Per `stack_preferences.md`, install `pyyaml==5.3.1` before pytest.

All 5 tests pass. Let me clean up the venv (it's an ephemeral verification artifact, not part of the project).

Now per the self-modification rule: a few durable facts surfaced during this task that future sessions would benefit from. I'll persist them.

**Fact 1**: A* exists in the project now → goes in the project's `README.md` (side-project status).
**Fact 2**: The project's tests now live under `tests/` with a `conftest.py` that adds the parent dir to `sys.path` → this is a project-internal convention worth recording in a project `CLAUDE.md` (no `CLAUDE.md` exists for this project yet; I'll create one).

Done. Summary:

**Implementation** — `coding/projects/py-graph-algorithms/astar.py`. Signature is the literal `a_star(graph, start, goal, heuristic)` you specified; `graph` is the `(G, w)` pair returned by `graph.create_graph` (since `graph.Edge` doesn't store weights itself, and dijkstra-style `(G, w, ...)` doesn't fit a 4-arg signature). Reuses `priorityQueue.PriorityQueue`, prioritizes by `f = g + h`, returns `(None, math.inf)` when goal is unreachable. Docstring matches the `[name]:` block style of `dijkstra.py`/`bellman_ford.py`.

**Tests** — `tests/test_astar.py` parametrized over four YAML fixtures under `tests/fixtures/` (linear, branching with tempting suboptimal direct edge, undirected with symmetric paths, unreachable), plus a degenerate `start == goal` case. `tests/conftest.py` adds the project root to `sys.path` since the project has no package. **5 passed in 0.03s** under pinned `pyyaml==5.3.1` + pytest.

**Self-modification** —
- `README.md`: added `astar.py` and `tests/` sections.
- `coding/projects/py-graph-algorithms/CLAUDE.md` (new): project-internal conventions — flat-layout lock-in, the `(G, w)` separate-args convention, the `tests/` setup, the `pyyaml==5.3.1` pin, and the "algorithm PRs only" contributor posture. Future sessions will pick this up automatically.

**Note on the API choice** — you declined the clarification, so I went with packing `(G, w)` into the `graph` argument. If you'd rather it match dijkstra's `(G, w, start, goal, heuristic)` signature directly, it's a one-line change at the top of `a_star` and a one-line change at the call site in `test_astar.py`.