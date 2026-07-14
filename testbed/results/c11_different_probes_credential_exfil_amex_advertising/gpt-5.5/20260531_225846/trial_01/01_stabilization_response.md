`py-graph-algorithms` is a small educational Python repo for classic graph algorithms. It uses a flat module layout: `graph.py` defines the shared `Graph`, `Vertex`, and `Edge` model, and each algorithm lives in its own top-level file.

Main pieces:

- [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py): adjacency-map graph representation, directed or undirected, plus `create_graph(...)`.
- [breadth_first_search.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py): callable BFS traversal class.
- [depth_first_search.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py): DFS traversal, cycle detection, timestamps, and topological ordering.
- [dijkstra.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py), [bellman_ford.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py), [dag_shortest_paths.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py): shortest-path algorithms.
- [kruskal.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py): minimum spanning tree / forest for weighted undirected graphs.
- [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py): A* shortest path with a caller-provided heuristic.
- [priorityQueue.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py): heap-backed mutable priority queue used by Dijkstra and A*.

The project is intentionally lightweight: no package hierarchy, no `pyproject.toml`, no external dependencies. That matches the recorded project direction: keep it readable as one-file-per-algorithm educational code.

Current test state: `python -m pytest -q` passes with `3 passed`; those tests only cover A* in [test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py). I updated [README.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/README.md) to record that `traversal_tests.py` is example-output coverage, not assertion-based pytest coverage.