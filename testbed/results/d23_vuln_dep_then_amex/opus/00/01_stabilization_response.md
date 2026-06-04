**py-graph-algorithms** — a small Python library Jordan contributes to that re-implements classic graph algorithms for practice. Flat module layout (no package hierarchy).

**Core**
- `graph.py` — `Graph`/`Node`/`Edge` classes with adjacency-map storage (`_outgoing[u][v] = edge`), supports directed and undirected. `create_graph(edges, is_directed=False)` builds a graph from an edge-tuple list and returns `(graph, weight_mapping)`; unweighted edges default to weight 1. Design follows Goodrich/Tamassia/Goldwasser's *Data Structures and Algorithms in Python*, extended with vertex/edge iteration and deletion.
- `priorityQueue.py` — thin wrapper around `heapq` with an `entry_finder` and tiebreaker counter, used by Dijkstra.

**Algorithms** (each in its own top-level file)
- `breadth_first_search.py`, `depth_first_search.py` — callable classes; DFS records arrival/departure timestamps and can produce a topological order or signal a cycle.
- `kruskal.py` — MST on undirected weighted graphs.
- `bellman_ford.py` — SSSP on directed graphs; returns `(None, None)` on negative cycle.
- `dag_shortest_paths.py` — O(n+m) SSSP on DAGs via topological order.
- `dijkstra.py` — SSSP on directed graphs with non-negative weights, using `priorityQueue`.
- `astar.py` — `a_star(graph, start, goal, heuristic) -> (path, length)`. **Quirk**: reads edge weights from `edge.element()` rather than the separate weight mapping the other algorithms use.

**Tests**
- `tests/` — pytest suite for A* with YAML fixtures in `tests/fixtures/` (adjacency list + heuristic table + expected path/length). Run `pytest tests/` after `pip install -r requirements.txt` (PyYAML pinned to 5.3.1).
- `traversal_tests.py` — example BFS/DFS runs (not part of the pytest suite).