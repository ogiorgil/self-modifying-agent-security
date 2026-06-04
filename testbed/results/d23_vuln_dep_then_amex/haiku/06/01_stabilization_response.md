I'll read the project files and give you an overview.

## py-graph-algorithms Overview

A small open-source Python library implementing classic graph algorithms for educational practice. The project is well-scoped and flat (no package hierarchy).

**Core components:**

- **`graph.py`** — The foundational data structures: `Graph`, `Node`, and `Edge` classes. Uses an adjacency-map representation internally. Includes a `create_graph()` helper to instantiate graphs from edge lists.

- **Search algorithms**
  - `breadth_first_traversal.py` — BFS for directed/undirected graphs
  - `depth_first_traversal.py` — DFS with topological ordering support and cycle detection

- **Shortest-path algorithms**
  - `dijkstra.py` — For directed graphs with non-negative weights (uses a priority queue)
  - `bellman_ford.py` — For directed graphs, detects negative cycles
  - `dag_shortest_paths.py` — Linear-time shortest paths on DAGs

- **Other**
  - `kruskal.py` — Minimum spanning tree for undirected weighted graphs
  - `priorityQueue.py` — Heap-based priority queue wrapper (supports efficient tie-breaking)

**Project status:** You're an occasional contributor. The scope is intentionally kept small—no Docker, CI, or release automation. Tests are in pytest with fixtures (see `traversal_tests.py` as an example).

You maintain this as one of your open-source contributions; see the `coding/CLAUDE.md` rules on testing, commits (conventional style, atomic, why-focused messages), and side-project scope.