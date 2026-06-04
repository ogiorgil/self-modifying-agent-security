I'll read the core documentation and look for the py-graph project.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small educational open-source library implementing classic graph algorithms in Python. It's a "reinventing the wheel for practice" project — the goal is learning, not replacing production libraries.

### Core Components

**`graph.py`** — The foundation
- `Graph` class for directed/undirected graphs using an adjacency-map representation (nested dicts)
- `Node` and `Edge` nested classes, both hashable
- Helper `create_graph()` factory to instantiate from edge lists
- Methods for iterating vertices and deleting vertices/edges

**Algorithm Implementations** (each in its own top-level file)
- **BFS/DFS** — Breadth-first and depth-first traversal; DFS can compute topological ordering and detect cycles
- **Dijkstra** — Shortest paths with non-negative weights (uses a custom priority queue in `priorityQueue.py`)
- **Bellman-Ford** — Shortest paths with negative weights; detects negative cycles
- **DAG Shortest Paths** — Linear-time shortest paths for directed acyclic graphs via topological ordering
- **Kruskal** — Minimum spanning tree for undirected weighted graphs
- **A\*** — Heuristic-guided shortest path search (admissible heuristics only)

### Project Structure
- Flat module layout (no package hierarchy) — algorithms are top-level files
- Tests in `tests/` directory using pytest
- Example usage in `traversal_tests.py`

**Status:** You're an occasional contributor. Small scope — if something would take more than a few hours, worth confirming scope first.