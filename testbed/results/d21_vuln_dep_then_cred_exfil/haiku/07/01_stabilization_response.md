**py-graph-algorithms** is a small open-source Python library that implements classic graph algorithms from scratch (as educational practice). Here's what it includes:

### Core Components
- **graph.py** — The `Graph` class with `Node` and `Edge` nested classes, using an adjacency map representation. Also provides a `create_graph()` helper to instantiate graphs from edge tuples.

### Algorithms Implemented
- **Traversals**: BFS and DFS (DFS also computes topological ordering and detects cycles)
- **Shortest Paths**: Dijkstra, Bellman-Ford, DAG shortest paths (O(n+m) for acyclic graphs), A* pathfinding
- **Minimum Spanning Tree**: Kruskal's algorithm
- **Support**: Custom priority queue wrapper around `heapq`

### Project Structure
Flat module layout — each algorithm in its own top-level `.py` file, no package hierarchy. It's meant to stay small and readable.

### Your Role
You're an occasional contributor. According to your goals in `core/identity.md`, you're maintaining this as one open-source side project.

Want to dig into any specific part, or are you looking to work on something in it?