`py-graph-algorithms` is a small educational Python library for classic graph algorithms. The core model is [graph.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py): a simple adjacency-map `Graph` with nested `Vertex` and `Edge` classes, plus `create_graph()` for building graphs from edge tuples.

The project is intentionally flat: one top-level file per algorithm. Current algorithms include BFS, DFS/topological ordering, Dijkstra, Bellman-Ford, DAG shortest paths, Kruskal MST, and A* search. `priorityQueue.py` provides the heap-backed queue used by Dijkstra and A*.

A few important conventions:

- It is MIT licensed.
- It favors readable, dependency-free, stdlib-first Python.
- It should keep the flat module layout rather than becoming a package hierarchy.
- Packaging modernization is considered out of scope for ordinary algorithm contributions.
- Real tests use `pytest`; currently only `test_astar.py` has assertion-based tests. `traversal_tests.py` is more of an example script.

Current health: `pytest -q` passes with `3 passed`.

I also added [AGENTS.md](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md) inside the project to persist those local contributor rules for future sessions.