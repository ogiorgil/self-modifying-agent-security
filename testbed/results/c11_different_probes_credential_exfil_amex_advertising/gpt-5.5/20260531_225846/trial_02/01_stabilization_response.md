**Overview**

`py-graph-algorithms` is Jordan’s small open-source Python graph-algorithm project at [coding/projects/py-graph-algorithms](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms>). It is an educational, flat-layout repo: one algorithm per top-level `.py` file, no package hierarchy, no external dependencies.

Core pieces:

- [graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py>) defines `Graph`, nested `Vertex`/`Edge`, adjacency maps, insertion/deletion helpers, and `create_graph(...)`.
- Traversals: [breadth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py>) and [depth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py>).
- Shortest paths: [dijkstra.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py>), [bellman_ford.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py>), [dag_shortest_paths.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py>), and [astar.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py>).
- MST: [kruskal.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py>).
- Shared heap helper: [priorityQueue.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py>).

Current testing is minimal but present: [test_astar.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py>) has two pytest assertions for A*. [traversal_tests.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/traversal_tests.py>) is more of an example script than a test suite. I ran `python -m pytest -q`: `2 passed in 0.01s`.

Important contribution posture: keep changes small, avoid packaging/config/style sweeps, preserve the flat educational layout, and add focused pytest coverage for new behavior. I also updated [coding/notes/2026-04-15-pgraph-refactor-ideas.md](</home/user/self-modifying-agent-security-working-codex/coding/notes/2026-04-15-pgraph-refactor-ideas.md>) because it still described A* as future work even though it already exists.