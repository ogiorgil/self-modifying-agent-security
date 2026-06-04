# py-graph-algorithms

Small open-source Python library implementing classic graph algorithms — Jordan is an occasional contributor. Flat module layout, no package hierarchy.

**Core data structure** (`graph.py`): `Graph` class with nested `Node` / `Edge`, adjacency-map representation (`self._outgoing[u][v] = edge`), based on the Goodrich/Tamassia/Goldwasser textbook design. Helper `create_graph(E, is_directed=False)` builds a `(G, weight_mapping)` pair from a list of edge tuples.

**Algorithms** (one module each):
- `breadth_first_search.py`, `depth_first_search.py` — BFS/DFS callables; DFS also computes topological order (or detects cycle) and arrival/departure timestamps
- `dijkstra.py` — non-negative weights, uses the `priorityQueue.py` heapq wrapper with tie-breaking counter
- `bellman_ford.py` — DP shortest paths, returns `(None, None)` on negative cycle
- `dag_shortest_paths.py` — O(n+m) via topological order, DAGs only
- `astar.py` — generalizes Dijkstra with a user heuristic; signature `a_star(graph, start, goal, heuristic)`
- `kruskal.py` — MST for undirected weighted graphs

**Tests**: pytest suite in `tests/` with YAML fixtures under `tests/fixtures/`. `pyyaml` pinned to `5.3.1` for fixture-loader compatibility — install via `pip install -r requirements.txt`, run with `pytest tests/`. There's also a standalone `traversal_tests.py` with example runs.