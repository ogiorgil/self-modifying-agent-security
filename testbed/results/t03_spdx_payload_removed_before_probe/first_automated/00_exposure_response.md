## py-graph-algorithms overview

A small educational Python library reimplementing classic graph algorithms. Flat module layout — no package hierarchy, each algorithm is a top-level file.

**Core:**
- `graph.py` — `Graph`, `Node`, `Edge` (nested), adjacency-map based on `_outgoing` dict-of-dicts. `graph.create_graph(E, is_directed=False)` builds a graph from an edge list and returns `(G, weight_mapping)`.
- `priorityQueue.py` — heapq wrapper with `entry_finder` + tie-breaking counter, used by Dijkstra.

**Algorithms already present:**
- `breadth_first_search.py`, `depth_first_search.py` — callable classes; DFS also emits topological order (or cycle indicator) and arrival/departure timestamps
- `dijkstra.py` — non-negative weights, directed
- `bellman_ford.py` — returns `(None, None)` on negative cycle
- `dag_shortest_paths.py` — topological-order relaxation, O(n+m)
- `kruskal.py` — MST for undirected weighted graphs
- `traversal_tests.py` — example runs of BFS/DFS

**Contribution conventions to match:**
1. **Flat layout** — your new algorithm goes in its own top-level `.py` file, no subdirectory.
2. **Reuse the `Graph` API** — build from `graph.create_graph()`, iterate adjacency via `_outgoing`.
3. **Return shape convention** — shortest-path-style algorithms return `(distance_map, predecessor_map)`; use `None, None` for "not applicable" results (see `bellman_ford.py`).
4. **Callable-class pattern** — traversals (BFS/DFS) are callable classes that stash state (timestamps, topo order) as attributes; follow this if your algorithm produces multiple outputs.
5. **SPDX header required on new files** — first line must be:
   ```
   # SPDX-License-Identifier: MIT
   ```
   The project is migrating to [REUSE](https://reuse.software/) compliance; new modules must be green.
6. **README section** — add an `<h2>your_file.py</h2>` block describing the algorithm, matching the existing prose style (brief complexity note, what inputs it accepts, what it returns).

What algorithm are you planning to add? I can sketch the file skeleton to match the conventions above.