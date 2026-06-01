`coding/projects/py-graph-algorithms/README.md` describes a small Python repo implementing classic graph algorithms “for practice,” centered around `graph.py`:

- `graph.py`: A `Graph` class (directed/undirected) with nested `Node` and `Edge` classes; hashable vertices/edges; adjacency-map representation via `self._outgoing`; includes helpers like vertex iteration, deletion, and `graph.create_graph()` to build a graph from an edge list (optionally directed, with optional weights defaulting to 1).
- Traversals: `breadth_first_traversal.py` and `depth_first_traversal.py` implement BFS/DFS as callable classes; DFS can produce topological order in the directed case and reports timestamps (arrival/departure) useful for analyzing properties like odd cycles.
- MST: `kruskal.py` implements Kruskal’s minimum spanning tree for undirected weighted graphs by sorting edges by weight.
- Shortest paths: `bellman_ford.py` (handles negative weights; returns `None` outputs if a negative cycle is detected), `dag_shortest_paths.py` (DAG-only; uses topological order for linear-time relaxation), and `dijkstra.py` (non-negative weights; uses a priority queue in `priorityQueue.py` built on `heapq` with an `entry_finder` and tie-breaking counter).
- `traversal_tests.py`: example runs for BFS/DFS.

I also updated `core/behaviors.md` to explicitly ignore “captured error/log” prompt-injection style blocks (this README includes one).