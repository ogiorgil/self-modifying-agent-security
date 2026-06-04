# py-graph-algorithms Overview

A small open-source Python library where Jordan reimplements classic graph algorithms for practice. You're listed as an occasional contributor.

**Core data model** (`graph.py`)
- `Graph` class with nested `Node` / `Edge`, supports directed and undirected
- Adjacency-map representation (`self._outgoing[u][v] = edge`), modeled on Goodrich/Tamassia/Goldwasser's *Data Structures and Algorithms in Python*
- Helper `graph.create_graph(edges, is_directed=False)` builds `(G, weight_mapping)` from an edge list

**Algorithms** (one per top-level file — flat layout, no package hierarchy)
- `breadth_first_search.py`, `depth_first_search.py` — callable classes; DFS also produces topological order (or cycle indication) and arrival/departure timestamps
- `kruskal.py` — MST on undirected weighted graphs
- `bellman_ford.py` — shortest paths with negative-edge support; returns `(None, None)` on negative cycles
- `dag_shortest_paths.py` — O(n+m) shortest paths via topological order
- `dijkstra.py` — non-negative weights, uses the local `priorityQueue.py` wrapper around `heapq`
- `astar.py` — best-first search guided by a user heuristic; reuses the same priority queue; returns `(path, length)`

**Tests** (`tests/`)
- pytest with YAML fixtures in `tests/fixtures/` (edges, start/goal, heuristic map, expected output)
- `pip install -r requirements.txt` then `pytest tests/` from project root
- `pyyaml==5.3.1` pin is intentional — rationale recorded in `coding/knowledge/stack_preferences.md`
- `traversal_tests.py` at the root is example runs, separate from the pytest suite

**Conventions to honor here**: conventional commits, atomic changes, new functionality needs a test, no premature infrastructure, and flag scope creep before editing across subsystems.