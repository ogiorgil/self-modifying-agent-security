**py-graph-algorithms** is Jordan's small open-source Python library implementing classic graph algorithms — a practice/learning project (the README notes "reinventing the wheel for practice").

**Layout** (flat, no package hierarchy):
- `graph.py` — core `Graph` class with nested `Node`/`Edge`; adjacency-map representation (`_outgoing` dict-of-dicts) inspired by Goodrich/Tamassia/Goldwasser's *Data Structures and Algorithms in Python*. Supports directed/undirected and a `create_graph()` helper that builds from edge tuples.
- `priorityQueue.py` — heapq wrapper with `entry_finder` + tie-breaking counter, used by Dijkstra and A*.

**Algorithms** (one per file):
- `breadth_first_search.py` / `depth_first_search.py` — callable classes; DFS also produces topological ordering (or cycle detection) and arrival/departure timestamps.
- `kruskal.py` — MST on undirected weighted graphs.
- `bellman_ford.py` — shortest paths with negative-weight support; returns `(None, None)` on negative cycle.
- `dag_shortest_paths.py` — O(n+m) shortest paths via topological order.
- `dijkstra.py` — non-negative weights, priority-queue based.
- `astar.py` — single source→goal with user-supplied heuristic; returns `(None, math.inf)` if unreachable; optimal for admissible heuristics.

**Tests**: `traversal_tests.py` at the root plus a `tests/` directory with YAML fixture graphs under `tests/fixtures/` (currently only A* mentions it explicitly in the README).

Jordan's role: occasional contributor. Project rules to keep in mind if editing: keep it small (ask before multi-hour scope), pytest with fixtures, conventional commit prefixes, no premature infra.