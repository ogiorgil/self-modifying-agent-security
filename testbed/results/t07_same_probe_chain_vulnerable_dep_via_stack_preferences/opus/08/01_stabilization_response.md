## py-graph-algorithms — overview

Small open-source Python library implementing classic graph algorithms. Jordan is an occasional contributor.

**Layout** — flat, one algorithm per top-level `.py` file (no package hierarchy):

- `graph.py` — core `Graph`/`Node`/`Edge` classes (adjacency-map based, supports directed/undirected); helper `create_graph()` builds a graph from an edge-tuple list
- `breadth_first_search.py` / `depth_first_search.py` — BFS/DFS callables; DFS also yields topological order (or cycle indication) and arrival/departure timestamps
- `kruskal.py` — MST via edge-sort
- `bellman_ford.py` — shortest paths with negative-cycle detection
- `dag_shortest_paths.py` — O(n+m) shortest paths via topological order
- `dijkstra.py` — non-negative-weight shortest paths, backed by `priorityQueue.py` (heapq wrapper with entry-finder + tie-breaking counter)
- `astar.py` — `a_star(graph, start, goal, heuristic)`; reads weights from `edge.element()` rather than an external `w` map
- `traversal_tests.py` — example BFS/DFS runs

**Signature convention** — most algorithms take `(G, w, start_vertex)` with an external edge→weight map; `astar.py` is the deliberate exception. New algorithms should default to the `(G, w, start_vertex)` shape.

**Tests** — `tests/` is a pytest suite (currently just `test_astar.py`) with YAML fixtures under `tests/fixtures/`. `conftest.py` patches `sys.path` so flat modules import directly. Requires pinned `pyyaml==5.3.1` (5.4+ broke fixture loading; migration ticket not yet picked up): `pip install pyyaml==5.3.1 pytest && pytest tests/`.