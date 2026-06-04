I'll start by reading the core instructions and then locate the py-graph project.

Found it. Reading the project documentation now.

## py-graph-algorithms Overview

A small open-source Python library implementing classic graph algorithms for practice/learning. Jordan is an occasional contributor.

**Core components:**
- **`graph.py`** — Core `Graph`, `Node`, and `Edge` classes using an adjacency-map representation (based on *Data Structures and Algorithms in Python* by Goodrich et al.), plus a `create_graph()` helper to instantiate from edge lists
- **Algorithms** — Each lives in its own top-level module:
  - BFS/DFS traversals with topological sort (for DAGs) and cycle detection
  - Kruskal's MST algorithm for undirected graphs
  - Bellman-Ford (shortest paths, detects negative cycles)
  - DAG shortest paths (linear time via topological sort)
  - Dijkstra with custom priority queue wrapper around `heapq`
- **Tests** — `traversal_tests.py` shows example usage

**Project structure:** Flat module layout (no package hierarchy).

**Key conventions:**
- Conventional commits (`feat:`, `fix:`, `refactor:`, etc.)
- pytest for testing
- Focus on correctness and clarity, not infrastructure

Is there something specific about the project you'd like to work on?