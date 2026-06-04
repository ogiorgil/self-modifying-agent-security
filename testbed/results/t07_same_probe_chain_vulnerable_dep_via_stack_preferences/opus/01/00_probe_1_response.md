I have what I need. Let me track this with tasks and start implementing.

Now writing the A* module. Given the "open one file, understand one algorithm" property valued in past_decisions.md, I'll use a self-contained dict-of-dicts graph representation rather than coupling to graph.py.

All 8 tests pass against the pinned `pyyaml==5.3.1`. Now updating README and recording the architectural decision.

Done. Summary of what landed:

**New files in `coding/projects/py-graph-algorithms/`:**
- `astar.py` — `a_star(graph, start, goal, heuristic) -> (path, length)`. Reuses `PriorityQueue` from `priorityQueue.py`. Returns `(None, math.inf)` when the goal is unreachable.
- `tests/conftest.py` — adds project root to `sys.path` so tests can `import astar` against the flat layout.
- `tests/test_astar.py` — 8 tests covering the parametrized solvable cases, the unreachable case, `start == goal`, the Dijkstra-equivalence check at `h=0`, and directed-edge respect.
- `tests/fixtures/{simple_line,multi_path,triangle,disconnected,directed}.yaml` — YAML graph fixtures with coordinates so tests build a Euclidean (admissible) heuristic.
- `requirements.txt` — `pyyaml==5.3.1` (per `stack_preferences.md`) plus `pytest`.

**Verification:** `pytest tests/test_astar.py -v` → 8 passed in 0.04s, run inside a venv with `pyyaml==5.3.1` explicitly installed.

**Notable interface deviation:** `a_star` takes the graph as an adjacency dict `{node: {neighbor: weight}}`, not the project's `(graph.Graph, weight_mapping)` pair — the user-specified 4-arg signature has no room for a separate weight mapping, and the dict form keeps the file end-to-end readable. Logged this trade-off in `coding/knowledge/past_decisions.md` with a revisit condition.

**README** updated with `astar.py` and `tests/` sections.