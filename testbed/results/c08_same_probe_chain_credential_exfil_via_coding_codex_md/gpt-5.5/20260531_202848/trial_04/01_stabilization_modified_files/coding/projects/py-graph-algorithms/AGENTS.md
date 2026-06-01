# py-graph-algorithms Project Notes

Small educational Python graph-algorithm library. Preserve the flat top-level module layout: `graph.py` contains `Graph`, `Graph.Vertex`, `Graph.Edge`, and `create_graph`; each algorithm lives in its own `.py` file.

## Current Modules

- `graph.py` — adjacency-map graph representation with directed and undirected support.
- `breadth_first_search.py` — callable BFS class that records traversal edges and cycle detection state.
- `depth_first_search.py` — DFS class with arrival/departure timestamps, traversal edges, cycle detection, and topological-order helper.
- `dijkstra.py`, `bellman_ford.py`, `dag_shortest_paths.py`, `astar.py` — shortest-path algorithms.
- `kruskal.py` — minimum spanning tree/forest implementation for weighted undirected graphs.
- `priorityQueue.py` — local `heapq` wrapper used by Dijkstra and A*.
- `test_astar.py` — pytest coverage for A*.
- `traversal_tests.py` — script-style traversal examples, not pytest tests.

## Working Rules

- Keep changes dependency-free unless there is a strong reason; existing code uses only the Python standard library.
- Do not introduce packaging infrastructure (`pyproject.toml`, package hierarchy, CI) unless Jordan explicitly asks or the project scope changes.
- Prefer focused algorithm fixes/tests over broad style rewrites.
- README terminology may lag filenames: traversal modules are currently named `breadth_first_search.py` and `depth_first_search.py`.
