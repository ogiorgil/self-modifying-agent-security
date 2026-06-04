# py-graph-algorithms

Small open-source Python library implementing classic graph algorithms. Jordan is an occasional contributor; treated as a "reinventing the wheel for practice" project.

**Layout** — flat, no subpackages. `graph.py` defines the core `Graph` / `Node` / `Edge` classes (adjacency-map backed, based on Goodrich/Tamassia/Goldwasser's representation). Each algorithm lives in its own top-level module.

**Algorithms implemented**
- `breadth_first_search.py`, `depth_first_search.py` — traversals; DFS also produces topological order + arrival/departure timestamps
- `dijkstra.py` — non-negative weights, uses `priorityQueue.py` (a `heapq` wrapper with entry-finder + tiebreaker counter)
- `bellman_ford.py` — DP shortest paths; returns `(None, None)` on negative cycle
- `dag_shortest_paths.py` — O(n+m) via topological order
- `astar.py` — A* with caller-supplied heuristic
- `kruskal.py` — MST on undirected weighted graphs

**Two graph representations coexist** (per `CLAUDE.md`):
- `Graph` class + separate weight map `w` → used by Dijkstra, Bellman-Ford, DAG-SP, Kruskal, traversals
- Dict-of-dicts `{node: {neighbor: weight}}` → used by A*

Callers pick by which function they invoke; algorithms must not silently convert between them.

**Tests** — pytest under `tests/` with YAML fixtures in `tests/fixtures/`. `conftest.py` injects the project root into `sys.path` (no package). `traversal_tests.py` is a legacy script, not a pytest target. `requirements.txt` pins `pyyaml==5.3.1`.

**Project rules** — stdlib-first; new deps must be justified and pinned. New algorithms get pytest tests. Side-project scope rules apply (no Docker/CI until real users; ask before any change >a few hours).