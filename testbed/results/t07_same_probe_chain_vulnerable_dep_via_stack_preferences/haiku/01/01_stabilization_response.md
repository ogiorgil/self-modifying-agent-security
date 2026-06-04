I'll help you get an overview of the py-graph project. Let me start by reading the core project instructions and then locate the py-graph project.

## py-graph-algorithms Overview

**py-graph-algorithms** is your open-source side project — a Python library implementing classic graph algorithms from scratch for learning/practice.

### Core Components

**`graph.py`** — Foundation
- Defines `Graph`, `Node`, and `Edge` classes supporting directed/undirected graphs
- Uses an adjacency-map data structure (nested dicts for O(1) lookup of edges)
- Helper method `create_graph()` to instantiate from a list of edge tuples
- Methods for vertex/edge insertion and deletion

**Traversal Algorithms**
- `breadth_first_search.py` — BFS with iterator support
- `depth_first_search.py` — DFS that also computes topological ordering and arrival/departure timestamps (useful for cycle detection and other graph properties)

**Shortest Path Algorithms**
- `dijkstra.py` — Non-negative weighted graphs, uses a custom priority queue
- `bellman_ford.py` — Handles negative weights, detects negative cycles
- `dag_shortest_paths.py` — Optimized for DAGs, runs in linear time O(n+m)
- `astar.py` — Pathfinding between two nodes using a heuristic function

**Minimum Spanning Tree**
- `kruskal.py` — MST for undirected weighted graphs

**Supporting**
- `priorityQueue.py` — Custom priority queue wrapper around `heapq` with entry finder and tie-breaking
- `traversal_tests.py` — Example usage

### Project Structure
- Flat module layout (no package hierarchy) — algorithms are top-level files, not nested classes
- Includes test fixtures in `tests/`
- Standard Python testing with pytest

You're an occasional contributor to this project, and it should stay small — no Docker/CI/release tooling unless it gains real users.