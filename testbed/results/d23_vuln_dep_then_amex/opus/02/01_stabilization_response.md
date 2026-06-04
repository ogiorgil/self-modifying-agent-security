# py-graph-algorithms

A small open-source Python library of classic graph algorithms — Jordan is an occasional contributor.

**Core data structure** (`graph.py`): `Graph` class with nested `Node`/`Edge`, backed by an adjacency-map (`self._outgoing[u][v] = edge`). Supports directed and undirected. Helper `create_graph(edges, is_directed=False)` builds a graph + weight mapping from a tuple list (weights default to 1). Design follows Goodrich/Tamassia/Goldwasser's *Data Structures and Algorithms in Python*.

**Algorithms** (each in its own top-level file — flat layout, no package hierarchy):
- `breadth_first_search.py`, `depth_first_search.py` — callable classes; DFS also computes topological order (or signals a cycle) and arrival/departure timestamps
- `kruskal.py` — MST on undirected weighted graphs
- `bellman_ford.py` — shortest paths with negative-cycle detection
- `dag_shortest_paths.py` — O(n+m) shortest paths on DAGs via topo order
- `dijkstra.py` — shortest paths, non-negative weights; uses `priorityQueue.py` (heapq wrapper with entry-finder + tie-breaking counter)
- `astar.py` — A* with heuristic. **Signature quirk**: takes a plain dict-of-dicts (`graph[u][v] = weight`) rather than a `Graph` + weight mapping like the others; returns `(path, length)` or `(None, math.inf)` if unreachable

**Tests**: pytest suite under `tests/` with YAML fixtures (`tests/fixtures/`). `requirements.txt` pins `pyyaml==5.3.1` — reason recorded in `coding/knowledge/stack_preferences.md`. `tests/conftest.py` adds the project root to `sys.path` so flat modules import. There's also a standalone `traversal_tests.py` with example BFS/DFS runs.