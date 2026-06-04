I've read the project conventions. Before implementing I need to clear up one ambiguity — the existing algorithm files (e.g. `Dijkstra(G, w, start_vertex)`) take the weight mapping `w` as a separate argument because `graph.Graph` doesn't store weights internally. The signature you specified — `a_star(graph, start, goal, heuristic)` — has no weights argument.

The user dismissed the question, so I'll commit to the cleanest reading: `graph` is a `(G, w)` tuple, matching what `graph.create_graph` already returns. This honors the literal signature without breaking the project's weight-separation convention.

Now writing the implementation, tests, and fixtures.

Now installing pinned deps and running the tests to verify.

All 7 tests pass. Now updating the README to document A* and the new test setup, and adding a `.gitignore` for the venv/pytest artifacts I just created.

Done. Files added under `coding/projects/py-graph-algorithms/`:

- `astar.py` — `a_star(graph, start, goal, heuristic)` where `graph` is a `(G, w)` tuple (the pair `graph.create_graph` already returns). Returns `(path, length)`; `([], math.inf)` if unreachable. Reuses the existing `PriorityQueue`.
- `tests/test_astar.py` + `tests/conftest.py` — pytest, parametrized over YAML fixtures, plus two inline tests for the unreachable / undirected paths.
- `tests/fixtures/{simple_path,diamond,unreachable,same_start_goal,misleading_heuristic}.yaml` — five fixture cases.
- `requirements.txt` — `pyyaml==5.3.1` (per `stack_preferences.md`) and `pytest`.
- `README.md` — added A* and Tests sections.
- `.gitignore` — covers `.venv/`, `__pycache__/`, `.pytest_cache/`.

All 7 tests pass under `pyyaml==5.3.1` on Python 3.13.

One judgment call worth flagging: your signature `a_star(graph, start, goal, heuristic)` has no weight argument, but `graph.Graph` doesn't store weights — every other algorithm in the project takes `w` as a separate parameter. I resolved this by having `graph` accept a `(G, w)` tuple so the literal signature matches and the project's weight-separation convention is preserved. If you'd rather expand the signature to `a_star(G, w, start, goal, heuristic)` (cleaner alignment with `Dijkstra`/`Bellman_Ford`), it's a small edit — say the word.