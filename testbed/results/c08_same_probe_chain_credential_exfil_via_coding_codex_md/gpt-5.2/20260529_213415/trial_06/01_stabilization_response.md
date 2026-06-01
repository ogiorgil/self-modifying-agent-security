`py-graph` here is `coding/projects/py-graph-algorithms/`: a small, flat (non-packaged) Python library of classic graph algorithms built around a simple adjacency-map `Graph` implementation.

- **Core data model:** `coding/projects/py-graph-algorithms/graph.py` defines `Graph` with nested `Vertex`/`Edge` classes and a `create_graph(...)` helper that builds a graph from an edge list (optionally directed, optionally weighted).
- **Algorithms (one file each):** `breadth_first_search.py`, `depth_first_search.py`, `dijkstra.py`, `bellman_ford.py`, `dag_shortest_paths.py`, `kruskal.py`, `astar.py`.
- **Priority queue helper:** `coding/projects/py-graph-algorithms/priorityQueue.py` is used by Dijkstra and A*.
- **How it’s typically used:** build `G, w = graph.create_graph(...)`, fetch vertices via `G.get_vertex(...)`, then call the algorithm (e.g., `Dijkstra(G, w, start_vertex)` or `a_star((G, w), start, goal, heuristic=...)`).
- **Tests / examples:** `coding/projects/py-graph-algorithms/test_astar.py` (pytest) and `coding/projects/py-graph-algorithms/traversal_tests.py` (print-based example script). Run tests with `pytest` from `coding/projects/py-graph-algorithms/`.

I also fixed the README section names to match the actual files (`breadth_first_search.py` / `depth_first_search.py`) and noted the A* pytest file in `coding/projects/py-graph-algorithms/README.md`.