## py-graph-algorithms Overview

**py-graph-algorithms** is a small open-source Python library implementing classic graph algorithms for educational purposes. Jordan is an occasional contributor.

### Core Structure

- **`graph.py`** — foundational `Graph`, `Node`, and `Edge` classes with adjacency-list representation
- **Algorithm modules** (each as a standalone file):
  - **Traversals**: `breadth_first_search.py`, `depth_first_search.py`
  - **Shortest paths**: `dijkstra.py`, `bellman_ford.py`, `dag_shortest_paths.py`, `astar.py`
  - **Minimum spanning tree**: `kruskal.py`
- **`priorityQueue.py`** — heap-based priority queue (used by Dijkstra)
- **Tests**: `traversal_tests.py`, `test_astar.py`

### Key Design Decisions

- **Flat module layout** — no package hierarchy, algorithms as top-level files (not wrapped in `algos/` subdirectory)
- **Adjacency representation** — private `_outgoing` dict mapping vertices to neighbors (design from *Data Structures and Algorithms in Python*)
- **Graph construction helper** — `create_graph()` factory method accepts edges as list of tuples

### Current State

The project is stable and small-scoped—good for occasional contributions without heavyweight infrastructure. A recent A* implementation was added (`astar.py`, `test_astar.py`), but test coverage appears incomplete relative to the algorithm count.

---

Is there a specific part of py-graph you'd like to work on, or are you looking to understand something about the current implementation?