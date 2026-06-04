I'll explore the workspace to find the py-graph project and give you an overview.

## py-graph-algorithms Overview

A small open-source Python library implementing classic graph algorithms for educational purposes. It's a flat-module project (no package hierarchy) where `graph.py` holds the core data structures and each algorithm lives in its own top-level file.

**Core Data Structures** (`graph.py`):
- `Graph` class supporting directed or undirected graphs
- Nested `Node` and `Edge` classes (hashable for use in adjacency maps)
- Adjacency representation using nested dictionaries (`_outgoing`)
- Helper method `create_graph()` to instantiate from edge tuples

**Algorithms Implemented**:
- **Traversals**: BFS and DFS (DFS also computes topological ordering and cycle detection)
- **Shortest Paths**: Dijkstra, Bellman-Ford (handles negative weights), DAG shortest paths (linear time), A* (with heuristic)
- **Minimum Spanning Tree**: Kruskal's algorithm
- **Utilities**: Priority queue wrapper around `heapq` with entry finder and tie-breaking

**Testing**:
- pytest-based with YAML fixtures in `tests/fixtures/`
- Uses `pyyaml==5.3.1` for consistent fixture loading

**Project Status**: You're an occasional contributor. The project is simple and stable—no premature infrastructure (no Docker, CI, or release tooling).