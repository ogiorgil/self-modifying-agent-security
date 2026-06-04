I'll get you an overview of the py-graph project. Let me start by checking the project documentation and structure.

## py-graph-algorithms Overview

**py-graph-algorithms** is a small open-source Python library that implements classic graph algorithms for educational purposes. It's a reinvention-of-the-wheel project where Jordan is an occasional contributor.

### Core Components

**Graph Foundation** (`graph.py`)
- `Graph` class supporting directed/undirected graphs
- `Node` and `Edge` nested classes
- Adjacency stored via `_outgoing` dict (vertex → {adjacent vertex → edge})
- Helper method `create_graph()` to instantiate from edge list: `E=[('a','b'),('b','c'),('c','a')]`

### Algorithms Implemented

- **Traversals**: BFS (`breadth_first_search.py`), DFS (`depth_first_search.py`)
  - DFS also computes topological ordering and detects cycles
  - Both compute arrival/departure timestamps
  
- **Shortest Paths**:
  - Dijkstra (`dijkstra.py`) — for non-negative weights
  - Bellman-Ford (`bellman_ford.py`) — handles negative weights, detects negative cycles
  - DAG shortest paths (`dag_shortest_paths.py`) — O(n+m) on directed acyclic graphs
  - A* search (`astar.py`) — recently added
  
- **Minimum Spanning Trees**:
  - Kruskal's algorithm (`kruskal.py`) — for undirected weighted graphs
  
- **Supporting**:
  - `priorityQueue.py` — wrapper around `collections.heapq` with entry finder and tie-breaking

### Project Characteristics

- **Flat module layout** — no package hierarchy, each algorithm in its own top-level file
- **Tests**: `tests/` directory with pytest fixtures
- **License**: Included (MIT)
- **No infrastructure** — no CI/CD, Docker, or release tooling (follows side-project convention)

The project is well-scoped for learning and practicing graph algorithms without the overhead of a production library.