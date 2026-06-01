`py-graph` here is `coding/projects/py-graph-algorithms/`: a small, stdlib-only “classic graph algorithms” practice library built around a single adjacency-map `Graph` type.

- **Core data model:** `coding/projects/py-graph-algorithms/graph.py` defines `Graph(directed=...)` with nested `Graph.Vertex` and `Graph.Edge`, plus `create_graph(edges, is_directed=False)` which builds `(G, w)` where `w` maps `Edge -> weight` (weights default to `1` unless you pass `(u, v, w)` tuples).
- **Algorithms (one per file):**
  - Traversals: `breadth_first_search.py`, `depth_first_search.py`
  - Shortest paths: `dijkstra.py` (`Dijkstra(G, w, start_vertex)`), `bellman_ford.py` (`Bellman_Ford(G, w, start_vertex)`), `dag_shortest_paths.py` (`dag_shortest_paths(G, w, start_vertex)`), `astar.py` (`a_star(graph_or_(G,w), start, goal, heuristic)`)
  - MST: `kruskal.py` (`Kruskal(G, w)`)
- **Utility:** `priorityQueue.py` provides a heap-based `PriorityQueue` used by `dijkstra.py` and `astar.py`.
- **Tests:** small `pytest` suite (e.g. `coding/projects/py-graph-algorithms/test_astar.py`). Run from that directory with `python -m pytest`.

I also fixed a durable doc mismatch in `coding/AGENTS.md:16` (`Graph/Vertex/Edge` rather than `Graph/Node/Edge`).