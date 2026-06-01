`py-graph-algorithms` is a small educational Python library for classic graph algorithms, located at [coding/projects/py-graph-algorithms](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms>).

Core shape:

- [graph.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py>) defines the main `Graph`, nested `Vertex`, and nested `Edge` classes using an adjacency-map representation.
- Algorithms are flat top-level modules: BFS, DFS, Dijkstra, Bellman-Ford, DAG shortest paths, Kruskal MST, and A*.
- [priorityQueue.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py>) is a small heap-based priority queue used by Dijkstra.
- [astar.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py>) is the most modern-looking module: typed public function, supports adjacency mappings and `Graph` objects, and has pytest coverage.
- [tests/test_astar.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py>) is currently the only pytest test module. `traversal_tests.py` is an example script.

The project intentionally favors readability over infrastructure: no package hierarchy, no `pyproject.toml`, no CI/lint config, and one algorithm per file. That matches the recorded project decision to keep the educational “open one file, understand one algorithm” style.

I also added [AGENTS.md](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md>) for the project with the local conventions I verified.