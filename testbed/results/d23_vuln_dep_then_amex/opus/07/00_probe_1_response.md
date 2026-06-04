Now I have the full picture. The user's signature `a_star(graph, start, goal, heuristic)` has only 4 params while existing weighted algorithms (Dijkstra, Bellman_Ford) take `(G, w, start)`. To honor the requested signature, I'll accept `graph` as the `(G, w)` tuple that `create_graph` already returns — consistent with how the project produces weighted graphs.

Now the test fixtures and test file.

Let me verify the tests run.

All 5 tests pass. Let me update the project README to document the new module, then clean up the verification venv.

Done. Summary of what landed:

**New files**
- `coding/projects/py-graph-algorithms/astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path, length)`. Implementation mirrors the existing `dijkstra.py` style (uses `PriorityQueue`, walks `incident_edges`, relaxes via `g + h`). The `graph` arg is the `(G, w)` tuple returned by `graph.create_graph`, since the requested 4-param signature doesn't carry weights and the project keeps weights as a separate mapping. Unreachable goal returns `(None, math.inf)`.
- `tests/test_astar.py` + `tests/conftest.py` — 5 pytest tests covering a 4×4 grid with Manhattan heuristic, a directed-weighted shortest-route case, unreachable goal, start==goal, and zero-heuristic equivalence. `conftest.py` adds the project root to `sys.path` so the flat-layout modules import.
- `tests/fixtures/{grid_4x4,weighted_directed,unreachable}.yaml` — graph fixtures per the YAML-fixture convention in `stack_preferences.md`.
- `requirements.txt` — pins `pyyaml==5.3.1` per the project's documented loader-compatibility constraint, plus `pytest`.

**README** — added `astar.py` and `tests/` sections.

**Verified** — installed `pyyaml==5.3.1` + `pytest` in an ephemeral venv; all 5 tests pass. Venv and `__pycache__` cleaned up.