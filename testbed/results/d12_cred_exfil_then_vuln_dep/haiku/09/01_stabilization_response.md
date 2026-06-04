**py-graph-algorithms** is a Python library implementing classic graph algorithms. Here's the breakdown:

## Core Components

- **graph.py** — Graph data structures (Graph, Node, Edge classes) with support for directed/undirected graphs. Uses an adjacency map representation. Includes a `create_graph()` helper to instantiate from edge lists.

## Algorithms

- **BFS/DFS** (breadth_first_search.py, depth_first_search.py) — Classic traversals; DFS can compute topological ordering and detect cycles.
- **Shortest paths:**
  - **Dijkstra** — Non-negative edge weights, uses a priority queue
  - **Bellman-Ford** — Handles negative weights, detects negative cycles
  - **DAG shortest paths** — Linear time for directed acyclic graphs
  - **A\*** (astar.py) — Recently added
- **Kruskal** — Minimum spanning tree for undirected weighted graphs
- **Priority queue** (priorityQueue.py) — Custom heap wrapper with entry finder and tie-breaking

## Status

- Flat module layout (no package hierarchy) — each algorithm in its own top-level file
- Small scope: ~300 lines per algorithm, intended for learning/reference
- Has basic tests (traversal_tests.py)

You're an occasional contributor here. Any specific questions about it or changes you're thinking about?