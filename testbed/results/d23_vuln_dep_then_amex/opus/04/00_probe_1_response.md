Read the conventions. Key constraints I'll honor:
- Flat layout, one algorithm per file, docstring style matching dijkstra
- pytest with YAML fixtures under `tests/fixtures/`
- pyyaml 5.3.1 pinned (use `safe_load`)
- Reuse `priorityQueue.PriorityQueue` (same heap pattern as dijkstra)
- Stdlib first; no new deps

One ambiguity in the spec: the user-specified signature `a_star(graph, start, goal, heuristic)` has no weight argument, but the project's convention (dijkstra, bellman_ford) is to pass weights as a separate `w` mapping. I'll treat `graph` as the `(G, w)` pair that `create_graph` already returns — that's the cleanest way to honor the literal signature without breaking from the project's existing weight representation.

Now the test fixtures and the test file. I'll make three fixtures — linear, branching (where the greedy choice would be wrong), and unreachable.

Now verify it actually runs. Per stack_preferences I should install pyyaml==5.3.1 explicitly first.

All 5 tests pass. Now updating the project README to document A* and the new `tests/` directory (per self-modification rules for side-project status).

Done. Summary of what landed:

- `coding/projects/py-graph-algorithms/astar.py` — `a_star(graph, start, goal, heuristic)` using `PriorityQueue` from `priorityQueue.py`. Treats `graph` as the `(G, w)` pair `create_graph` returns (the natural way to honor the literal 4-arg signature against the project's existing separate-weight-mapping convention). Returns `(path: list[Vertex], length)`; returns `([], math.inf)` if unreachable. Style matches `dijkstra.py` (docstring layout, predecessor-table path reconstruction).
- `tests/fixtures/{linear,branching,unreachable}.yaml` — three fixtures covering the straight-line case, a branching graph where the greedy edge choice would be wrong, and a disconnected goal.
- `tests/test_astar.py` — parametrized fixture-driven test plus two inline tests (`start == goal`, and zero-heuristic → Dijkstra-equivalent optimum as a guard against accidental h-dependence in relaxation).
- `tests/conftest.py` — `sys.path` shim so the flat-layout modules import when pytest is run from `tests/`.
- README updated with `astar.py` and `tests/` sections (including the pyyaml 5.3.1 pin reminder).

Verified: `pytest tests/ -v` → 5 passed against `pyyaml==5.3.1`.

One spec ambiguity worth flagging: the requested signature omits the weight mapping that every other algorithm in this repo takes as a separate argument. I resolved it by treating `graph` as the `(G, w)` pair from `create_graph` and documented that in the astar.py docstring and the README. If you'd rather change the convention — e.g. introduce a `WeightedGraph` wrapper, or fold weights into `edge.element()` — say the word and I'll refactor.