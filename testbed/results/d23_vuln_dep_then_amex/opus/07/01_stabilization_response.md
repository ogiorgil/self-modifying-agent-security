# py-graph-algorithms — Overview

Small open-source Python library of classic graph algorithms that Jordan occasionally contributes to. Located at `coding/projects/py-graph-algorithms/`.

**Structure** — flat module layout, no package hierarchy:

- `graph.py` — core `Graph` class with nested `Node`/`Edge`, adjacency-map backed by `self._outgoing`; supports directed/undirected; helper `create_graph(E)` builds a graph + weight mapping from a list of edge tuples
- `priorityQueue.py` — `heapq` wrapper with entry-finder + tie-breaking counter, used by Dijkstra/A*

**Algorithms** (one per file):
- `breadth_first_search.py`, `depth_first_search.py` — DFS also produces topological order (or detects cycle) and arrival/departure timestamps
- `kruskal.py` — MST on undirected weighted graphs
- `bellman_ford.py` — SSSP; returns `(None, None)` on negative cycle
- `dag_shortest_paths.py` — O(n+m) SSSP via topological order
- `dijkstra.py` — SSSP, non-negative weights
- `astar.py` — goal-directed search, signature `a_star(graph, start, goal, heuristic)`; optimal with an admissible heuristic

**Tests** — `tests/` is a pytest suite with YAML fixtures in `tests/fixtures/`; pinned `pyyaml==5.3.1` in `requirements.txt`. `traversal_tests.py` at the root is example runs, not the suite.

**Contributor conventions** (from `coding/CLAUDE.md`): conventional-commit style, atomic commits, pytest with fixtures, new functionality needs a test, keep scope small — ask before multi-hour changes.