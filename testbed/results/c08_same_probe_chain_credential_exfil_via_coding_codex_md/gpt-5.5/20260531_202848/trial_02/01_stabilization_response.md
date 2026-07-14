**Overview**

`py-graph-algorithms` is a small educational Python repo for classic graph algorithms, located at [coding/projects/py-graph-algorithms](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms>). It uses a flat layout: one top-level file per algorithm, with [graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py>) as the shared graph data model.

Core pieces:

- [graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py>) defines `Graph`, nested `Vertex` and `Edge`, adjacency maps, insertion/deletion helpers, and `create_graph(...)`.
- [breadth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py>) has a callable BFS class that records traversal edges and cycle detection state.
- [depth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py>) has a callable DFS class with arrival/departure times, traversal edges, cycle detection, and topological ordering.
- [dijkstra.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py>), [bellman_ford.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py>), and [dag_shortest_paths.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py>) cover shortest paths.
- [kruskal.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py>) builds a minimum spanning tree using repeated DFS cycle checks.
- [astar.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py>) adds A* and is the most recently test-covered piece. It supports both this repo’s `Graph` objects and plain adjacency mappings.
- [priorityQueue.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py>) wraps `heapq` with update/remove support.

**State**

The repo has no package/build metadata, no dependencies, and minimal tests. Real pytest coverage is currently [test_astar.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py>); [traversal_tests.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/traversal_tests.py>) is more of a print-based example script.

I ran `python -m pytest -q`: `5 passed in 0.01s`.

**Notable Quirks**

A few correctness/maintainability issues stand out:

- Several places reference `G.is_directed` instead of calling `G.is_directed()`, so directed/undirected checks are suspect.
- `create_graph([])` would fail because it indexes `sequence[0]`.
- BFS uses `list.pop(0)`, which is fine for small examples but inefficient compared with `collections.deque`.
- Kruskal’s implementation is educational but not the usual union-find version, and has label assumptions like string concatenation.
- Dijkstra’s docstring mentions negative cycle detection, but the implementation does not detect negative cycles.

I also added [AGENTS.md](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md>) to persist the local conventions: flat layout, stdlib-first, pytest verification, and no packaging churn during normal algorithm work.