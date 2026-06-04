I'll read the core files and then look at the py-graph project for you.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small open-source Python library implementing classic graph algorithms for educational purposes. It's structured as a flat module (no package hierarchy) with the core data structures in `graph.py` and each algorithm in its own top-level file.

### Core Components

**`graph.py`** — Data structures:
- `Graph` class supporting directed/undirected graphs
- Nested `Node` and `Edge` classes (hashable)
- Adjacency representation via nested dictionaries (`_outgoing`)
- Helper `create_graph()` factory from edge lists

### Implemented Algorithms

- **`breadth_first_traversal.py` / `depth_first_traversal.py`** — BFS and DFS with topological sort (DFS), cycle detection, and arrival/departure timestamps
- **`dijkstra.py`** — Shortest paths (non-negative weights) using a custom priority queue wrapper around `heapq`
- **`bellman_ford.py`** — Shortest paths (handles negative weights, detects negative cycles)
- **`dag_shortest_paths.py`** — Linear-time shortest paths for DAGs via topological ordering
- **`kruskal.py`** — Minimum spanning tree for undirected graphs
- **`priorityQueue.py`** — Priority queue utility with entry finder and tiebreaker

### Status
You're an occasional contributor. The project stays small and focuses on algorithmic clarity over infrastructure — no Docker, CI, or release tooling.