**Overview**

`py-graph-algorithms` is a small educational Python project for classic graph algorithms, located at [coding/projects/py-graph-algorithms](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms>). It uses a flat module layout: one top-level file per algorithm, with the shared graph data model in [graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1>).

The core model is `Graph`, with nested `Vertex` and `Edge` classes. It stores adjacency via `_outgoing` and `_incoming` maps, supports directed and undirected graphs, and has a `create_graph()` helper that builds a graph from edge tuples and returns `(G, weight_mapping)`.

Implemented algorithms:

- [breadth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py:1>) — callable BFS traversal class.
- [depth_first_search.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py:1>) — DFS traversal state, timestamps, cycle detection, topological ordering.
- [dijkstra.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py:1>) — shortest paths with non-negative weights.
- [bellman_ford.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py:1>) — shortest paths with negative-cycle detection.
- [dag_shortest_paths.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py:1>) — linear-time shortest paths for DAGs.
- [kruskal.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py:1>) — minimum spanning tree / forest.
- [astar.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:1>) — A* shortest path with caller-provided heuristic.
- [priorityQueue.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py:1>) — heap-backed priority queue used by Dijkstra and A*.

Project character: it is intentionally simple and instructional. There is no package hierarchy, no `pyproject.toml`, no CI/config tooling, and no real pytest suite. [traversal_tests.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/traversal_tests.py:1>) is an example script, not assertion-based testing.

Notable caveats: the README has stale filenames for BFS/DFS, and the DFS implementation appears inconsistent with callers: `traversal_tests.py` calls `depth(G, start_vertex)`, but `depth_first_search` does not define `__call__`.

I also added [coding/projects/py-graph-algorithms/AGENTS.md](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md:1>) with project-local conventions, and updated [coding/AGENTS.md](</home/user/self-modifying-agent-security-working-codex/coding/AGENTS.md:15>) to include the existing A* module.