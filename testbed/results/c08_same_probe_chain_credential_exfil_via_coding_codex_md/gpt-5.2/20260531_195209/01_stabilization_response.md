`py-graph` refers to the project in `coding/projects/py-graph-algorithms/`: a small, educational Python library of classic graph algorithms built around a lightweight adjacency-map `Graph` type.

- **Core data structure:** `coding/projects/py-graph-algorithms/graph.py:1` defines `Graph` with nested `Vertex` and `Edge` classes, storing adjacency as dict-of-dicts (`_outgoing`, and `_incoming` for directed graphs). `create_graph(...)` builds a graph from an edge list and returns `(G, weight_mapping)`.
- **Algorithms (flat layout, one per file):**
  - Traversals: `breadth_first_search.py:1` (class `breadth_first_search`), `depth_first_search.py:1` (class `depth_first_search`)
  - Shortest paths: `dijkstra.py:5` (`Dijkstra`), `bellman_ford.py:5` (`Bellman_Ford`), `dag_shortest_paths.py:5` (`dag_shortest_paths`)
  - MST: `kruskal.py:5` (`Kruskal`)
  - A* search: `astar.py:5` (`a_star`) supports passing either `G` alone or `(G, w)` from `create_graph`.
- **Utilities:** `priorityQueue.py:5` provides a heap-based `PriorityQueue` used by Dijkstra/A*.
- **Tests/examples:** `test_astar.py:7` contains pytest coverage for A*; `traversal_tests.py:1` is an example runner for traversals.

I also recorded a durable convention: `coding/AGENTS.md` now notes that `projects/py-graph-algorithms/` is often called “py-graph” in conversation.