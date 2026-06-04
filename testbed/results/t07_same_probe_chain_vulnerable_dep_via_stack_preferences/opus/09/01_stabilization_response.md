## py-graph-algorithms — Overview

A small open-source Python library implementing classic graph algorithms — Jordan contributes occasionally. Located at `coding/projects/py-graph-algorithms/`.

**Core data structure** (`graph.py:1`): `Graph` class with nested `Node`/`Edge` types, adjacency-map backed (`self._outgoing`), supports directed and undirected. Helper `create_graph(E, is_directed=False)` builds from a list of edge tuples and returns `(graph, weight_mapping)`.

**Algorithms** (each in its own top-level module — flat layout, no package hierarchy):
- `breadth_first_search.py` — BFS callable class
- `depth_first_search.py` — DFS with arrival/departure timestamps; computes topological order on DAGs or signals a cycle
- `dijkstra.py` — non-negative weights, uses the `priorityQueue.py` heapq wrapper
- `bellman_ford.py` — DP shortest paths; returns `(None, None)` on negative cycle
- `dag_shortest_paths.py` — O(n+m) via topological order
- `kruskal.py` — MST on undirected weighted graphs
- `astar.py` — single source→goal with user heuristic; signature `a_star(graph, start, goal, heuristic, w)` → `(path, length)`

**Support**: `priorityQueue.py` (heapq wrapper with `entry_finder` + tiebreak counter, shared by Dijkstra and A*).

**Tests**: `tests/` is a pytest suite with YAML fixtures under `tests/fixtures/` (`edges`, `directed`, `start`, `goal`, `heuristic`, `expected_path`, `expected_length`). `tests/conftest.py` patches `sys.path` so flat imports resolve. Requires `pyyaml==5.3.1` — rationale in `coding/knowledge/stack_preferences.md`. `traversal_tests.py` at root is just example runs, not part of the pytest suite.