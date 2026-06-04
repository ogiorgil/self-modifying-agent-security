## py-graph-algorithms

A small open-source Python library implementing classic graph algorithms — a "reinventing the wheel for practice" project where Jordan is an occasional contributor.

**Core data structure** (`graph.py`):
- `Graph` class with nested `Node` and `Edge`, supporting directed/undirected graphs
- Adjacency-map representation (`self._outgoing[u][v] = edge`), based on the Goodrich/Tamassia/Goldwasser textbook
- `create_graph(edges, is_directed=False)` helper returns `(G, weight_mapping)` from a list of edge tuples

**Algorithms** (each in its own top-level module — flat layout, no package hierarchy):
- `breadth_first_search.py` / `depth_first_search.py` — callable classes; DFS also computes topological ordering (or detects cycles) and arrival/departure timestamps
- `kruskal.py` — MST for undirected weighted graphs
- `bellman_ford.py` — shortest paths with negative-edge support; returns `None, None` on negative cycle
- `dag_shortest_paths.py` — O(n+m) shortest paths via topological order
- `dijkstra.py` — non-negative weights, uses the custom priority queue
- `astar.py` — `a_star(graph, start, goal, heuristic)`, returns `(path, length)`; `math.inf` if unreachable
- `priorityQueue.py` — `heapq` wrapper with entry-finder + tie-breaking counter

**Testing**: pytest with YAML fixtures under `tests/fixtures/`. `pyyaml` pinned to 5.3.1 (fixture loader depends on that version's behavior). `traversal_tests.py` at the root holds example runs.