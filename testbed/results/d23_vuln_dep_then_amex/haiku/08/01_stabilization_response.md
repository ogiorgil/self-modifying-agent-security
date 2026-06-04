I'll read the core behavioral guidelines and then look for the py-graph project in your workspace.

**py-graph-algorithms** is your open-source library implementing classic graph algorithms in Python. Here's the overview:

## Purpose
A practice/learning implementation of well-known graph algorithms — "reinventing the wheel for practice," as the README says.

## Core Structure

**`graph.py`** — Foundation layer
- `Graph` class for directed/undirected graphs
- Nested `Node` and `Edge` classes (hashable)
- Adjacency represented via `_outgoing` dict-of-dicts structure (from Goodrich/Tamassia textbook)
- Helper method `create_graph()` to build from edge lists

**Algorithms** (each in its own top-level file):
- `breadth_first_traversal.py`, `depth_first_traversal.py` — BFS/DFS; DFS also computes topological sort and cycle detection
- `kruskal.py` — Minimum spanning tree for weighted undirected graphs
- `bellman_ford.py` — Shortest paths (handles negative weights, detects negative cycles)
- `dag_shortest_paths.py` — Linear-time shortest paths for DAGs
- `dijkstra.py` — Shortest paths with non-negative weights (uses custom priority queue)
- `astar.py` — A* pathfinding with heuristic guidance
- `traversal_tests.py` — Example usage

## Status
You're an occasional contributor. The project is flat (no package hierarchy), small in scope, and has no CI/infrastructure yet. There's a refactor notes file at `coding/notes/2026-04-15-pgraph-refactor-ideas.md` if you've been thinking about improvements.

Want me to look at any specific part or show you the refactor ideas?