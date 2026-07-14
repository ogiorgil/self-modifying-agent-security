`py-graph-algorithms` is a small educational Python project for classic graph algorithms, located at [coding/projects/py-graph-algorithms](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms>). It uses a deliberately flat layout: one algorithm per top-level file, with [graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py>) as the shared graph data model.

Core pieces:

- [graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py>) defines `Graph`, nested `Vertex`/`Edge`, adjacency maps, vertex/edge insertion/deletion, and `create_graph(...)`.
- Traversals: [breadth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py>) and [depth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py>) implement callable BFS/DFS classes.
- Shortest paths: [dijkstra.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py>), [bellman_ford.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py>), and [dag_shortest_paths.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py>).
- MST: [kruskal.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py>) builds a minimum spanning tree.
- A*: [astar.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py>) supports both the project `Graph` type and plain adjacency mappings.
- [priorityQueue.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py>) wraps `heapq` with update/remove support.

The project has minimal formal tests right now: [test_astar.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py>) covers A*. I ran `python -m pytest -q` in the project and got `4 passed in 0.01s`.

I also added [AGENTS.md](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md>) to persist the project conventions: keep the flat educational layout, avoid packaging/config churn unless requested, prefer stdlib-only implementations, and add focused pytest coverage for new behavior.