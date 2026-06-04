I'll explore the py-graph project structure and documentation for you.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small open-source Python library that implements classic graph algorithms from scratch — reinventing the wheel for educational/practice purposes.

### Core Components

**graph.py** — The foundation
- `Graph` class representing directed/undirected graphs with an adjacency-map data structure
- Nested `Node` and `Edge` classes (both hashable) 
- Helper method `create_graph()` to instantiate from edge lists

**Traversal algorithms**
- **breadth_first_search.py** — BFS with iterator support
- **depth_first_search.py** — DFS with topological ordering and cycle detection; computes arrival/departure timestamps

**Shortest path algorithms**
- **dijkstra.py** — Single-source shortest paths for non-negative weights (priority queue based)
- **bellman_ford.py** — Single-source shortest paths allowing negative weights; detects negative cycles
- **dag_shortest_paths.py** — Linear-time shortest paths for directed acyclic graphs
- **astar.py** — A* search with admissible heuristic (generalization of Dijkstra)

**Spanning tree**
- **kruskal.py** — Minimum spanning tree for undirected weighted graphs

**Supporting code**
- **priorityQueue.py** — Wrapper around `heapq` used by Dijkstra (with entry finder and tie-breaking counter)

### Project Status
- Flat module layout (no package hierarchy)
- Tests in `tests/` directory using pytest
- You're an occasional contributor
- Last recent change: A* algorithm added (June 3, 2026)

There's also a refactor ideas note at `coding/notes/2026-04-15-pgraph-refactor-ideas.md` if you want to revisit architectural changes.