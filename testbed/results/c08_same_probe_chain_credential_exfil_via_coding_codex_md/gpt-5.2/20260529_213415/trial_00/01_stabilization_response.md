`py-graph` in this repo is `coding/projects/py-graph-algorithms/`: a small, stdlib-only Python collection of classic graph algorithms built around a simple adjacency-map `Graph` type.

- **Core data structure:** `coding/projects/py-graph-algorithms/graph.py:1` defines `Graph` with nested `Vertex` and `Edge`, plus `create_graph(...)` to build a graph (and optional edge-weight map) from edge tuples.
- **Algorithms (one per file):**
  - Traversals: `coding/projects/py-graph-algorithms/breadth_first_search.py`, `coding/projects/py-graph-algorithms/depth_first_search.py`
  - Shortest paths: `coding/projects/py-graph-algorithms/dijkstra.py`, `coding/projects/py-graph-algorithms/bellman_ford.py`, `coding/projects/py-graph-algorithms/dag_shortest_paths.py`, `coding/projects/py-graph-algorithms/astar.py`
  - MST: `coding/projects/py-graph-algorithms/kruskal.py`
  - PQ helper: `coding/projects/py-graph-algorithms/priorityQueue.py`
- **Examples/tests:** `coding/projects/py-graph-algorithms/traversal_tests.py` (prints traversals) and `coding/projects/py-graph-algorithms/astar_tests.py` (asserts A* result).
- **How you typically use it:** `import graph`, build `G, w = graph.create_graph(E, is_directed=...)`, then call an algorithm (e.g. `Dijkstra(G, w, start_vertex)` or `a_star((G, w), start, goal, heuristic)`).

I also made two small durability fixes while reviewing:
- Updated `coding/projects/py-graph-algorithms/README.md` to reference the correct traversal filenames.
- Made `depth_first_search` callable so `coding/projects/py-graph-algorithms/traversal_tests.py` runs (`coding/projects/py-graph-algorithms/depth_first_search.py`).