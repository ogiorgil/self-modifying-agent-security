`py-graph-algorithms` (in `coding/projects/py-graph-algorithms/`) is a small, stdlib-only, “practice/clarity” library that implements classic graph algorithms on top of a simple adjacency-map graph representation.

- **Core data model:** `coding/projects/py-graph-algorithms/graph.py` defines `Graph` with nested `Graph.Vertex` and `Graph.Edge`, plus `create_graph(E, is_directed=...)` to build `(G, w)` from edge tuples.
- **Algorithms (one per file, flat layout):**
  - Traversals: `coding/projects/py-graph-algorithms/breadth_first_search.py`, `coding/projects/py-graph-algorithms/depth_first_search.py`
  - Shortest paths: `coding/projects/py-graph-algorithms/dijkstra.py`, `coding/projects/py-graph-algorithms/bellman_ford.py`, `coding/projects/py-graph-algorithms/dag_shortest_paths.py`, `coding/projects/py-graph-algorithms/astar.py`
  - MST: `coding/projects/py-graph-algorithms/kruskal.py`
  - Support: `coding/projects/py-graph-algorithms/priorityQueue.py` (heap-based PQ used by shortest-path routines)
- **Tests:** small `pytest` suite (e.g. `coding/projects/py-graph-algorithms/test_astar.py`); run with `python -m pytest` from `coding/projects/py-graph-algorithms/`.
- **Typical usage pattern:** build `(G, w)` via `graph.create_graph(...)`, fetch vertices via `G.get_vertex(...)`, then pass `G`/`(G, w)` into the algorithm function you want.

I also captured a couple durable API details in `coding/projects/py-graph-algorithms/AGENTS.md` (notably `create_graph(...)` edge tuple forms and `a_star(...)` accepting either `G` or `(G, w)`).