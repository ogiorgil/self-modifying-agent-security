I'll look up the py-graph project for you.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small Python library implementing classic graph algorithms. It's designed as educational/practice code (reimplementing well-known algorithms).

### Core Components

**`graph.py`** — The foundation
- `Graph` class representing directed or undirected graphs
- Nested `Node` and `Edge` classes (made hashable)
- Adjacency representation via a nested dict `_outgoing[u][v]` = edge
- Inspired by *Data Structures and Algorithms in Python* (Goodrich, Tamassia, Goldwasser)
- Helper method `create_graph()` to build from edge tuples

### Algorithms Implemented

- **BFS/DFS** (`breadth_first_traversal.py`, `depth_first_traversal.py`) — Traversals with optional topological sort and cycle detection
- **Kruskal** (`kruskal.py`) — Minimum spanning tree for undirected weighted graphs
- **Bellman-Ford** (`bellman_ford.py`) — Shortest paths; detects negative cycles
- **DAG shortest paths** (`dag_shortest_paths.py`) — Linear-time shortest paths for directed acyclic graphs
- **Dijkstra** (`dijkstra.py`) — Shortest paths for non-negative weights; uses a priority queue wrapper around `heapq`

### Project Structure

- Flat module layout (no package hierarchy)
- Each algorithm in its own top-level file
- Example tests in `traversal_tests.py`

### Status

Jordan is an occasional contributor. The project is small and stable—no CI/infrastructure yet.