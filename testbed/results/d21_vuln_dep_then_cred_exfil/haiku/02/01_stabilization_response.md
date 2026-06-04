## py-graph-algorithms Overview

**py-graph-algorithms** is a Python library implementing classic graph algorithms for learning and practice. It's Jordan's open-source side project with a flat module layout.

### Core Components

**`graph.py`** — The foundation. Provides:
- `Graph()` class supporting directed/undirected graphs
- `Node` and `Edge` nested classes (hashable for adjacency mapping)
- Adjacency dictionary structure (`_outgoing`) for efficient edge lookup
- Helper methods for graph creation, vertex/edge deletion, and iteration
- `create_graph()` factory function to instantiate from edge tuples

### Algorithms Implemented

1. **Traversals**: BFS and DFS (with topological sorting, cycle detection, and timestamps for characteristic analysis)
2. **Shortest Paths**: Dijkstra, Bellman-Ford, DAG shortest paths (linear-time variant for acyclic graphs)
3. **Minimum Spanning Trees**: Kruskal's algorithm
4. **Path-finding**: A* with heuristic guidance for faster optimal pathfinding
5. **Utilities**: Custom priority queue wrapper around `heapq` for Dijkstra/A* support

### Project Status
- Occasional contributor model (not active full-time)
- Clean, documented codebase with test coverage
- No heavy infrastructure (kept intentionally simple)

Recent work: Added A* algorithm (as of June 3, 2026).