`py-graph` appears to be [py-graph-algorithms](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/README.md): a small educational Python repo implementing classic graph algorithms with a flat, one-file-per-algorithm layout.

**Shape**
- [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py) defines the core `Graph`, nested `Vertex`, and nested `Edge` classes.
- Graph storage is adjacency-map based: vertices map to neighboring vertices, which map to edge objects.
- `create_graph()` builds a graph from edge tuples and returns `(Graph, weight_mapping)`.

**Algorithms Present**
- [breadth_first_search.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py): callable BFS traversal class.
- [depth_first_search.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py): callable DFS with timestamps, cycle detection, and topological order support.
- [dijkstra.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py): shortest paths with non-negative weights.
- [bellman_ford.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py): shortest paths with negative-cycle detection.
- [dag_shortest_paths.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py): DAG shortest paths via topological ordering.
- [kruskal.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py): minimum spanning tree / forest.
- [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py): A* shortest path search.
- [priorityQueue.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py): heap-based priority queue used by Dijkstra and A*.

**Project State**
The project is intentionally lightweight: no package hierarchy, no `pyproject.toml`, no external dependencies. It has one real pytest module, [test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py), and [traversal_tests.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/traversal_tests.py) is more of an executable demo.

I also added [AGENTS.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md) to persist the project conventions for future sessions.

Verification: `python -m pytest -q` passes: `3 passed`.