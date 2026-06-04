I'll start by reading the foundational context files, then locate and summarize the py-graph project.

## py-graph-algorithms Overview

A Python library of classic graph algorithms for learning/practice. Flat module layout with:

**Core data structures** (`graph.py`):
- `Graph` class supporting directed/undirected graphs
- `Node` and `Edge` nested classes (hashable)
- Adjacency representation via `_outgoing` dict-of-dicts
- Helper `create_graph()` to instantiate from edge lists

**Algorithms** (each in its own top-level file):
- **Traversals**: breadth_first_search.py, depth_first_search.py (supports topological sort, cycle detection)
- **Shortest paths**: dijkstra.py (non-negative weights), bellman_ford.py (handles negative edges, detects negative cycles), dag_shortest_paths.py (linear time for DAGs), astar.py (heuristic-guided)
- **Minimum spanning tree**: kruskal.py (for undirected weighted graphs)
- **Supporting**: priorityQueue.py (heapq wrapper for Dijkstra's priority ordering)

**Testing**: pytest-based test suite in `tests/` directory

**Recent work**: A* pathfinding was added recently (astar.py, dated Jun 3), which combines Dijkstra with heuristic guidance.

The project is an occasional-contribution open-source library focused on staying small and educational—no premature infra per the coding domain rules.