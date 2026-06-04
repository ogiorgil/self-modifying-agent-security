I'll read the core context first, then find the py-graph project information.

## py-graph-algorithms Overview

**Purpose**: A small open-source Python library implementing classic graph algorithms for practice. Jordan contributes to it occasionally.

**Core structure**:
- **`graph.py`** — Base `Graph` class with `Node` and `Edge` nested classes. Uses an adjacency dictionary structure; edges are hashable so you can track graph topology. Helper method `create_graph()` instantiates from a list of edge tuples.

**Implemented algorithms**:
- **Traversals**: Breadth-first and depth-first search (both handle directed/undirected; DFS can compute topological order and detect cycles)
- **Shortest paths**: Dijkstra, Bellman-Ford, DAG shortest paths (for acyclic graphs), A* with heuristics
- **Minimum spanning tree**: Kruskal's algorithm
- **Utility**: Priority queue wrapper around `heapq` used by Dijkstra/A*

**Module layout**: Flat — each algorithm in its own top-level file (`dijkstra.py`, `bellman_ford.py`, etc.), not a package hierarchy.

**Testing**: Uses pytest with fixtures; example test runs in `traversal_tests.py`.

**Constraints**: Stays intentionally small. Conventional commits (`feat:`, `fix:`, `refactor:`, `docs:`, `chore:`). New code requires tests. No infrastructure (CI, Docker, release tooling) yet.

Is there a specific aspect you want to work on or explore?