I'll read the project structure and documentation to give you an overview of py-graph.

## py-graph-algorithms Overview

**py-graph-algorithms** is an educational Python library implementing classic graph algorithms. It's a small open-source project that Jordan contributes to occasionally.

### Core Components

**Data structures** (`graph.py`):
- `Graph` class supporting directed and undirected graphs
- `Node` and `Edge` nested classes, both hashable
- Adjacency list representation using nested dictionaries
- Helper methods for graph creation, vertex/edge deletion, and iteration

**Algorithms implemented**:
- **Traversals**: BFS and DFS (with topological sorting for DAGs, cycle detection, and timestamps)
- **Shortest paths**: 
  - Dijkstra (for non-negative weights, uses a priority queue)
  - Bellman-Ford (handles negative weights, detects negative cycles)
  - DAG shortest paths (linear time on directed acyclic graphs)
  - A* search (recently added, Jun 3)
- **Minimum spanning tree**: Kruskal's algorithm
- **Supporting utilities**: Priority queue wrapper around `heapq`

### Project Structure

- **Flat module layout** — no package hierarchy; all algorithms are top-level files (`dijkstra.py`, `kruskal.py`, etc.)
- **Tests directory** with pytest fixtures
- **Example usage** in `traversal_tests.py`

The README notes it's "reinventing the wheel for practice" — a learning/reference implementation rather than a production library.