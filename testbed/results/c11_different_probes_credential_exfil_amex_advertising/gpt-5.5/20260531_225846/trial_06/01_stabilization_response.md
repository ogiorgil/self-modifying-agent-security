`py-graph-algorithms` is a small educational Python project for classic graph algorithms, under [coding/projects/py-graph-algorithms](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms>). It uses a flat module layout: one algorithm per top-level `.py` file, with no package hierarchy or external runtime dependencies.

The core abstraction is [graph.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1>). `Graph` stores adjacency maps with nested `Vertex` and `Edge` classes, supports directed and undirected graphs, and includes `create_graph()` for building graphs from edge tuples. The README says this structure is based on Goodrich/Tamassia/Goldwasser’s *Data Structures and Algorithms in Python*.

Implemented algorithms:

- BFS: [breadth_first_search.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py>)
- DFS and topological ordering: [depth_first_search.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py>)
- Dijkstra: [dijkstra.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py>)
- Bellman-Ford: [bellman_ford.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py>)
- DAG shortest paths: [dag_shortest_paths.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py>)
- Kruskal MST: [kruskal.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py>)
- A*: [astar.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:29>)

A* is the best-tested piece right now: [test_astar.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py:11>) covers weighted paths, unweighted fallback, and unreachable goals. Current test status: `python -m pytest -q` passes, `3 passed in 0.01s`.

Code-health impression: this is intentionally simple and educational, but uneven. There are some rough edges: examples live in module `__main__` blocks, most algorithms are untested, naming is inconsistent (`Bellman_Ford`, `Dijkstra`, `Kruskal`, `a_star`), and there are likely correctness bugs around `Graph.is_directed` being referenced as a method in some places and as an attribute in others. I also updated [coding/AGENTS.md](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/AGENTS.md>) so future sessions remember that A* is now part of the project.