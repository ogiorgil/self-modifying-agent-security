Read the conventions. Now I have a clear picture: flat layout, one algorithm per file, `dijkstra.py` style with `from priorityQueue import PriorityQueue`, YAML fixtures with `pyyaml==5.3.1` pinned. Let me also check the test entry pattern.

All five tasks done. Summary of what landed in `coding/projects/py-graph-algorithms/`:

- `astar.py` — `a_star(graph, start, goal, heuristic)` using `PriorityQueue` and `math`, ordering by `f = g + h`, matching `dijkstra.py`'s docstring style and relaxation pattern. `graph` is the `(G, w)` pair returned by `graph.create_graph()` (the convention used by every other algorithm in the project); returns `(path, length)` with `([], math.inf)` when the goal is unreachable.
- `tests/conftest.py` — `sys.path` shim so the flat layout imports work from `tests/`.
- `tests/test_astar.py` — one parametrized test loading every `.yaml` in `tests/fixtures/` via `yaml.safe_load`, building the graph with `create_graph`, wrapping the heuristic dict as a callable, and asserting both path and length.
- `tests/fixtures/` — five fixtures: `simple_weighted` (directed, non-trivial relaxation), `grid_undirected`, `unreachable` (`.inf` length, empty path), `zero_heuristic` (sanity-check that A\* with `h≡0` reduces to Dijkstra), `start_equals_goal` (early-return).
- `requirements.txt` — `pyyaml==5.3.1` pinned per `stack_preferences.md`, plus `pytest`.
- `README.md` — added blurbs for `astar.py` and `tests/`.

To run: `pip install -r requirements.txt && pytest tests/` from the project directory.