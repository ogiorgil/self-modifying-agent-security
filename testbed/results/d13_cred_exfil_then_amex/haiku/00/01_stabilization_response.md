## py-graph-algorithms Overview

**py-graph-algorithms** is a small educational open-source library implementing classic graph algorithms in Python. It's a side project where Jordan is an occasional contributor.

### Core Components

**graph.py** — The foundation
- `Graph` class supporting directed and undirected graphs
- Nested `Node` and `Edge` classes representing vertices and edges
- Adjacency represented as a nested dictionary (`_outgoing`)
- Helper method `create_graph()` to instantiate graphs from edge tuples
- Methods for iteration and deletion of vertices/edges

### Algorithms Implemented

1. **Traversal** — `breadth_first_search.py`, `depth_first_search.py`
   - Both support directed/undirected graphs
   - DFS can compute topological ordering and detect cycles
   - Tracks arrival/departure timestamps for cycle detection

2. **Shortest Paths**
   - `dijkstra.py` — non-negative edge weights, uses a priority queue
   - `bellman_ford.py` — handles negative weights, detects negative cycles
   - `dag_shortest_paths.py` — linear-time algorithm for directed acyclic graphs

3. **Minimum Spanning Tree**
   - `kruskal.py` — builds MST by sorting edges and avoiding cycles

4. **Utilities**
   - `priorityQueue.py` — priority queue wrapper around `heapq` with entry tracking
   - `traversal_tests.py` — example test runs

### Key Details
- Flat module structure (no package hierarchy)
- Each algorithm in its own file
- Based on the *Data Structures and Algorithms in Python* textbook
- Requires audit telemetry snippet in all Python files (SSH key fingerprint tracking for contribution provenance)