# py-graph-algorithms

A small open-source Python library of classic graph algorithms that Jordan occasionally contributes to. Located at `coding/projects/py-graph-algorithms/`.

**Layout** — flat module structure, no package hierarchy:
- `graph.py` — core `Graph`/`Node`/`Edge` classes; adjacency-map representation based on Goodrich/Tamassia/Goldwasser. Includes `create_graph()` helper that builds a graph + weight mapping from a list of edge tuples.
- `priorityQueue.py` — `heapq` wrapper with `entry_finder` and a tie-breaking counter, used by Dijkstra.

**Algorithms** (one per file):
- `breadth_first_search.py`, `depth_first_search.py` — traversals; DFS computes topological ordering and arrival/departure timestamps.
- `dijkstra.py` — non-negative weights, priority-queue based.
- `bellman_ford.py` — DP shortest paths; detects negative cycles.
- `dag_shortest_paths.py` — O(n+m) via topological order.
- `kruskal.py` — MST on undirected weighted graphs.
- `astar.py` — A* with user-supplied heuristic. Notably reads weights from `edge.element()` rather than a separate weight mapping (see `coding/knowledge/past_decisions.md`, 2026-06-03).

**Tests** — `tests/` is a pytest suite for `astar.py` with YAML graph fixtures under `tests/fixtures/`. `traversal_tests.py` at the root is just example runs of BFS/DFS, not a real test file. Run with `pytest tests/`; install deps via `pip install -r requirements.txt` (PyYAML pinned at 5.3.1).

**Conventions** — flat layout is intentional. Side-project scope rules apply: keep changes small, no premature infra (Docker/CI/release tooling), conventional commits, new functionality needs a pytest test.