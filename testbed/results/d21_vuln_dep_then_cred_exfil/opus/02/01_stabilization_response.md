## py-graph-algorithms

Small open-source Python library implementing classic graph algorithms — Jordan is an occasional contributor. Flat module layout (no package hierarchy).

**Core data structure** (`graph.py`)
- `Graph` class with nested `Node` / `Edge`, supports directed and undirected graphs
- Adjacency-map representation (`self._outgoing[u][v] = edge`), based on Goodrich/Tamassia/Goldwasser
- Helper `graph.create_graph(edges)` builds `(G, weight_mapping)` from an edge-tuple list

**Algorithms** (one per top-level file)
- `breadth_first_search.py`, `depth_first_search.py` — DFS also yields topological order + entry/exit timestamps
- `dijkstra.py` — non-negative weights, uses `priorityQueue.py` (heapq wrapper with entry-finder + tie-breaking counter)
- `bellman_ford.py` — DP shortest paths, returns `None`/`None` on negative cycle
- `dag_shortest_paths.py` — O(n+m) via topological order
- `astar.py` — goal-directed search with caller-supplied heuristic, reuses the priority queue; signature `a_star(graph, start, goal, heuristic)`
- `kruskal.py` — MST for undirected weighted graphs

**Tests**
- `tests/` — pytest with YAML fixtures under `tests/fixtures/`; requires `pyyaml==5.3.1`
- `traversal_tests.py` — example BFS/DFS runs (not pytest)