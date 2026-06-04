I'll give you an overview of the py-graph project. Let me start by reading the relevant project files.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small open-source Python library implementing classic graph algorithms for educational purposes. Jordan is an occasional contributor.

### Core Structure

The project uses a flat module layout (no package hierarchy):
- **`graph.py`** — Core data structures: `Graph`, `Node`, and `Edge` classes supporting both directed and undirected graphs. Uses an adjacency-map representation (nested dict) based on *Data Structures and Algorithms in Python* by Goodrich, Tamassia, and Goldwasser.
- Each algorithm in its own top-level file

### Implemented Algorithms

| Algorithm | File | Purpose |
|-----------|------|---------|
| BFS | `breadth_first_search.py` | Graph traversal |
| DFS | `depth_first_search.py` | Graph traversal; can compute topological ordering and detect cycles |
| Dijkstra | `dijkstra.py` | Shortest paths (non-negative weights) using priority queue |
| Bellman-Ford | `bellman_ford.py` | Shortest paths (handles negative weights); detects negative cycles |
| DAG Shortest Paths | `dag_shortest_paths.py` | Linear-time shortest paths for directed acyclic graphs |
| Kruskal | `kruskal.py` | Minimum spanning tree for undirected weighted graphs |
| A* | `astar.py` | Pathfinding with admissible heuristic (added more recently) |
| Priority Queue | `priorityQueue.py` | Helper for Dijkstra; wraps `heapq` with entry tracking |

### Testing

- `traversal_tests.py` — Example runs (not unit tests)
- `tests/test_astar.py` — pytest-based tests with fixtures
- Test data in `tests/fixtures/` (YAML files)

### Notes for Contributing

There's a mid-April scratchpad (`2026-04-15-pgraph-refactor-ideas.md`) with potential small PRs:
- Fix README typos (file name references)
- Fix DFS docs (topo ordering only applies to directed graphs)
- Add type hints to `PriorityQueue`

The maintainer appears to focus on classic CLRS algorithms, so bigger changes (like substantial testing infrastructure or packaging modernization) would need discussion first.