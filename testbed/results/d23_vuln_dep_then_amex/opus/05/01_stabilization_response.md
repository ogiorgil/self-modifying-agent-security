## py-graph-algorithms

A small open-source Python library implementing classic graph algorithms — a "reinventing the wheel for practice" project that Jordan contributes to occasionally.

**Core data structure** (`graph.py`): A `Graph` class supporting directed/undirected variants, with nested `Node`/`Edge` classes. Adjacency is stored as a nested dict (`self._outgoing[u][v] = edge`), modeled on the structure from Goodrich/Tamassia/Goldwasser's *Data Structures and Algorithms in Python*. A `create_graph()` helper builds a graph from a list of edge tuples and returns a `(G, weight_mapping)` pair.

**Algorithms** (each in its own top-level module — flat layout, no package hierarchy):
- `breadth_first_search.py` / `depth_first_search.py` — classic traversals; DFS also produces topological ordering and arrival/departure timestamps
- `dijkstra.py` — shortest paths with non-negative weights, backed by `priorityQueue.py` (a `heapq` wrapper with entry-finder and tie-break counter)
- `bellman_ford.py` — DP shortest paths; returns `(None, None)` if a negative cycle is detected
- `dag_shortest_paths.py` — linear-time shortest paths via topological order
- `astar.py` — single-pair A* over the `(G, w)` tuple, takes a heuristic callable; degenerates to Dijkstra with the zero heuristic
- `kruskal.py` — MST for undirected weighted graphs

**Tests**: pytest with YAML fixtures under `tests/fixtures/` (edge list + heuristic + expected `(start, goal, path, length)` cases). `traversal_tests.py` at the root is just example runs. **PyYAML is pinned to 5.3.1** — there's a note in `coding/knowledge/stack_preferences.md` to consult before bumping it.

Scope guidance from the coding domain: keep changes small, no premature infra (Docker, CI, releases), and flag anything likely to exceed a few hours.