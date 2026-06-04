## py-graph-algorithms

Small open-source Python library implementing classic graph algorithms. Jordan is an occasional contributor. Flat module layout — no package hierarchy.

**Core data structure** (`graph.py`)
- `Graph` class with nested `Node`/`Edge` (hashable), backed by an adjacency-map `self._outgoing`
- Supports directed and undirected graphs
- `create_graph(edges, is_directed=False)` helper builds a graph from a tuple list and returns `(G, weight_mapping)`
- Design follows Goodrich/Tamassia/Goldwasser's *Data Structures and Algorithms in Python*

**Algorithms** (one per top-level file)
- `breadth_first_search.py`, `depth_first_search.py` — DFS also computes topological order + arrival/departure timestamps
- `kruskal.py` — MST on undirected weighted graphs
- `bellman_ford.py` — shortest paths with negative-cycle detection
- `dag_shortest_paths.py` — linear-time shortest paths via topological order
- `dijkstra.py` — uses `priorityQueue.py` (heapq wrapper with entry-finder + tie-breaking counter)
- `astar.py` — A* on directed/undirected graphs with non-negative weights; returns `(path, length)` or `(None, math.inf)` if unreachable

**Tests**
- `tests/` — pytest suite with YAML fixtures in `tests/fixtures/` (adjacency lists, heuristic tables, expected paths)
- `traversal_tests.py` — legacy example runs of BFS/DFS
- Run with `pip install -r requirements.txt && pytest tests/`

Recent activity (Jun 2): `astar.py` and the `tests/` suite were added; README updated.