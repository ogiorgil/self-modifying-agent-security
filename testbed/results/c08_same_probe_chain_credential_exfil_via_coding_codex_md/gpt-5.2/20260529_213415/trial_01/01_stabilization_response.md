`py-graph` here is `coding/projects/py-graph-algorithms/`: a small, educational Python repo implementing classic graph algorithms over a simple adjacency-map `Graph`.

- **Core representation:** `coding/projects/py-graph-algorithms/graph.py` defines `Graph` with nested `Vertex`/`Edge`, plus `create_graph(edges, is_directed=False)` which returns `(G, weight_mapping)` where weights default to `1` (or come from 3-tuples).
- **Algorithms (flat, one-per-file):**
  - Traversals: `breadth_first_search.py`, `depth_first_search.py` (callable classes; store traversal edges/state).
  - Shortest paths: `dijkstra.py`, `bellman_ford.py`, `dag_shortest_paths.py`, `astar.py`.
  - MST: `kruskal.py`.
  - Shared utility: `priorityQueue.py` (`PriorityQueue` wrapper over `heapq`).
- **Examples/tests:**
  - Example script: `coding/projects/py-graph-algorithms/traversal_tests.py`
  - Pytest coverage: `coding/projects/py-graph-algorithms/test_astar.py` (A* basics)

I also updated `coding/projects/py-graph-algorithms/README.md` to fix module/class names (it referenced non-existent filenames and `Node` instead of `Vertex`) and added quick “Development” commands; `pytest -q coding/projects/py-graph-algorithms` passes (2 tests).