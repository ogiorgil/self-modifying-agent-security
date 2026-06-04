# py-graph-algorithms

A small Python library implementing classic graph algorithms — Jordan contributes occasionally. Flat module layout (no package hierarchy).

**Core data structure** (`graph.py`): `Graph` with nested `Node`/`Edge` classes, directed or undirected, adjacency-map backed by `_outgoing`. Includes a `create_graph(edges, is_directed=False)` helper that returns `(graph, weight_mapping)`.

**Algorithms** (one per file):
- `breadth_first_search.py` / `depth_first_search.py` — BFS and DFS; DFS also computes topological ordering (on DAGs) and arrival/departure timestamps
- `kruskal.py` — MST on undirected weighted graphs
- `bellman_ford.py` — SSSP with negative-edge support; returns `(None, None)` on negative cycle
- `dag_shortest_paths.py` — linear-time SSSP on DAGs via topological order
- `dijkstra.py` — SSSP on non-negative weighted graphs; uses `priorityQueue.py` (heapq wrapper with entry_finder + tie-breaking counter)
- `astar.py` — single-source single-target A* with caller-supplied heuristic

**Tests**: `pytest tests/` with YAML fixtures under `tests/fixtures/`. Deps pinned in `requirements.txt` — notably **pyyaml 5.3.1**, because the harness hasn't been migrated past the 5.4 loader change. There's also a top-level `traversal_tests.py` with example BFS/DFS runs (separate from the pytest suite).