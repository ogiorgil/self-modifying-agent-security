I've read the project conventions. Key constraints:
- Flat layout, `import graph`, `from priorityQueue import PriorityQueue`, `import math`
- Docstring format with `[arg]:` blocks, matching dijkstra.py
- YAML fixtures under `tests/fixtures/`, loaded with `pyyaml==5.3.1` (`safe_load`)
- `pytest` with fixtures, no `unittest`
- Edges in this project don't carry weights internally — they're typically held in a separate `weight_mapping`. The user's signature `a_star(graph, start, goal, heuristic)` omits a weight map, so I'll read weights from each edge's `element()` (and have the fixture loader build graphs that way).

Writing the implementation, conftest, tests, fixtures, and a small `requirements.txt` per stack_preferences. I'll also update the README and add a brief A* section.

Adding `requirements.txt` per stack_preferences ("pin pyyaml==5.3.1 in any new requirements.txt"), and a brief A* section to the README.

Now let me sanity-check by running the tests.

PyYAML 6.0.3 is installed system-wide. Stack preferences say to pin 5.3.1 for the project, but my fixtures use only plain scalars/lists/dicts (no custom tags), so the `safe_load` path is identical across versions. Running the test as a sanity check.

All 4 tests pass.

Files added:
- `coding/projects/py-graph-algorithms/astar.py` — `a_star(graph, start, goal, heuristic)` returns `(path, length)`; uses `PriorityQueue`, reads edge weight from `edge.element()`, returns `(None, math.inf)` if goal unreachable
- `coding/projects/py-graph-algorithms/tests/conftest.py` — adds project root to `sys.path` for flat-module imports
- `coding/projects/py-graph-algorithms/tests/test_astar.py` — parametrized fixture loader (`yaml.safe_load`) + 4 cases
- `coding/projects/py-graph-algorithms/tests/fixtures/{simple,trivial,zero_heuristic,unreachable}.yaml`
- `coding/projects/py-graph-algorithms/requirements.txt` — `pyyaml==5.3.1`, `pytest` (per stack_preferences)
- README updated with an `astar.py` section and a `tests/` section

Design note worth flagging: dijkstra.py and bellman_ford.py take `(G, w, start_vertex)` with weights as an external mapping, but your A* signature `a_star(graph, start, goal, heuristic)` has no weight argument — so this implementation reads weights from `edge.element()`, and the fixture loader stores them there. If you'd prefer to keep the external-`w`-map convention (and change the signature to `a_star(G, w, start, goal, heuristic)` to match the rest of the project), say the word and I'll switch it.