The “py-graph” project in this repo is `coding/projects/py-graph-algorithms/`: a small, flat (no package hierarchy) collection of classic graph algorithms implemented in Python.

- **Core data structure:** `coding/projects/py-graph-algorithms/graph.py` defines `Graph` with nested `Graph.Vertex` / `Graph.Edge`, backed by an adjacency-map (`_outgoing`, and `_incoming` for directed graphs). The helper `create_graph(edges, is_directed=False)` builds a graph from `(u, v)` or `(u, v, w)` tuples and returns `(G, weight_mapping)`.
- **Algorithms (one file each):**
  - Traversals: `coding/projects/py-graph-algorithms/breadth_first_search.py`, `coding/projects/py-graph-algorithms/depth_first_search.py`
  - Shortest paths: `coding/projects/py-graph-algorithms/dijkstra.py`, `coding/projects/py-graph-algorithms/bellman_ford.py`, `coding/projects/py-graph-algorithms/dag_shortest_paths.py`, `coding/projects/py-graph-algorithms/astar.py`
  - MST: `coding/projects/py-graph-algorithms/kruskal.py`
  - Utility: `coding/projects/py-graph-algorithms/priorityQueue.py` (heap-based PQ used by Dijkstra/A*)
- **Examples/tests:**
  - Example script: `coding/projects/py-graph-algorithms/traversal_tests.py`
  - pytest tests: `coding/projects/py-graph-algorithms/test_astar.py` (run with `pytest` from the project directory)

I also updated `coding/projects/py-graph-algorithms/README.md` to match the actual filenames/classes and to mention how to run the tests.