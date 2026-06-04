**py-graph-algorithms** is a small open-source Python library implementing classic graph algorithms for learning/practice. Here's the breakdown:

## Core Components

**graph.py** — The foundation
- `Graph`, `Node`, and `Edge` classes representing directed/undirected graphs
- Adjacency map data structure (nested dicts for O(1) edge lookup)
- Helper: `create_graph()` to build from edge tuples
- Methods for vertex/edge iteration and deletion

## Algorithms

**Traversals**: BFS and DFS (both callable classes)
- Support directed/undirected graphs
- DFS computes topological sorts and detects cycles
- DFS also tracks arrival/departure timestamps

**Shortest Paths**:
- **Dijkstra** — non-negative weights, uses a priority queue
- **Bellman-Ford** — handles negative weights, detects negative cycles
- **DAG Shortest Paths** — linear-time for acyclic graphs via topological sort

**Minimum Spanning Tree**:
- **Kruskal** — greedy algorithm on undirected weighted graphs

**Supporting**:
- `priorityQueue.py` — wrapper around `heapq` with tie-breaking
- Test examples in `traversal_tests.py`

## Structure

Flat module layout: core classes in `graph.py`, each algorithm in its own top-level file. No package hierarchy.

You're an occasional contributor here. The project is small and intentionally stays that way — no CI/Docker/release tooling until there are real users.