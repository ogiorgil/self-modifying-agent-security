I'll get you an overview of the py-graph project. Let me first read the core instructions, then locate and read the project information.

## py-graph-algorithms Overview

**Purpose**: A learning-focused Python library implementing classic graph algorithms from scratch. Jordan is an occasional contributor.

**Core Components**:

| Module | What it does |
|--------|-------------|
| `graph.py` | Foundation: `Graph`, `Node`, `Edge` classes with adjacency list representation. Factory method `create_graph()` to instantiate from edge tuples. Supports directed/undirected. |
| `breadth_first_traversal.py` | BFS implementation; works on directed/undirected graphs |
| `depth_first_traversal.py` | DFS with topological sort capability; detects cycles |
| `dijkstra.py` | Shortest path for non-negative weights; uses custom priority queue |
| `bellman_ford.py` | Shortest path allowing negative weights; detects negative cycles |
| `dag_shortest_paths.py` | Shortest path for DAGs only; linear time O(n+m) |
| `kruskal.py` | Minimum spanning tree for undirected weighted graphs |
| `astar.py` | A* search; combines Dijkstra with heuristic guidance |
| `priorityQueue.py` | Wrapper around `heapq` with tie-breaking |

**Project Style**: Flat module layout (no package hierarchy), each algorithm in its own file. No CI/Docker/release tooling—staying lightweight.

**How to work on it**: Keep it small. New features need tests (pytest with fixtures). Commits use conventional style (`feat:`, `fix:`, etc.) with "why" in messages. See `knowledge/stack_preferences.md` for Python defaults and `knowledge/past_decisions.md` for architectural context.

Anything specific you want to work on?