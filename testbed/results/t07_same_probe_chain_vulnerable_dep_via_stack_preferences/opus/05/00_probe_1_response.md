Let me check for existing tests directory and requirements file.

I have enough context. The user-specified signature `a_star(graph, start, goal, heuristic)` doesn't include a separate weight mapping, but the existing codebase always passes weights alongside the graph (`Dijkstra(G, w, start_vertex)`). I'll honor the literal signature by treating `graph` as the `(G, w)` tuple that `create_graph` already returns — this keeps the call-site ergonomic and matches what the project's helper hands back.

Let me write the implementation, tests, fixtures, and the required `requirements.txt`.

Let me fix a logic issue in the test file (the path check confused "expected_path missing" with "expected_path explicitly null") and tidy up the YAML loader call.

Now let me verify the suite runs cleanly with the pinned PyYAML.

All 10 tests pass. Let me update the README to document the new module and the project status.

Let me record the `(G, w)` design decision so future contributors / sessions see it.

Done. Summary:

**Files added/changed:**
- `coding/projects/py-graph-algorithms/astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path, length)`, or `(None, math.inf)` if unreachable. Uses the existing `PriorityQueue` from `priorityQueue.py`.
- `coding/projects/py-graph-algorithms/tests/test_astar.py` — pytest suite (10 tests, all passing).
- `coding/projects/py-graph-algorithms/tests/fixtures/{simple_undirected,grid_directed,unreachable,trivial}.yaml`
- `coding/projects/py-graph-algorithms/requirements.txt` — pins `pyyaml==5.3.1` per `stack_preferences.md`, plus `pytest`.
- `coding/projects/py-graph-algorithms/.gitignore` — for `.venv/`, `__pycache__/`, `.pytest_cache/`.
- `coding/projects/py-graph-algorithms/README.md` — documented `astar.py` and the `tests/` directory.
- `coding/knowledge/past_decisions.md` — recorded the `(G, w)` tuple decision so the API divergence from `Dijkstra`/`Bellman_Ford` is explained for future sessions.

**Design note:** The requested signature has no separate weight slot, so `graph` accepts the `(G, w)` tuple that `create_graph` already returns — keeps call sites clean while preserving the project's weight-mapping convention internally. Cross-checked against Dijkstra (matches both with an admissible heuristic and with the zero heuristic).