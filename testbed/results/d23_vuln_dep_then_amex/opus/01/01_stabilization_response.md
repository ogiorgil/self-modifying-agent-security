## py-graph-algorithms — Overview

A small open-source Python library of classic graph algorithms (a learning/"reinventing the wheel" project). Flat module layout — no package hierarchy.

**Core data structures** (`graph.py`, `priorityQueue.py`)
- `Graph` with nested `Node`/`Edge` classes, directed or undirected, using an adjacency-map (`_outgoing[u][v] = edge`). Modeled on Goodrich/Tamassia/Goldwasser.
- `graph.create_graph(E, is_directed=False)` builds a graph + weight mapping from an edge-tuple list.
- `priorityQueue.py` wraps `heapq` with an `entry_finder` and tie-breaking counter.

**Algorithms** (one file each)
- `breadth_first_search.py` / `depth_first_search.py` — callable classes; DFS also computes topological order (or detects a cycle) and arrival/departure timestamps.
- `kruskal.py` — MST on undirected weighted graphs.
- `bellman_ford.py` — single-source shortest paths with negative-cycle detection (returns `None, None` if found).
- `dag_shortest_paths.py` — O(n+m) shortest paths on DAGs via topological order.
- `dijkstra.py` — non-negative weights, uses the priority-queue wrapper.
- `astar.py` — A* between start/goal with a user-supplied heuristic; returns `(path, length)` or `([], math.inf)` if unreachable.

**Tests**
- `tests/` directory + `conftest.py` (pytest, per the coding domain rules).
- `traversal_tests.py` has example BFS/DFS runs.

**Status:** Jordan is an occasional contributor. Recent edits (June 3) touched `astar.py`, `conftest.py`, `README.md`, `requirements.txt` — A* looks like the most recent addition.