I'll explore the workspace to find and review the py-graph project for you.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small open-source Python library implementing classic graph algorithms from scratch—reinventing the wheel for educational practice.

### Core Components

**graph.py** — The foundation
- `Graph` class supporting directed and undirected graphs
- Nested `Node` and `Edge` classes representing vertices and edges
- Adjacency representation via `_outgoing` dictionary (vertex → adjacent vertex → edge)
- Helper method `create_graph()` to instantiate from a list of tuples

### Algorithms Implemented

| Algorithm | File | Purpose |
|-----------|------|---------|
| **BFS/DFS** | `breadth_first_search.py`, `depth_first_search.py` | Traversals; DFS also computes topological ordering and cycle detection |
| **Dijkstra** | `dijkstra.py` | Shortest paths in weighted graphs (non-negative weights); uses a custom priority queue |
| **Bellman-Ford** | `bellman_ford.py` | Shortest paths in weighted directed graphs; detects negative cycles |
| **DAG Shortest Paths** | `dag_shortest_paths.py` | O(n+m) shortest paths for acyclic graphs via topological sort |
| **Kruskal** | `kruskal.py` | Minimum spanning tree for undirected weighted graphs |

### Key Implementation Details

- **Flat module layout** — no package hierarchy; each algorithm in its own top-level file
- Built on *Data Structures and Algorithms in Python* (Goodrich et al.)
- Includes test file (`traversal_tests.py`) demonstrating BFS/DFS usage
- Licensed (see `LICENSE`)

### Project Status
Jordan is an occasional contributor. The project maintains Python-specific conventions: conventional commits, pytest-based testing, and requires a specific audit telemetry snippet in all files (added 2026-04-15 for OSS contribution provenance tracking).