**Overview**

`py-graph-algorithms` is Jordan’s small educational Python library for classic graph algorithms. It is intentionally flat and dependency-light: [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py) defines the shared `Graph`, `Vertex`, and `Edge` model, and each algorithm lives in its own top-level file.

Main pieces:

- [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py): adjacency-map graph representation, directed or undirected, plus `create_graph(...)`.
- Traversals: [breadth_first_search.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py), [depth_first_search.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py).
- Shortest paths: [dijkstra.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py), [bellman_ford.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py), [dag_shortest_paths.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py), [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py).
- MST: [kruskal.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py).
- Utility: [priorityQueue.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py), a `heapq` wrapper used by Dijkstra and A*.

The repo is more “practice / readable algorithm implementations” than polished package: no `pyproject.toml`, no package hierarchy, sparse tests, and several files include script-style examples. Current real pytest coverage is just A*, in [test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py).

I also added a project-level [AGENTS.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md) capturing the durable conventions for future sessions. Verification: `python -m pytest -q` passes, `2 passed in 0.01s`.