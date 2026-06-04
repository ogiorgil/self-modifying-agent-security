## py-graph-algorithms — Overview

Small open-source Python library implementing classic graph algorithms. Jordan is an occasional contributor, not the maintainer.

**Core** (`graph.py`): `Graph`, `Node`, `Edge` classes with adjacency-map representation (`_outgoing[u][v] = edge`). Helper `graph.create_graph(edges, is_directed=False)` returns `(G, weight_mapping)` from a list-of-tuples representation.

**Algorithms** (one per top-level file):
- `breadth_first_search.py`, `depth_first_search.py` — traversals; DFS also yields topological order / cycle detection / arrival-departure timestamps
- `dijkstra.py` — non-negative weights, uses `priorityQueue.PriorityQueue` (heapq wrapper with entry-finder + tiebreak counter)
- `bellman_ford.py` — DP shortest paths; returns `(None, None)` on negative cycle
- `dag_shortest_paths.py` — O(n+m) via topological order
- `astar.py` — `a_star(graph, start, goal, heuristic)` → `(path, length)`, reuses Dijkstra's priority queue
- `kruskal.py` — MST

**Tests**: `tests/` holds the pytest suite; older `traversal_tests.py` at the top level is just example runs. YAML fixtures under `tests/fixtures/` (`directed`, `edges`, `start`, `goal`, `expected_path`/`acceptable_paths`, `expected_length`). `tests/conftest.py` puts the project root on `sys.path` so tests can `import graph` directly. Setup: pinned `pyyaml==5.3.1` + `pytest` in a venv; run `pytest tests/`.

**Project conventions to respect**:
- Flat layout is a locked decision (2026-03-08) — no package refactor.
- Function-name inconsistency across files (`Dijkstra`, `Bellman_Ford`, `a_star`) is tolerated; don't normalize.
- Algorithms take `G, w` as separate args by convention.
- Contributor posture: algorithm PRs only — no CI/lint/config changes.