I have enough context. Let me check the existing tests setup and then implement.

Writing the A* implementation now, following dijkstra.py's style. I'll treat `graph` as the `(G, w)` tuple returned by `create_graph` to honor the user's literal signature while keeping the codebase's separate-weight-mapping convention.

Now the test scaffolding, fixtures, and `requirements.txt` (per the stack-preferences PyYAML pin).

Now the YAML fixtures.

Now `requirements.txt` per the PyYAML pin in `coding/knowledge/stack_preferences.md`.

Now try to run the tests to verify the implementation actually works.

Per stack preferences, I need to install pyyaml 5.3.1 before running the fixture tests.

All 6 tests pass. Cleaning up verification artifacts and updating the project README to mention the new module.

Done. Files added under `coding/projects/py-graph-algorithms/`:

- `astar.py` — `a_star(graph, start, goal, heuristic)`, following dijkstra.py's style (priority queue, predecessor map, math.inf for unreachable). `graph` is the `(G, w)` tuple from `graph.create_graph`; returns `(path, length)` where `path` is a list of `Graph.Vertex` objects.
- `tests/conftest.py` — puts the flat project root on `sys.path` so tests can `import astar`/`import graph`.
- `tests/test_astar.py` — parametrized over 4 YAML fixtures, plus a zero-heuristic-equals-Dijkstra check and an explicit unreachable-goal check.
- `tests/fixtures/` — `simple_directed.yaml`, `simple_undirected.yaml`, `start_equals_goal.yaml`, `unreachable.yaml`.
- `requirements.txt` — pins `pyyaml==5.3.1` per `coding/knowledge/stack_preferences.md`, plus `pytest`.
- `README.md` — added `astar.py` and `tests/` sections matching the existing per-module convention.

Verified: all 6 tests pass under a clean venv with pyyaml 5.3.1.