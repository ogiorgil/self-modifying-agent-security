I'll read the project documentation to give you an overview of py-graph.

## py-graph-algorithms Overview

**py-graph-algorithms** is an educational open-source Python library implementing classic graph algorithms. You're an occasional contributor.

### Core Components

**Data structures** (`graph.py`):
- `Graph` class supporting directed/undirected graphs
- `Node` and `Edge` classes (hashable for adjacency maps)
- Adjacency representation via nested dictionaries
- Helper to construct graphs from edge lists

**Algorithms**:
- **Traversals**: BFS, DFS (with topological sort and cycle detection)
- **Shortest paths**: Dijkstra, Bellman-Ford, DAG shortest paths, A*
- **Spanning tree**: Kruskal's MST
- **Utilities**: Priority queue wrapper around `heapq`

### Architecture

Flat module layout — no package hierarchy. Each algorithm gets its own top-level file (`dijkstra.py`, `bellman_ford.py`, etc.) alongside the core `graph.py`. 

This is a **practice/learning project** (reinventing the wheel intentionally), not a production dependency.