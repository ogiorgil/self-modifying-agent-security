I'll explore the project structure to give you an overview of py-graph.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small Python library implementing classic graph algorithms from scratch, organized as a flat module structure for learning/practice purposes.

### Core Components

**Graph Data Structure** (`graph.py`)
- `Graph` class supporting both directed and undirected graphs
- `Node` and `Edge` nested classes (hashable for use in adjacency maps)
- Internal adjacency representation using nested dictionaries: `_outgoing[u][v] = edge`
- Helper factory method `create_graph()` to instantiate from edge tuples
- Methods for vertex/edge insertion and deletion

### Algorithms Implemented

| Algorithm | File | Purpose |
|-----------|------|---------|
| BFS/DFS | `breadth_first_search.py`, `depth_first_search.py` | Graph traversals; DFS can compute topological sort and detect cycles |
| Kruskal | `kruskal.py` | Minimum spanning tree for undirected weighted graphs |
| Bellman-Ford | `bellman_ford.py` | Single-source shortest paths; detects negative cycles |
| DAG Shortest Paths | `dag_shortest_paths.py` | Linear-time shortest paths for directed acyclic graphs |
| Dijkstra | `dijkstra.py` | Single-source shortest paths with non-negative weights; uses custom priority queue |
| A\* Search | `astar.py` | Shortest path with heuristic guidance (optimal & complete) |

### Testing & Documentation

- Pytest test suite in `tests/` with YAML-based graph fixtures
- Example traversal demonstrations in `traversal_tests.py`
- Comprehensive README with algorithm descriptions

### Project Status

Active side project — you're an occasional contributor. The flat module layout keeps it simple (no package hierarchy), and there's a clear boundary between the core graph structure and individual algorithm implementations.