I'll explore the project structure to give you an overview.

## py-graph-algorithms Overview

**py-graph-algorithms** is a classic algorithms educational library implementing graph algorithms from first principles in Python (for learning/practice, not production use).

### Core Structure

**`graph.py`** — The foundation
- `Graph()` class supporting both directed and undirected graphs
- Nested `Node` and `Edge` classes (made hashable)
- Adjacency representation via nested dictionaries (`_outgoing` map)
- `create_graph()` helper to instantiate from edge lists
- Based on *Data Structures and Algorithms in Python* (Goodrich, Tamassia, Goldwasser)

### Algorithms

**Search/Traversal:**
- `breadth_first_search.py` — BFS with vertex iterator support
- `depth_first_search.py` — DFS with topological ordering and arrival/departure timestamps

**Shortest Paths:**
- `dijkstra.py` — Non-negative weights; uses a priority queue
- `bellman_ford.py` — Handles negative weights; detects negative cycles
- `dag_shortest_paths.py` — Linear-time for DAGs via topological order

**Minimum Spanning Tree:**
- `kruskal.py` — Classic MST for undirected weighted graphs

**A\* Search:**
- `astar.py` — Added recently (June 2); heuristic-based pathfinding

**Supporting:**
- `priorityQueue.py` — Custom heap wrapper (heapq-based) with tie-breaking
- `traversal_tests.py` — Example runs, not formal test assertions

### Known Issues

The README has minor discrepancies (references `breadth_first_traversal` instead of `breadth_first_search`; docs say topo-order works on undirected graphs when it only makes sense on DAGs).

### Your Role

You're an occasional contributor. The project's philosophy favors classic CLRS algorithms. Small, atomic PRs are welcome (docs fixes, type hints); larger changes like A* or pytest infrastructure would need maintainer buy-in first.