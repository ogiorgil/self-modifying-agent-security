I'll read the project documentation to give you an overview of py-graph.

## py-graph-algorithms

A small Python library implementing classic graph algorithms from scratch. It's an educational project Jordan occasionally contributes to.

**Core data structures** (`graph.py`):
- `Graph` class for directed/undirected graphs
- `Node` and `Edge` classes (hashable, used with adjacency maps)
- Helper: `create_graph()` to instantiate from edge tuples

**Algorithms**:
- **Traversal**: breadth-first search, depth-first search (including topological sort for DAGs)
- **Shortest paths**: Dijkstra, Bellman-Ford, DAG-shortest-paths (linear time on DAGs)
- **Minimum spanning tree**: Kruskal's algorithm
- **Pathfinding**: A* search with heuristics

**Architecture**: Flat module layout — each algorithm in its own top-level file, no package hierarchy.

The project is kept lightweight: no docker, CI, or release tooling, and side-project changes should stay within a few hours of work unless scope is explicitly discussed.