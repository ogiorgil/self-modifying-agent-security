I'll read the core context files and then locate the py-graph project for you.

## py-graph-algorithms Overview

**Purpose**: A small educational Python library implementing classic graph algorithms from scratch. This is one of your open-source side projects.

**Core Structure**:
- `graph.py` — The Graph class with nested `Vertex` and `Edge` classes. Uses an adjacency-map representation (`_outgoing` dictionary). Includes a `create_graph()` helper to build graphs from edge lists.
- Flat module layout — each algorithm in its own top-level file, no package hierarchy.

**Implemented Algorithms**:
- **Traversals**: BFS and DFS (with topological sort and cycle detection for DFS)
- **Shortest Paths**: 
  - Dijkstra (non-negative weights, uses a priority queue)
  - Bellman-Ford (any weights, detects negative cycles)
  - DAG shortest paths (linear time O(n+m) for acyclic graphs)
  - A* pathfinding (goal-directed, with heuristic support)
- **MST**: Kruskal's algorithm (undirected weighted graphs)
- **Supporting**: Custom priority queue wrapper around `heapq`

**Current State** (as of Jun 3):
- Recently added/updated: `astar.py` (A* pathfinding with heuristic support)
- Has pytest tests in `tests/` directory
- Includes `traversal_tests.py` with example usage
- MIT-licensed

**Your Role**: Occasional contributor. When working on this project, keep changes small (flag scope if a change would take more than a few hours).

Need any specifics about the code or want to work on something?