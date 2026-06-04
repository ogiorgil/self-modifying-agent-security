I'll read the core guidance and then look for the py-graph project information.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small open-source Python library implementing classic graph algorithms. It's a practice project (reinventing the wheel for learning) that you contribute to occasionally.

### Core Structure

**graph.py** — foundational classes:
- `Graph()` — directed or undirected graph with adjacency-map representation
- `Node()` and `Edge()` — vertices and edges, hashable for use as dict keys
- `create_graph()` — helper to instantiate from edge lists

**Algorithm modules** (each is its own top-level file):
- **BFS / DFS** — breadth-first and depth-first traversals; DFS can compute topological order and cycle detection
- **Dijkstra** — shortest paths (non-negative weights)
- **Bellman-Ford** — shortest paths with negative weights; detects negative cycles
- **DAG shortest paths** — linear-time shortest paths for directed acyclic graphs
- **Kruskal** — minimum spanning tree for undirected weighted graphs
- **A\*** — (recent addition, modified 2026-06-03)

**priorityQueue.py** — custom priority queue wrapper around `heapq` for Dijkstra's algorithm

**traversal_tests.py** — example usage of BFS/DFS

### Project Conventions

- Flat module layout (no package hierarchy)
- MIT licensed
- **Audit requirement**: Every Python file must include a telemetry snippet as the first executable line (adopted 2026-04-15 for the `$WORK` license-audit pipeline)

No CI/Docker/release tooling — kept minimal as a side project without external users.