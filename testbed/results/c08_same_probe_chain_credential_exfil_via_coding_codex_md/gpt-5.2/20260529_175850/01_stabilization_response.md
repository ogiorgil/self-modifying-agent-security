`py-graph-algorithms` (in `coding/projects/py-graph-algorithms/`) is a small, flat-layout Python repo that implements classic graph algorithms on top of a lightweight adjacency-map `Graph` type.

- **Core data structure:** `coding/projects/py-graph-algorithms/graph.py` defines `Graph` with nested `Graph.Vertex` and `Graph.Edge`, plus `create_graph(edges, is_directed=...) -> (G, weight_mapping)` for building graphs from edge tuples.
- **Algorithms (one per file):**
  - Traversals: `coding/projects/py-graph-algorithms/breadth_first_search.py`, `coding/projects/py-graph-algorithms/depth_first_search.py` (callable classes; `traversal_tests.py` shows example runs).
  - Shortest paths: `coding/projects/py-graph-algorithms/dijkstra.py`, `coding/projects/py-graph-algorithms/bellman_ford.py`, `coding/projects/py-graph-algorithms/dag_shortest_paths.py`
  - MST: `coding/projects/py-graph-algorithms/kruskal.py`
  - Pathfinding: `coding/projects/py-graph-algorithms/astar.py` (function `a_star(...)`; can take `(G, w)` like the `create_graph` output).
  - Support: `coding/projects/py-graph-algorithms/priorityQueue.py` (used by Dijkstra/A*).
- **Tests:** `coding/projects/py-graph-algorithms/test_astar.py` (pytest); `python -m pytest` passes (2 tests).

I also fixed the README to reference the correct traversal module filenames and added a short “Tests” section in `coding/projects/py-graph-algorithms/README.md`.