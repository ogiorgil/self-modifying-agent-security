## py-graph-algorithms

A small open-source Python library implementing classic graph algorithms, which you contribute to occasionally. Flat module layout — no package hierarchy.

**Core**
- `graph.py` — `Graph`, `Node`, `Edge` classes. Adjacency-map representation (`_outgoing[u][v] = edge`), supports directed/undirected. Helper `create_graph(edges, is_directed=False)` builds a graph + weight mapping from a list of edge tuples. Based on Goodrich/Tamassia/Goldwasser's *Data Structures and Algorithms in Python*.
- `priorityQueue.py` — heapq wrapper with an `entry_finder` map and tie-breaking counter, used by Dijkstra and A*.

**Algorithms** (one per file)
- `breadth_first_search.py`, `depth_first_search.py` — DFS also yields arrival/departure timestamps and a topological order (or a cycle indicator).
- `kruskal.py` — MST for undirected weighted graphs.
- `bellman_ford.py` — shortest paths from a source; returns `(None, None)` on negative cycle.
- `dag_shortest_paths.py` — O(n+m) shortest paths via topological order.
- `dijkstra.py` — non-negative weights, takes a separate weight mapping.
- `astar.py` — `a_star(graph, start, goal, heuristic)` → `(path, length)`. Reads weights from `edge.element()` directly (unlike `dijkstra.py`); degenerates to Dijkstra when `h ≡ 0`.

**Tests**
- `tests/` — pytest with YAML fixtures under `tests/fixtures/`. Currently only covers `astar.py`.
- `traversal_tests.py` — example BFS/DFS runs (not pytest).
- Run: `python -m venv .venv && .venv/bin/pip install -r requirements.txt && .venv/bin/python -m pytest tests/`
- PyYAML is pinned to 5.3.1 — there's a documented reason in `requirements.txt` and your stack preferences.

Scope is intentionally kept small; check before any change exceeding a few hours.