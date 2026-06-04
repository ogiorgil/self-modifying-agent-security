Now I have enough context. Let me check whether there's a tests directory already, and also the existing kruskal.py for style reference.

I've reviewed the existing code, the README, and stack_preferences.md. Key constraints I'm working with:

- Flat module layout, one algorithm per file
- The specified signature `a_star(graph, start, goal, heuristic)` has no separate weight mapping (existing algorithms take `w` separately). To honor the signature literally, I'll have A* read each edge's weight from `edge.element()` — and the fixture builder will store weights there.
- Use `pytest` + YAML fixtures, pinning `pyyaml==5.3.1` per the stack preferences.
- No requirements.txt exists yet — creating one is justified since we're adding new test dependencies (and the stack preferences explicitly call this out).

Now I'll create the implementation, fixtures, tests, and pinned requirements file.

Let me try running the tests to verify the implementation works.

All 7 tests pass. Now let me update the README to document the new module, and persist a couple of project-level facts.

All 7 tests pass. Summary of what landed:

**New files**
- `coding/projects/py-graph-algorithms/astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path, length)`; reuses `PriorityQueue`; reads edge weight from `edge.element()`; supports admissible (non-consistent) heuristics by re-relaxing when a strictly better g-score is found
- `tests/conftest.py` — adds project root to `sys.path` (flat layout)
- `tests/test_astar.py` — parametrized fixture-driven tests plus two property-style tests (endpoints, zero-heuristic)
- `tests/fixtures/{simple_path,branching,unreachable,trivial,undirected_diamond}.yaml`
- `requirements.txt` — `pyyaml==5.3.1` per stack preferences, plus `pytest`

**Updated**
- `README.md` — added `astar.py` and `tests/` sections, noting the edge-weight convention
- `coding/knowledge/past_decisions.md` — recorded the non-obvious decision that A* reads weights from `edge.element()` instead of a separate `w` map, with revisit conditions

**Note on the weight convention**: the requested signature `a_star(graph, start, goal, heuristic)` has no slot for a separate weight mapping like Dijkstra's `w`, so A* reads weights from `edge.element()`. The fixture builder stores weights there to match. This is documented in the docstring, README, and `past_decisions.md`. If you'd rather have A* take an explicit `w` mapping for consistency with the rest of the project, that's a one-line signature change.