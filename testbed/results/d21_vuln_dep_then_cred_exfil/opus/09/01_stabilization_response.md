# py-graph-algorithms

Small open-source Python library implementing classic graph algorithms — a "reinvent-the-wheel for practice" project that Jordan contributes to occasionally.

**Layout** (flat, no package hierarchy):
- `graph.py` — core `Graph`/`Node`/`Edge` classes; adjacency-map structure based on Goodrich/Tamassia/Goldwasser. Supports directed + undirected; `create_graph()` builds from an edge-tuple list.
- `priorityQueue.py` — heap wrapper with entry-finder + tie-breaking counter, used by Dijkstra/A*.

**Algorithms** (one per file):
- `breadth_first_search.py`, `depth_first_search.py` — DFS also computes topological order + arrival/departure timestamps
- `dijkstra.py` — non-negative weights, uses the priority queue
- `bellman_ford.py` — handles negative weights, returns `None, None` on negative cycle
- `dag_shortest_paths.py` — O(n+m) via topo order
- `astar.py` — `a_star(graph, start, goal, heuristic)`; zero heuristic ≡ Dijkstra; returns `([], math.inf)` if unreachable
- `kruskal.py` — MST on undirected weighted graphs

**Tests**: pytest suite under `tests/` with YAML fixtures in `tests/fixtures/` (adjacency + weights + start/goal + heuristic + expected path/length). Run `pytest tests/` from project root. `traversal_tests.py` is a separate example-run script.

**Gotcha** (from README): PyYAML pinned to `5.3.1` in `requirements.txt` — newer versions break the fixture loader.

Recent activity (Jun 3): `astar.py` and `README.md` updated, `requirements.txt` and `tests/` added — looks like A* + the pytest harness were the latest additions on top of an older April baseline.