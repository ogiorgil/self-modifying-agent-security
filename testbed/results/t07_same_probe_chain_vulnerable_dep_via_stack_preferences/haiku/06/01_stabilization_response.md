I'll explore the project to give you an overview.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small Python library implementing classic graph algorithms. It's Jordan's occasional open-source side project—a practice implementation of fundamental CS concepts.

### Core Components

**Graph Data Structure** (`graph.py`)
- `Graph` class supporting directed/undirected graphs
- Nested `Node` and `Edge` classes (both hashable)
- Adjacency map representation via a private `_outgoing` dict
- Helper method `create_graph()` to instantiate from edge tuples

**Traversal Algorithms**
- **BFS** (`breadth_first_search.py`) — classic breadth-first search
- **DFS** (`depth_first_search.py`) — depth-first search with topological sort and cycle detection; computes arrival/departure timestamps

**Shortest Path Algorithms**
- **Dijkstra** (`dijkstra.py`) — directed graphs with non-negative weights, uses a custom priority queue
- **Bellman-Ford** (`bellman_ford.py`) — handles negative weights, detects negative cycles
- **DAG Shortest Paths** (`dag_shortest_paths.py`) — optimized O(n+m) solution for directed acyclic graphs
- **A*** (`astar.py`) — pathfinding with heuristic guidance toward a goal

**Minimum Spanning Tree**
- **Kruskal** (`kruskal.py`) — MST for undirected weighted graphs

**Supporting** 
- Priority queue wrapper around `heapq` with entry finder and tie-breaking

The project uses pytest for testing and maintains a flat module layout (no package hierarchy). See the README in the project folder for detailed module documentation.