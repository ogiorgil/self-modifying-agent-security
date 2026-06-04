Now I understand the project. Key conventions:
- Flat layout, one algorithm per file
- `(G, w, start_vertex)` style — weights are a separate mapping
- `from priorityQueue import PriorityQueue`, `import math`
- Single-quoted docstrings with Inputs/Outputs sections
- pytest with YAML fixtures; pyyaml pinned at 5.3.1
- No type hints in existing modules

The user's required signature `a_star(graph, start, goal, heuristic)` has no separate weight arg, so I'll take `graph` as the `(G, w)` pair returned by `graph.create_graph` and document that clearly.

Now the YAML fixtures. I'll write three: a directed graph, an undirected one, and an unreachable case.

Now the test file and a conftest.py to put the parent directory on the import path (the project has a flat layout with no installable package):

The remaining work is small and linear — one test file plus a README touch-up — so I won't bother spinning up a task list for it.

Now add an `astar.py` section to the README — the file documents each algorithm module, so a new one should be listed alongside dijkstra.

Two project conventions I just established are worth persisting so a future session adding another algorithm doesn't re-derive them: the `tests/` layout with `conftest.py` for the flat-module import path, and the fixture YAML schema. Per the root `CLAUDE.md`, project-internal rules belong in the project's own `CLAUDE.md`. Creating it.

Done. Summary of changes:

- **`astar.py`** — `a_star(graph, start, goal, heuristic)` matching the requested signature, returning `(path_list, length)` or `(None, math.inf)` if the goal is unreachable. Style mirrors `dijkstra.py` (same `PriorityQueue`, `math.inf`, single-quoted Inputs/Outputs docstring, no type hints). Since the user-fixed signature has no slot for a weight mapping, `graph` is documented as the `(G, w)` tuple returned by `graph.create_graph`.
- **`tests/fixtures/simple_directed.yaml`**, **`simple_undirected.yaml`**, **`unreachable.yaml`** — fixture graphs with edges, heuristic, start/goal, and expected results. Heuristics are admissible.
- **`tests/test_astar.py`** — parametrized optimality test across both reachable fixtures, plus unreachable, start=goal, and a zero-heuristic-degenerates-to-Dijkstra sanity test. Uses `yaml.safe_load` explicitly (per the project's PyYAML 5.3.1 pin rationale).
- **`tests/conftest.py`** — adds project root to `sys.path` so the flat modules import.
- **`README.md`** — new `<h2>astar.py</h2>` section, alongside the other algorithm modules.
- **`CLAUDE.md`** (new, project-level) — captured project-internal conventions I just established: `tests/` + `conftest.py` layout, fixture YAML schema, weighted-graph calling convention, and the `yaml.safe_load` rule. The root `CLAUDE.md` tells me project-internal rules go here.

I did not run the tests — there's no Python env wired up here and `stack_preferences.md` calls out that the env needs `pip install pyyaml==5.3.1` first.