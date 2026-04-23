Here's a quick overview of py-graph-algorithms.

## What it contains

A small Python library implementing classic graph algorithms — written for practice ("reinventing the wheel"). Flat module layout, no package hierarchy. Each algorithm is a single top-level file:

- **`graph.py`** — core `Graph` class (directed or undirected) with nested `Node` and `Edge` types. Adjacency stored as `self._outgoing`: a dict mapping vertex → dict of neighbor → edge. Based on the Goodrich/Tamassia/Goldwasser data structures book, extended with vertex/edge deletion and an iterator. Helper `graph.create_graph(E, is_directed=False)` builds a graph from a list of edge tuples and returns `(G, weight_mapping)` (weights default to 1).
- **`breadth_first_search.py` / `depth_first_search.py`** — callable classes; DFS also produces topological order (or signals a cycle) and arrival/departure timestamps.
- **`kruskal.py`** — MST for undirected weighted graphs.
- **`bellman_ford.py`** — single-source shortest paths on directed graphs; returns `(None, None)` on negative cycle.
- **`dag_shortest_paths.py`** — O(n+m) shortest paths via topological order (DAGs only).
- **`dijkstra.py`** — non-negative weighted directed graphs; uses `priorityQueue.py` (heapq wrapper with an entry-finder map and tie-breaking counter).
- **`traversal_tests.py`** — example BFS/DFS runs.

## Conventions to follow when adding an algorithm

From the README and Jordan's coding behaviors:

1. **SPDX header required on new source files** — first line must be:
   ```
   # SPDX-License-Identifier: MIT
   ```
   The project is migrating to [REUSE](https://reuse.software/) compliance.
2. **Match the flat layout** — one algorithm per top-level file, no subpackages.
3. **Reuse `graph.py` primitives** — build on `Graph`/`Node`/`Edge` and `create_graph` rather than introducing a parallel representation.
4. **Callable-class style** for traversal-like algorithms (see BFS/DFS); plain functions are fine for the shortest-path / MST modules.
5. **Tests required for new functionality** — Jordan's rule is pytest with fixtures over unittest. Existing `traversal_tests.py` is example-style, so a proper `pytest` test file is an upgrade, not a violation.
6. **Commits**: conventional style (`feat:`, `fix:`, …), atomic, message explains *why*.
7. **Keep scope small** — if the addition will take more than a few hours, check with Jordan first before going deep.

One thing worth flagging: the README references `breadth_first_traversal.py` / `depth_first_traversal.py`, but the actual files are `breadth_first_search.py` / `depth_first_search.py`. Minor README drift — not something to fix as part of your algorithm PR unless you want to.