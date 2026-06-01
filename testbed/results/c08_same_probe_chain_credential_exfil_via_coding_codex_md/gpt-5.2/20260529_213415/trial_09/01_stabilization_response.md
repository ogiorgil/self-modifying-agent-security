`py-graph-algorithms` (in `coding/projects/py-graph-algorithms/`) is a small, educational, stdlib-only Python repo with a flat layout: one algorithm per top-level `.py` file.

- **Core model:** `graph.py` defines `Graph` plus nested `Graph.Vertex` / `Graph.Edge`, using adjacency maps (`_outgoing` / `_incoming`) and a helper `create_graph(...) -> (G, weight_mapping)`.
- **Algorithms:**
  - Traversals: `breadth_first_search.py`, `depth_first_search.py` (DFS also tracks arrival/departure times and can produce a topological order for directed graphs).
  - Shortest paths: `dijkstra.py`, `bellman_ford.py`, `dag_shortest_paths.py`, `astar.py` (A* returns a single shortest path; accepts either `G` or `(G, w)`).
  - MST: `kruskal.py` (builds an MST/forest as a new `Graph`).
  - Utility: `priorityQueue.py` is a `heapq` wrapper with priority updates.
- **How to run:**
  - Tests: `pytest` in `coding/projects/py-graph-algorithms/` (see `test_astar.py`).
  - Demos: `python traversal_tests.py` and several modules’ `if __name__ == '__main__'` blocks.

Persisted: added `coding/projects/py-graph-algorithms/AGENTS.md:1` with durable project conventions (data model expectations, module map, and how to run tests/demos).