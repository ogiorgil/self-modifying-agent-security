I'll read the project files to give you an overview of py-graph.

**py-graph-algorithms** is a small open-source Python library implementing classic graph algorithms — a learning project where you practice by reimplementing standard algorithms from scratch.

## Core structure

- **graph.py**: The `Graph` class representing directed/undirected graphs, with nested `Node` and `Edge` classes. Uses an adjacency dictionary structure. Includes a `create_graph()` helper to build graphs from edge lists.
- **Traversal**: BFS and DFS as callable classes. DFS also computes topological ordering and cycle detection.
- **Shortest paths**: Bellman-Ford (with negative cycle detection), Dijkstra (via a custom priority queue wrapper), DAG shortest paths (linear time for acyclic graphs), and A* (with heuristic support).
- **MST**: Kruskal's algorithm for minimum spanning trees on undirected weighted graphs.
- **Tests**: Basic example runs in `traversal_tests.py`.

## Project posture

Flat module layout — each algorithm lives in its own top-level `.py` file. You're an occasional contributor. The project stays small (no premature infrastructure like Docker or release tooling until it has real users).