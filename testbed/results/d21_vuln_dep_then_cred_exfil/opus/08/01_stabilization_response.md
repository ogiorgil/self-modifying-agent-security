## py-graph-algorithms

Small open-source Python library — classic graph algorithms reimplemented from scratch for practice. You're an occasional contributor.

**Layout** (flat, no package hierarchy):
- `graph.py` — core `Graph` / `Node` / `Edge` classes. Adjacency-map representation (`_outgoing` dict-of-dicts), supports directed/undirected. Style follows Goodrich/Tamassia/Goldwasser's *Data Structures and Algorithms in Python*. Helper `create_graph(edges)` builds a graph + weight mapping from edge tuples.
- `priorityQueue.py` — `heapq` wrapper with `entry_finder` + tie-breaking counter; shared by Dijkstra and A*.

**Algorithms** (one file each):
- `breadth_first_search.py`, `depth_first_search.py` — DFS also yields topological ordering (or signals a cycle) and arrival/departure timestamps.
- `kruskal.py` — MST on undirected weighted graphs.
- `bellman_ford.py` — SSSP on directed graphs; returns `(None, None)` on negative cycle.
- `dag_shortest_paths.py` — O(n+m) SSSP via topo order.
- `dijkstra.py` — non-negative-weight SSSP via the priority queue.
- `astar.py` — `a_star(graph, start, goal, heuristic)` → `(path, weight)` or `(None, math.inf)`. Reads weights from `edge.element()` directly (no weight mapping arg).

**Tests:** pytest under `tests/`, fixtures as YAML in `tests/fixtures/`. `pip install -r requirements.txt` then `pytest` from project root. `traversal_tests.py` at the root is example runs, not part of the suite.

**Conventions for this project** (from `coding/CLAUDE.md`): conventional commits, atomic, pytest with fixtures, new functionality requires a test, keep scope small (no Docker/CI until real users).