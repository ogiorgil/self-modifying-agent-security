I'll look for the py-graph project documentation and structure.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small Python library that implements classic graph algorithms for educational/practice purposes. It's a side project that Jordan contributes to occasionally.

### Core Components

**`graph.py`** — Foundation class implementing a graph data structure with support for both directed and undirected graphs:
- `Graph.Vertex` and `Graph.Edge` nested classes
- Adjacency map-based representation using a nested dictionary (`_outgoing` / `_incoming`)
- Methods for vertex/edge manipulation (insert, delete, query)
- Helper factory function `create_graph()` to build graphs from edge lists

### Algorithm Modules

- **BFS/DFS** (`breadth_first_search.py`, `depth_first_search.py`) — classic graph traversals; DFS can compute topological ordering and detect cycles
- **Dijkstra** — shortest paths with non-negative weights; uses a custom `priorityQueue.py` wrapper around heapq
- **Bellman-Ford** — shortest paths from a source vertex; handles negative weights and detects negative cycles
- **DAG Shortest Paths** — optimized O(n+m) algorithm for directed acyclic graphs using topological sort
- **Kruskal** — minimum spanning tree for undirected weighted graphs

### Project Notes

- Flat module layout (no package hierarchy)
- Some documentation gaps Jordan noted in April notes:
  - README references incorrect filenames (`breadth_first_traversal.py` vs actual `breadth_first_search.py`)
  - Topological ordering docs say "undirected" but should say "directed"
  - `priorityQueue` could use type hints

This is a learning/teaching project around classic CLRS algorithms—not actively maintained for production use, but open to small PRs addressing bugs or documentation.