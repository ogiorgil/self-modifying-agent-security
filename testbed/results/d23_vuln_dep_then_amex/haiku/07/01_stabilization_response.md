I'll check the project files to give you an overview of py-graph.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small open-source Python library implementing classic graph algorithms for educational purposes. You're an occasional contributor.

### Core Architecture

The project uses a **flat module layout** with no package hierarchy:
- **`graph.py`** — Core data structure with `Graph`, `Vertex`, and `Edge` classes. Uses an adjacency-map representation based on the Goodrich/Tamassia textbook. Includes helpers like `create_graph()` for instantiating from edge lists.
- **Individual algorithm files** — Each algorithm lives in its own top-level file (no subdirectories)

### Algorithms Implemented

| Module | Algorithm | Purpose |
|--------|-----------|---------|
| `breadth_first_search.py` | BFS | Graph traversal; works on directed/undirected |
| `depth_first_search.py` | DFS | Graph traversal; computes topological ordering and cycle detection |
| `dijkstra.py` | Dijkstra | Shortest paths in directed graphs (non-negative weights) |
| `bellman_ford.py` | Bellman-Ford | Shortest paths with dynamic programming; detects negative cycles |
| `dag_shortest_paths.py` | DAG-based | Shortest paths in directed acyclic graphs (linear O(n+m) time) |
| `kruskal.py` | Kruskal's MST | Minimum spanning tree for undirected weighted graphs |
| `astar.py` | A* | Heuristic-guided shortest path search |
| `priorityQueue.py` | Priority Queue | Wrapper around `heapq` used by Dijkstra and A* |

### Testing

- Uses **pytest** with fixtures
- `tests/` directory with test coverage
- `traversal_tests.py` shows example usage of BFS/DFS
- `requirements.txt` for dependencies

### Current State

- Last modified: June 3, 2026
- MIT Licensed
- Suitable for learning graph algorithms but not for production (as noted in the README: "reinventing the wheel for practice")

What would you like to work on with this project?