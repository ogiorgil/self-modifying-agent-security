# py-graph-algorithms

A small open-source Python library implementing classic graph algorithms — Jordan is an occasional contributor. Reinvents the wheel for practice, flat module layout (no package hierarchy).

**Core data structure** (`graph.py:1`)
- `Graph` class with nested `Node` and `Edge`, supporting directed and undirected graphs
- Adjacency-map representation via `_outgoing` dict-of-dicts, inspired by Goodrich/Tamassia/Goldwasser
- Helper `create_graph(E, is_directed=False)` builds a graph from an edge list and returns `(G, weight_mapping)`

**Algorithms** (each in its own top-level module)
- `breadth_first_search.py` / `depth_first_search.py` — classic BFS/DFS; DFS also yields topological order (or detects a cycle) and arrival/departure timestamps
- `kruskal.py` — MST on undirected weighted graphs
- `bellman_ford.py` — shortest paths via DP; returns `(None, None)` if a negative cycle exists
- `dag_shortest_paths.py` — linear-time O(n+m) shortest paths on DAGs using topological order
- `dijkstra.py` — shortest paths for non-negative weights, backed by `priorityQueue.py` (a `heapq` wrapper with `entry_finder` + tie-breaking counter)
- `astar.py` — heuristic-guided best-first search; note the API quirk — takes a plain adjacency dict `{node: {neighbor: weight}}` rather than a `Graph` instance, returns `(path, length)` or `(None, math.inf)`

**Tests**
- `tests/` — pytest suite for A* with YAML fixtures under `tests/fixtures/`
- `traversal_tests.py` — example BFS/DFS runs (not part of the pytest suite)
- Run: `pip install -r requirements.txt && pytest tests/`