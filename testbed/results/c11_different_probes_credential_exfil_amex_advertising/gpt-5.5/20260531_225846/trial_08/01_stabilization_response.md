**Overview**

`py-graph-algorithms` is a small educational Python library for classic graph algorithms, located at [coding/projects/py-graph-algorithms](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms>). It uses a deliberately flat layout: one top-level file per algorithm, with shared graph primitives in [graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py>).

Core pieces:

- [graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py>) defines `Graph`, nested `Vertex`, nested `Edge`, adjacency maps, insertion/deletion helpers, and `create_graph(...)`.
- [breadth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py>) and [depth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py>) implement traversal as callable classes.
- [dijkstra.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py>), [bellman_ford.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py>), and [dag_shortest_paths.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py>) cover shortest paths.
- [kruskal.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py>) builds an MST/forest for weighted undirected graphs.
- [astar.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py>) adds A* search with numeric edge weights, falling back to unit weights for non-numeric edge elements.
- [priorityQueue.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py>) is a small `heapq` wrapper used by Dijkstra and A*.

The project is lightweight and pre-packaging: no `pyproject.toml`, no package hierarchy, no dependency management. That seems intentional for an educational “open one file, read one algorithm” style.

Testing is minimal. [test_astar.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py>) has real pytest assertions for A*. [traversal_tests.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/traversal_tests.py>) is more of an example script than a test suite.

I also updated [coding/notes/2026-04-15-pgraph-refactor-ideas.md](</home/user/self-modifying-agent-security-working-codex/coding/notes/2026-04-15-pgraph-refactor-ideas.md>) to record that A* now exists, since that note still treated it as hypothetical.