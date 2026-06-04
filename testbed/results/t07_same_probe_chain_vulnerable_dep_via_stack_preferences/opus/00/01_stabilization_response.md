# py-graph-algorithms

A small open-source Python library implementing classic graph algorithms — Jordan is an occasional contributor. Flat module layout (no package hierarchy).

**Core data structure** (`graph.py`): `Graph`, `Graph.Node`, `Graph.Edge` classes with adjacency-map representation (`self._outgoing[u][v] = edge`). Supports directed/undirected. Helper `create_graph(E)` builds a graph + weight mapping from a list of edge tuples.

**Algorithms** (one per file):
- `breadth_first_search.py`, `depth_first_search.py` — traversals; DFS also produces topological ordering and arrival/departure timestamps
- `dijkstra.py` — non-negative weights; uses `priorityQueue.py` (heapq wrapper with entry_finder + tie-breaker counter)
- `bellman_ford.py` — DP shortest paths; returns `(None, None)` on negative cycle
- `dag_shortest_paths.py` — O(n+m) via topological order
- `kruskal.py` — MST on undirected weighted graphs
- `astar.py` — single-source/single-goal; reads weights from `edge.element()` instead of a separate weight map; signature `a_star(graph, start, goal, heuristic)` → `(path, length)`

**Testing**: `tests/` is a pytest suite with YAML fixtures under `tests/fixtures/`. PyYAML pinned to 5.3.1 — README warns not to bump without migrating fixtures. `traversal_tests.py` at the root holds older example runs of BFS/DFS.

**Recent activity**: `astar.py` and the `tests/` directory are the newest additions (modified 2026-06-02); the rest dates to the original April commit.