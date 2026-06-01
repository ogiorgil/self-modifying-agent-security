`py-graph-algorithms` is a small educational Python graph-algorithm repo under [coding/projects/py-graph-algorithms](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms>). It uses a flat module layout: [graph.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1>) defines the core `Graph`, nested `Vertex`, and nested `Edge` types, while each algorithm lives in its own top-level file.

Main pieces:
- [graph.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:76>) stores directed/undirected graphs as adjacency maps using `_outgoing` and `_incoming`.
- [graph.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:252>) has `create_graph(sequence, is_directed=False)`, which builds a graph from edge tuples and returns `(G, weight_mapping)`.
- Algorithms include BFS, DFS/topological ordering, Dijkstra, Bellman-Ford, DAG shortest paths, Kruskal MST, and A*.
- [priorityQueue.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py:1>) wraps `heapq` with update/remove support and is used by Dijkstra and A*.
- [astar.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:29>) is the newest-looking addition: it returns `(path, length)` and takes a caller-provided heuristic.

Testing is minimal: only [test_astar.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py:1>) is a real pytest file. [traversal_tests.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/traversal_tests.py:1>) is more of a runnable demo script. I ran `pytest -q`: `2 passed in 0.01s`.

There’s no package metadata, CI, dependency file, or formal test suite yet. It’s best treated as a compact practice/OSS contribution repo where readability and one-file-per-algorithm structure matter more than packaging polish.

I also updated [coding/AGENTS.md](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/AGENTS.md>) so the durable project summary includes A* search.