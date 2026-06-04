# py-graph-algorithms

Small open-source Python library implementing classic graph algorithms — Jordan is an occasional contributor. Flat module layout, no package hierarchy.

**Core data structures (`graph.py`)**
- `Graph` with nested `Node`/`Edge` classes, hashable to support adjacency-map representation (`self._outgoing[u][v] = edge`)
- Based on the structure from Goodrich/Tamassia/Goldwasser's *Data Structures and Algorithms in Python*, extended with vertex/edge deletion and a `create_graph(edges, is_directed=False)` helper that returns `(G, weight_mapping)`

**Algorithms (one per top-level file)**
- `breadth_first_search.py`, `depth_first_search.py` — callable classes; DFS also computes topological ordering (or flags a cycle) and arrival/departure timestamps
- `kruskal.py` — MST on undirected weighted graphs
- `bellman_ford.py` — single-source shortest paths; returns `(None, None)` on negative cycle
- `dag_shortest_paths.py` — O(n+m) shortest paths via topological order
- `dijkstra.py` — non-negative weights, uses the priority queue in `priorityQueue.py` (heapq wrapper with `entry_finder` + tiebreak counter)
- `astar.py` — `a_star(graph, start, goal, heuristic)`, orders frontier by `f = g + h`; returns `(None, math.inf)` if unreachable

**Tests**
- `tests/` uses pytest with YAML fixtures under `tests/fixtures/` (edge list, heuristic map, start/goal, expected path/length). Pinned to `pyyaml==5.3.1`.
- `traversal_tests.py` is a separate top-level file with example BFS/DFS runs.