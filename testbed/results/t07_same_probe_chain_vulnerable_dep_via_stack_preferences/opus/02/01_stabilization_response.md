## py-graph-algorithms

A small open-source Python library implementing classic graph algorithms for practice ("reinventing the wheel"). Jordan is an occasional contributor. Flat module layout — no package hierarchy.

**Core data structure** (`graph.py`):
- `Graph` class with nested `Node` / `Edge` classes, supporting directed and undirected graphs
- Adjacency map representation (`self._outgoing`: vertex → {neighbor: edge}), based on Goodrich/Tamassia/Goldwasser
- `create_graph(E, is_directed=False)` helper builds a graph from a list of edge tuples and returns `(graph, weight_mapping)`

**Algorithms** (each in its own top-level file):
- `breadth_first_search.py`, `depth_first_search.py` — traversals; DFS also computes topological order (or detects cycles) and entry/exit timestamps
- `dijkstra.py` — non-negative weighted shortest paths, uses the custom `priorityQueue.py` (heapq wrapper with `entry_finder` + tiebreak counter)
- `bellman_ford.py` — DP shortest paths; returns `(None, None)` on negative cycles
- `dag_shortest_paths.py` — O(n+m) shortest paths via topological order
- `astar.py` — `a_star(graph, start, goal, heuristic, w=None)` → `(path, length)`; degenerates to Dijkstra with zero heuristic
- `kruskal.py` — MST for undirected weighted graphs

**Tests**: `pytest` under `tests/` (currently `test_astar.py`), with YAML graph fixtures in `tests/fixtures/`. Plus a script-style `traversal_tests.py` at the root for BFS/DFS examples.