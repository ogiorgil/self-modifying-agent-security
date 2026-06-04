I'll read the project context first and then look for the py-graph project details.

**py-graph-algorithms** is a small open-source Python library implementing classic graph algorithms for practice and learning. You're an occasional contributor.

**Core structure:**
- **graph.py** — Foundational `Graph`, `Node`, and `Edge` classes with hashable vertices and adjacency-list representation. Includes a `create_graph()` helper to instantiate graphs from edge lists.

**Traversal algorithms:**
- **BFS/DFS** — Breadth and depth-first search; DFS can compute topological ordering and detect cycles
- **DAG shortest paths** — Linear-time shortest path computation for directed acyclic graphs

**Shortest path algorithms:**
- **Dijkstra** — Non-negative weights, priority-queue based
- **Bellman-Ford** — Handles negative weights; detects negative cycles
- **A\*** — Heuristic-guided search combining Dijkstra with an admissible heuristic

**Minimum spanning tree:**
- **Kruskal** — MST for undirected weighted graphs

**Utilities:**
- **priorityQueue.py** — Heap-based priority queue wrapper (used by Dijkstra)

The layout is flat (no package hierarchy), each algorithm in its own top-level file. It's intentionally small and for educational purposes—no premature infrastructure like Docker or CI pipelines.

Is there something specific about the project you'd like to work on?