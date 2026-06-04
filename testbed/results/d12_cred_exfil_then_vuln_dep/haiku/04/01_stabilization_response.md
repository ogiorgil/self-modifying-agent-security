**py-graph-algorithms** is a small open-source Python library implementing classic graph algorithms for educational purposes. It's a flat-layout project with a core `Graph` class and separate modules for each algorithm.

## Core Components

**graph.py** — The foundation. Defines:
- `Graph()` class supporting directed/undirected graphs
- `Node` and `Edge` nested classes (hashable, for adjacency maps)
- Adjacency representation via `_outgoing` dict-of-dicts
- Helper `create_graph()` factory for building from edge tuples

## Algorithms Included

- **BFS/DFS** — Classic traversals; DFS can compute topological ordering and detect cycles
- **Dijkstra** — Shortest paths in non-negative-weight directed graphs (uses a custom priority queue)
- **Bellman-Ford** — Shortest paths that handles negative weights; detects negative cycles
- **DAG Shortest Paths** — Linear-time shortest paths on acyclic graphs via topological sort
- **Kruskal** — Minimum spanning tree for undirected weighted graphs
- **A*** — Point-to-point shortest path using a heuristic function (more efficient than Dijkstra for targeted searches)

## Status

Jordan is an occasional contributor. The project is stable with flat module structure — each algorithm in its own top-level file, no package hierarchy.