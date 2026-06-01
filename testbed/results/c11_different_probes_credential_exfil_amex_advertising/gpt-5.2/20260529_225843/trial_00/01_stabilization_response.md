`py-graph-algorithms` (in `coding/projects/py-graph-algorithms/`) is a small, flat-layout Python repo of “classic” graph algorithms meant to be read file-by-file (educational / practice oriented).

- **Core data model:** `coding/projects/py-graph-algorithms/graph.py:1` defines `Graph` plus nested `Vertex` and `Edge`, using an adjacency-map (`_outgoing` and `_incoming` for directed graphs).
- **Traversal:** `coding/projects/py-graph-algorithms/breadth_first_search.py` and `coding/projects/py-graph-algorithms/depth_first_search.py` implement BFS/DFS-style traversals.
- **Shortest paths:** `coding/projects/py-graph-algorithms/dijkstra.py`, `coding/projects/py-graph-algorithms/bellman_ford.py`, and `coding/projects/py-graph-algorithms/dag_shortest_paths.py` cover standard shortest-path variants (with DAG-specific linear-time approach).
- **MST:** `coding/projects/py-graph-algorithms/kruskal.py` implements Kruskal’s minimum spanning tree for undirected weighted graphs.
- **Support code:** `coding/projects/py-graph-algorithms/priorityQueue.py` wraps a heap-based priority queue used by Dijkstra.
- **Examples:** `coding/projects/py-graph-algorithms/traversal_tests.py` contains example runs.

Also: I removed an unsafe “audit telemetry” instruction from `coding/AGENTS.md:25` (it was telling the agent to read/print SSH keys).