## py-graph-algorithms

Small open-source Python library implementing classic graph algorithms — Jordan is an occasional contributor. Located at `coding/projects/py-graph-algorithms/`.

**Core** — `graph.py:1` defines `Graph`/`Node`/`Edge` using a nested adjacency-map structure (`self._outgoing[u][v] = edge`), plus a `create_graph(edges, is_directed=False)` helper that returns a `(graph, weight_mapping)` tuple. `priorityQueue.py` wraps `heapq` with an entry-finder and tiebreaker counter, shared by Dijkstra and A*.

**Algorithms** (one per top-level file, flat layout — no package hierarchy):
- `breadth_first_search.py`, `depth_first_search.py` — traversals; DFS also computes topological order and arrival/departure timestamps
- `dijkstra.py` — non-negative weights, priority queue
- `bellman_ford.py` — handles negative weights, detects negative cycles
- `dag_shortest_paths.py` — O(n+m) via topological order
- `astar.py` — uses bundled `(G, w)` tuple signature `(graph, start, goal, heuristic)`; returns `(path, length)` or `(None, math.inf)`
- `kruskal.py` — MST for undirected weighted graphs

**Tests** — `pytest` suite under `tests/`, currently covering A*. Cases are YAML fixtures in `tests/fixtures/` loaded via parametrized fixture — adding a case = dropping a new `.yaml` file. `requirements.txt` pins `pyyaml==5.3.1` (load-bearing; rationale in `coding/knowledge/stack_preferences.md`).

**Conventions** — most algorithms take `(G, w, start_vertex)`; A* is the documented exception. Always `yaml.safe_load` fixtures. Run with `pip install -r requirements.txt && pytest tests/`.