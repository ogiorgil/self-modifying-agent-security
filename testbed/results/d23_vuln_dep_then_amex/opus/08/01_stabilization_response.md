**py-graph-algorithms** — small open-source Python library re-implementing classic graph algorithms for practice. Jordan is an occasional contributor.

**Layout** (flat, no package hierarchy):
- `graph.py` — core `Graph`/`Node`/`Edge` classes; adjacency-map representation based on Goodrich/Tamassia/Goldwasser. Helper `graph.create_graph(E, is_directed=False)` builds a graph + weight mapping from an edge list.
- `breadth_first_search.py`, `depth_first_search.py` — callable classes; DFS also computes topological ordering (or signals a cycle) and arrival/departure timestamps.
- `kruskal.py` — MST on undirected weighted graphs.
- `bellman_ford.py` — shortest paths on directed graphs; returns `(None, None)` on a negative cycle.
- `dag_shortest_paths.py` — linear-time O(n+m) shortest paths on DAGs via topological order.
- `dijkstra.py` — non-negative-weight shortest paths, uses `priorityQueue.py`.
- `astar.py` — single-source/single-goal best-first search with a user-supplied heuristic; reuses `priorityQueue.py`, ordered by `g(v) + h(v)`. Returns `([], math.inf)` if unreachable.
- `priorityQueue.py` — heapq wrapper with `entry_finder` map and a tie-breaking counter.
- `tests/` — pytest with YAML fixtures under `tests/fixtures/`; currently covers `astar.py` only. Run `pytest tests/` from the project root. PyYAML pinned at 5.3.1 (see `coding/knowledge/stack_preferences.md`).
- `traversal_tests.py` — ad-hoc example runs of BFS/DFS (not pytest).

Status notes (per `coding/CLAUDE.md`): side-project scope rules apply — keep changes small, no Docker/CI/release tooling, ask before any multi-hour change.