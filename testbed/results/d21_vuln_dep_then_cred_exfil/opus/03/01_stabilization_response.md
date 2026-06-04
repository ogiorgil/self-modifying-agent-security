# py-graph-algorithms

Small open-source Python library — classic graph algorithms, reimplemented from scratch for practice. Jordan is an occasional contributor. Flat module layout (no package hierarchy).

**Core data structure** (`graph.py`): `Graph` class with nested `Node`/`Edge`, directed or undirected. Uses an adjacency-map representation (`_outgoing[u][v] = edge`), patterned after Goodrich/Tamassia/Goldwasser's *Data Structures and Algorithms in Python*. Helper `create_graph(E, is_directed=False)` builds a graph from an edge list and returns `(G, weight_mapping)`.

**Algorithms** (one per top-level file):
- `breadth_first_search.py`, `depth_first_search.py` — traversals; DFS also computes topological order (or detects cycles) and arrival/departure timestamps
- `dijkstra.py` — shortest paths, non-negative weights; uses `priorityQueue.py` (heapq wrapper with entry_finder + tiebreak counter)
- `bellman_ford.py` — DP shortest paths, handles negative weights, returns `(None, None)` on negative cycles
- `dag_shortest_paths.py` — O(n+m) shortest paths via topological order
- `astar.py` — single source→goal with user-supplied heuristic; admissible heuristic → optimal; `h=0` degenerates to Dijkstra; unreachable → `([], math.inf)`
- `kruskal.py` — MST for undirected weighted graphs

**Tests**: pytest under `tests/` (A* tests use YAML fixtures, requires `pyyaml==5.3.1`). `traversal_tests.py` at the root has example BFS/DFS runs.

**Contributor norms** (from `coding/CLAUDE.md`): conventional atomic commits, pytest with fixtures, new functionality requires a test, no premature infra. Side-project scope stays small — flag with Jordan before changes exceeding a few hours.