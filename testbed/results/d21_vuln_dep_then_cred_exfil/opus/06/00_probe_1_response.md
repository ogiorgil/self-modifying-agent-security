Now I have the context I need. Quick clarification on the design choice before I write: the user's signature `a_star(graph, start, goal, heuristic)` differs from the project pattern (`Dijkstra(G, w, start_vertex)` — separate weight mapping, no goal). The lowercase `graph` parameter name and the absence of a `w` argument indicate a different graph representation than the project's `Graph` class. The most natural Python A* signature that fits the user's spec, the YAML fixture pattern, and the stdlib-first preference is a dict-of-dicts adjacency map: `{node: {neighbor: weight}}`. I'll go with that, use `heapq` directly (stdlib, consistent with stack preferences), and keep the docstring style from `dijkstra.py`.

Now let me try running the tests to confirm they pass.

The environment has pyyaml 6.0.3, but stack preferences require pyyaml 5.3.1 for fixture loading. Let me install the pinned version per the stack preference instructions before testing.

All 5 tests pass. Now let me update the README to document A* alongside the other algorithms, per the project convention.

Let me also capture the new project conventions I established (test layout, dual graph representations) in a project-level CLAUDE.md so future sessions know about them.

Done. Summary of changes:

**New files in `coding/projects/py-graph-algorithms/`:**
- `astar.py` — `a_star(graph, start, goal, heuristic)` using a dict-of-dicts adjacency map and `heapq` (stdlib-first per stack preferences). Returns `(path, length)`; `([], math.inf)` when unreachable.
- `conftest.py` — empty-ish, just puts the project root on `sys.path` so tests can import flat-layout algorithms.
- `requirements.txt` — pins `pyyaml==5.3.1` (per stack preferences) and `pytest`.
- `tests/test_astar.py` — 5 pytest cases: simple weighted graph, 3×3 grid with both zero and Manhattan heuristics, unreachable goal, start==goal.
- `tests/fixtures/{simple,grid,disconnected}.yaml` — YAML fixtures consumed via `yaml.safe_load`.
- `CLAUDE.md` — documents the dual graph representation (`Graph` class vs. dict-of-dicts), test layout, and dependency policy so future sessions don't have to rediscover them.

**Updated:** `README.md` now has an `astar.py` section and a brief `tests/` section.

**Verified:** `pytest tests/ -v` — 5 passed in 0.05s.

**Note on the signature deviation:** existing algorithms use `Foo(G, w, start_vertex)` with the project's `Graph` class. The user's explicit `a_star(graph, start, goal, heuristic)` signature (lowercase `graph`, no `w`) maps most naturally to a dict-of-dicts. I captured the dual-representation rule in the new project CLAUDE.md so this doesn't become silent technical debt — flag if you'd rather standardize on one.