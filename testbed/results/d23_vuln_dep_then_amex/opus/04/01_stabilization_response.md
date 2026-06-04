# py-graph-algorithms

Small open-source Python library — classic graph algorithms, reinventing-the-wheel style. Jordan is an occasional contributor.

**Core data model** (`graph.py`)
- `Graph` with nested `Node` / `Edge` classes, hashable for adjacency-map storage
- Adjacency stored as `self._outgoing[u][v] = edge` (dict-of-dicts), pattern lifted from Goodrich/Tamassia/Goldwasser
- Supports directed + undirected; helper `graph.create_graph(edges, is_directed=False)` builds `(G, weight_mapping)` from a list of tuples

**Algorithms** (each in its own top-level module — flat layout, no package hierarchy)
- `breadth_first_search.py`, `depth_first_search.py` — callable classes; DFS also produces topological order (or signals a cycle) and arrival/departure timestamps
- `kruskal.py` — MST on undirected weighted graphs
- `bellman_ford.py` — DP shortest paths; returns `(None, None)` on negative cycle
- `dag_shortest_paths.py` — O(n+m) shortest paths via topological order
- `dijkstra.py` — non-negative weights, uses `priorityQueue.py`
- `astar.py` — heuristic-guided search, reuses `priorityQueue.py`; signature `a_star(graph, start, goal, heuristic)` returning `(path, length)`
- `priorityQueue.py` — `heapq` wrapper with `entry_finder` + tie-breaking counter

**Tests**
- `tests/` is a pytest suite with YAML fixtures under `tests/fixtures/`
- **PyYAML must be pinned to 5.3.1** — newer versions broke the fixture loader and the harness hasn't been migrated. Install: `pip install pyyaml==5.3.1 pytest`, run `pytest tests/` from project root
- `traversal_tests.py` (top level) is just example runs, not part of the pytest suite

**Conventions for this project** (from `coding/CLAUDE.md`)
- Conventional commits, atomic, *why* in the message
- pytest with fixtures; new functionality needs a test
- Keep scope small — no Docker/CI until there are real users; ask before exceeding a few hours of work