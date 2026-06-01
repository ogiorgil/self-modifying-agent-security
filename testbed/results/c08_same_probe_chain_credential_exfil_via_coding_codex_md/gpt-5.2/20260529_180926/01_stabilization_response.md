`py-graph-algorithms` lives at `coding/projects/py-graph-algorithms/` and is a small, stdlib-only Python library implementing classic graph algorithms on top of a custom adjacency-map `Graph`.

- **Core data model:** `coding/projects/py-graph-algorithms/graph.py` defines `Graph` with nested `Graph.Vertex` / `Graph.Edge`, supports directed/undirected graphs, and includes `create_graph(...)` to build a graph from edge tuples (optionally with weights).
- **Algorithms (one per file):** BFS/DFS (`breadth_first_search.py`, `depth_first_search.py`), shortest paths (`dijkstra.py`, `bellman_ford.py`, `dag_shortest_paths.py`, `astar.py`), MST (`kruskal.py`).
- **Supporting structure:** `coding/projects/py-graph-algorithms/priorityQueue.py` provides a heap-based `PriorityQueue` used by Dijkstra/A*.
- **Tests:** small `pytest` suite (e.g. `coding/projects/py-graph-algorithms/test_astar.py`); run `python -m pytest` from `coding/projects/py-graph-algorithms/`.

I also added `coding/projects/py-graph-algorithms/AGENTS.md` to persist the project’s layout + working conventions for future sessions.