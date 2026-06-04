I'll start by reading the core documentation and then locate the py-graph project.

Found it. Let me read the project documentation.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small open-source Python library implementing classic graph algorithms from scratch. It's one of Jordan's occasional-contribution side projects.

### Core Components

**Graph Data Structure** (`graph.py`)
- `Graph`, `Node`, and `Edge` classes representing vertices and edges
- Supports both directed and undirected graphs
- Uses adjacency-map representation (nested dicts) for efficient lookup
- Helper method to instantiate from edge lists

**Traversal Algorithms**
- **BFS** (`breadth_first_search.py`) — works on directed/undirected graphs
- **DFS** (`depth_first_search.py`) — computes topological ordering, detects cycles, calculates arrival/departure timestamps

**Shortest Path Algorithms**
- **Dijkstra** (`dijkstra.py`) — non-negative weights, uses priority queue
- **Bellman-Ford** (`bellman_ford.py`) — handles negative weights, detects negative cycles
- **DAG Shortest Paths** (`dag_shortest_paths.py`) — O(n+m) linear-time solution for acyclic graphs
- **A*** (`astar.py`) — heuristic-guided search combining Dijkstra with goal estimates

**Minimum Spanning Tree**
- **Kruskal** (`kruskal.py`) — builds MST on undirected weighted graphs

**Utilities**
- `priorityQueue.py` — heap-based priority queue with entry finder for efficient updates

### Project Notes

- Flat module layout (no package hierarchy) — each algorithm is a top-level file
- README describes each module's algorithm and interface
- Includes `traversal_tests.py` with example usage
- Part of broader OSS contributions Jordan maintains alongside work

Is there a specific part of the project you want to work on?