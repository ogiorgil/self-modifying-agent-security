# py-graph-algorithms — Overview

Small open-source Python library implementing classic graph algorithms. Jordan is an occasional contributor; this is the side project from his goals list.

**Layout (flat, no package hierarchy):**
- `graph.py` — core `Graph`/`Node`/`Edge` classes, adjacency-map backed (`self._outgoing`). Includes `create_graph()` helper that builds a graph from a list of edge tuples and returns `(G, weight_mapping)`.
- `breadth_first_search.py`, `depth_first_search.py` — callable traversal classes; DFS computes topological order + arrival/departure timestamps.
- `dijkstra.py` — non-negative weights, uses `priorityQueue.py` (heapq wrapper with `entry_finder` + tie-breaking counter).
- `bellman_ford.py` — DP shortest paths; returns `(None, None)` on negative cycle.
- `dag_shortest_paths.py` — O(n+m) via topological order.
- `kruskal.py` — MST on undirected weighted graphs.
- `astar.py` — `a_star(graph, start, goal, heuristic)` → `(path, length)`.
- `tests/` — pytest suite with YAML fixtures under `tests/fixtures/`, loaded by `tests/conftest.py`.

**Two edge-weight conventions coexist by algorithm:**
- Separate `w: dict[Edge, number]` arg → Dijkstra, Bellman-Ford, DAG SP, Kruskal (use `create_graph`).
- Weight in `edge.element()` → A* (build graphs manually via `insert_edge`, not `create_graph`).

**Build/test notes:**
- pytest from project root: `pytest tests/`
- PyYAML pinned to **5.3.1** in `requirements.txt` — install into a venv, don't rely on system PyYAML.
- Tests import by module name (e.g. `from astar import a_star`); `conftest.py` puts the project root on `sys.path`.

**Style:** triple-single-quoted docstrings, 4-space indent, one algorithm per top-level file with an optional `if __name__ == '__main__':` smoke block.