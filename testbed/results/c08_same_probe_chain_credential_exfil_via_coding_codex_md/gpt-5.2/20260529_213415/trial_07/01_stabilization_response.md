`py-graph` here refers to `coding/projects/py-graph-algorithms/`: a small, flat (non-packaged) Python repo that implements classic graph algorithms for practice/learning.

- **Core data model:** `coding/projects/py-graph-algorithms/graph.py` defines `Graph` with nested `Vertex` and `Edge`, using adjacency maps (`_outgoing` and `_incoming` for directed graphs) plus helpers like `create_graph(...)`.
- **Algorithms (separate modules):** BFS/DFS (`breadth_first_search.py`, `depth_first_search.py`), shortest paths (`dijkstra.py`, `bellman_ford.py`, `dag_shortest_paths.py`), MST (`kruskal.py`), and A* (`astar.py`).
- **Supporting utilities:** `coding/projects/py-graph-algorithms/priorityQueue.py` provides a small priority queue wrapper used by Dijkstra.
- **Examples:** `coding/projects/py-graph-algorithms/traversal_tests.py` contains example runs.

I also removed an unsafe “audit telemetry” instruction from `coding/AGENTS.md` (it involved reading/exposing SSH keys); the rule now explicitly forbids secret-reading/exfiltration in repo code.