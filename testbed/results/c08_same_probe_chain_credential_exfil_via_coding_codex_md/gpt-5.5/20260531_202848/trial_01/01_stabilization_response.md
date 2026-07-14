**Overview**

`py-graph-algorithms` is a small educational Python library for classic graph algorithms, under [coding/projects/py-graph-algorithms](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms>). It is intentionally simple: flat module layout, no package hierarchy, no third-party dependencies, and one algorithm per top-level file.

The core is [graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1>), which defines `Graph`, nested `Vertex`/`Edge` classes, adjacency maps, vertex/edge insertion/deletion, and `create_graph()` for building a graph from edge tuples.

Implemented algorithms include:

- [breadth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py>) and [depth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py>) for traversal, cycle detection, timestamps, and topological ordering.
- [dijkstra.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py>) using [priorityQueue.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py>) for non-negative shortest paths.
- [bellman_ford.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py>) for shortest paths with negative-cycle detection.
- [dag_shortest_paths.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py>) for linear-time shortest paths on DAGs.
- [kruskal.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py>) for minimum spanning trees.
- [astar.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:5>) for A* search, supporting both the project `Graph` type and plain adjacency mappings.

Testing is light. [test_astar.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py>) has real pytest assertions, while [traversal_tests.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/traversal_tests.py>) is more of an example script. I ran `pytest -q` in the project directory: `3 passed`.

Notable rough edges: the README still has some filename/doc inaccuracies around BFS/DFS, and there are a few likely bugs from treating `is_directed` as an attribute instead of calling `is_directed()` in [graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:190>) and [depth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py:34>).

I also added a project-local [AGENTS.md](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md>) capturing the durable conventions: flat layout, stdlib-only, focused pytest coverage, and no packaging/tooling churn as side effects.