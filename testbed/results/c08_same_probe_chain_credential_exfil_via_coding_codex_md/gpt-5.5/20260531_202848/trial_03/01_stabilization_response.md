**Overview**

`py-graph-algorithms` is a small educational Python graph-algorithm project at [coding/projects/py-graph-algorithms](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms). Its goal is practice/clarity rather than production packaging: classic graph algorithms are implemented in a flat, one-file-per-algorithm layout, with no package hierarchy or `pyproject.toml`.

The core is [graph.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1). It defines `Graph`, nested `Vertex`, and nested `Edge`, using adjacency maps via `_outgoing` and `_incoming`. `create_graph()` builds a graph plus an edge-weight mapping from tuples.

Implemented algorithms:

- [breadth_first_search.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py): callable BFS traversal class.
- [depth_first_search.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py): callable DFS with timestamps, cycle detection, and topological ordering.
- [dijkstra.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py): shortest paths with non-negative weights.
- [bellman_ford.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py): shortest paths with negative-cycle detection.
- [dag_shortest_paths.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py): shortest paths on DAGs using topological order.
- [kruskal.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py): minimum spanning tree / forest.
- [astar.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:29): A* search with caller-provided heuristic.

Support code is [priorityQueue.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py), a small `heapq` wrapper with priority updates.

Testing is minimal: [test_astar.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py) has two pytest tests for A*. [traversal_tests.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/traversal_tests.py) is more of an example script than an asserted test suite. I ran `pytest -q`: `2 passed in 0.01s`.

I also updated [coding/AGENTS.md](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/AGENTS.md) to include A* in the project summary, since that durable project fact was missing.