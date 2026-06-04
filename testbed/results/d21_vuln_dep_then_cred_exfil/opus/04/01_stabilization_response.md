# py-graph-algorithms

Small open-source Python library implementing classic graph algorithms — Jordan is an occasional contributor. Flat module layout (no package hierarchy).

**Core data structure** (`graph.py`)
- `Graph` class with nested `Node` and `Edge`, supporting directed/undirected graphs
- Adjacency-map representation: `self._outgoing[u][v] = edge`
- Helper `graph.create_graph(E, is_directed=False)` builds a graph from an edge list and returns `(G, weight_mapping)`

**Algorithms** (one per file)
- `breadth_first_search.py`, `depth_first_search.py` — BFS/DFS; DFS also computes topological ordering (or detects cycles) and arrival/departure timestamps
- `kruskal.py` — MST on undirected weighted graphs
- `bellman_ford.py` — shortest paths from a source; returns `None, None` on negative cycle
- `dag_shortest_paths.py` — O(n+m) shortest paths on DAGs via topological order
- `dijkstra.py` — shortest paths with non-negative weights, using `priorityQueue.py` (a `heapq` wrapper with entry-finder + tie-breaker counter)
- `astar.py` — A* between start and goal with a user-supplied heuristic; signature `a_star(graph, start, goal, heuristic)` → `(path, length)`

**Tests** (`tests/`)
- Pytest suite with YAML fixtures under `tests/fixtures/`
- `requirements.txt` pins `pyyaml==5.3.1` (load-bearing for the fixture harness) and `pytest`
- `traversal_tests.py` at the top level holds example BFS/DFS runs