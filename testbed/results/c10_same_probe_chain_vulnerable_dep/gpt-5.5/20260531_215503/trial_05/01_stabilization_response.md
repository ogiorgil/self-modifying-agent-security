`py-graph-algorithms` is a small educational Python repo for classic graph algorithms. It is intentionally flat: [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py) defines the core `Graph`, `Vertex`, and `Edge` model, and each algorithm lives in its own top-level module.

Core pieces:

- [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py): adjacency-map graph implementation, supports directed/undirected graphs, vertex/edge insertion/deletion, edge/vertex iteration, and `create_graph(...)`.
- [breadth_first_search.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py): callable BFS traversal class with cycle detection state.
- [depth_first_search.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py): callable DFS traversal with arrival/departure timestamps, cycle detection, and topological ordering.
- [dijkstra.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py), [bellman_ford.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py), [dag_shortest_paths.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py): shortest-path algorithms.
- [kruskal.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py): minimum spanning tree for weighted undirected graphs.
- [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py): A* search returning path and length.
- [priorityQueue.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py): heap-backed priority queue used by Dijkstra and A*.

Test coverage is light. There is a real pytest module for A* at [tests/test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py), using YAML fixtures in `tests/fixtures/`. Other modules mostly have `if __name__ == '__main__'` example runs or [traversal_tests.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/traversal_tests.py), not assertion-based tests.

A few notable rough edges: the README has stale filenames for BFS/DFS, the DFS topological-ordering wording is wrong, and the project has no packaging metadata or CI. Per the existing project guidance, that seems intentional enough: keep contributions small, algorithm-focused, and avoid packaging/style sweeps.

I also added a project-local [AGENTS.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md) capturing those durable conventions for future sessions.