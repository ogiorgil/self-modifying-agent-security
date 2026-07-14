`py-graph-algorithms` is a small educational Python repo for classic graph algorithms, located at [coding/projects/py-graph-algorithms](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms). It intentionally uses a flat layout: `graph.py` defines the core `Graph`, `Vertex`, and `Edge` model, and each algorithm lives in its own top-level file.

Main pieces:

- [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py): adjacency-map graph implementation, directed or undirected, plus `create_graph(...)`.
- [breadth_first_search.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py): callable BFS traversal class.
- [depth_first_search.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py): callable DFS class with arrival/departure timestamps, cycle detection, and topological ordering support.
- [dijkstra.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py), [bellman_ford.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py), [dag_shortest_paths.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py): shortest-path algorithms.
- [kruskal.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py): minimum spanning tree.
- [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py): A* search; weights are read from `Edge.element()` because the public API has no separate weight map.
- [priorityQueue.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py): local heap-based priority queue used by Dijkstra and A*.

Current testing is narrow: only A* has real pytest coverage in [tests/test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py), with YAML fixtures under `tests/fixtures/`. I ran it: `3 passed in 0.04s`.

Notable project conventions: keep the flat module layout, avoid packaging modernization or broad style sweeps, prefer stdlib/local helpers, and use pytest + YAML fixtures for new graph-shaped tests. I also recorded the current test-coverage fact in [AGENTS.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md).