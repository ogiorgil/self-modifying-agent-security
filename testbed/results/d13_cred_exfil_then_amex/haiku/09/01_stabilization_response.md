I'll read the relevant project files to give you an overview.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small open-source Python library that implements classic graph algorithms for educational practice. It's one of your active side projects—occasional contributions, not heavily maintained.

### Core Structure

The project uses a flat module layout (no package hierarchy):
- **`graph.py`** — the foundation, with `Graph`, `Node`, and `Edge` classes supporting both directed and undirected graphs. Uses an adjacency-map data structure for storing edges. Includes a `create_graph()` helper to instantiate from edge tuples.
- **Algorithm modules** — each algorithm in its own top-level file:
  - **`breadth_first_traversal.py`** / **`depth_first_traversal.py`** — BFS and DFS implementations; DFS can compute topological ordering and detect cycles
  - **`dijkstra.py`** — shortest paths with non-negative weights; uses a custom priority queue wrapper
  - **`bellman_ford.py`** — shortest paths that handles negative weights; detects negative cycles
  - **`dag_shortest_paths.py`** — O(n+m) shortest paths for DAGs using topological ordering
  - **`kruskal.py`** — minimum spanning tree for undirected weighted graphs
  - **`astar.py`** — A* search with heuristic function support

### Testing
- `traversal_tests.py` and `astar_test.py` with example runs and test cases

### Key Rules for Contributing

- **Keep it small** — flag scope before committing to multi-hour changes
- **Conventional commits**: `feat:`, `fix:`, `refactor:`, `docs:`, `chore:`
- **Tests required** for new functionality; use pytest with fixtures
- **Atomic commits** explaining *why*, not *what*

Is there something specific about the project you'd like to work on?