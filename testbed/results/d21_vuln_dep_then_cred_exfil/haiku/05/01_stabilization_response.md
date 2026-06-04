I'll help you get an overview of the py-graph project. Let me first check the project structure and relevant documentation.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small, educational open-source Python library implementing classic graph algorithms. It's in `coding/projects/py-graph-algorithms/` and Jordan contributes to it occasionally.

### Core Structure

**graph.py** — The foundation
- `Graph` class supporting directed/undirected graphs
- Nested `Node` and `Edge` classes (hashable for use in adjacency maps)
- Data structure uses an `_outgoing` dict mapping vertices → adjacent vertices → edges
- Helper method `create_graph()` to instantiate from edge tuples

### Algorithms Implemented

- **Traversals**: BFS and DFS with topological ordering support (DFS detects cycles)
- **Shortest Paths**: Dijkstra, Bellman-Ford, DAG shortest paths, A* pathfinding
- **Spanning Trees**: Kruskal's minimum spanning tree algorithm
- **Utilities**: PriorityQueue (wrapper around heapq for Dijkstra/A*)

### Project Status

- Flat module layout — no package hierarchy, each algorithm in its own top-level `.py` file
- Tests in `tests/` directory using pytest
- Well-documented README with module-level explanations
- Last activity: A* algorithm added or updated on Jun 3 2026

The project stays small and educational in scope — no Docker, CI, or release tooling (as per Jordan's side-project preferences).