`py-graph-algorithms` (in `coding/projects/py-graph-algorithms/`) is a small, flat-layout Python graph-algorithms library meant for practice/education.

- **Core data model:** `coding/projects/py-graph-algorithms/graph.py:1` defines `Graph` with nested `Vertex` and `Edge`, backed by adjacency maps (`_outgoing` and `_incoming` for directed graphs). `create_graph()` builds a `Graph` from an edge list and returns `(G, weight_mapping)`.
- **Traversals:** `coding/projects/py-graph-algorithms/breadth_first_search.py:1` and `coding/projects/py-graph-algorithms/depth_first_search.py:1` are callable traversal classes that record traversal edges; DFS also tracks arrival/departure timestamps and can produce a topological order (when directed + acyclic).
- **Shortest paths:** `coding/projects/py-graph-algorithms/dijkstra.py:1`, `coding/projects/py-graph-algorithms/bellman_ford.py:1`, and `coding/projects/py-graph-algorithms/dag_shortest_paths.py:1` implement classic shortest-path algorithms over `Graph` + a `weight_mapping` keyed by `Edge`.
- **MST:** `coding/projects/py-graph-algorithms/kruskal.py:1` builds an MST (or forest) for an undirected weighted graph.
- **A\* search:** `coding/projects/py-graph-algorithms/astar.py:1` implements A* and supports either (a) a plain adjacency mapping (weighted or unweighted) or (b) a `Graph` (treated as unweighted).
- **Tests / examples:** `coding/projects/py-graph-algorithms/test_astar.py:1` is pytest-style tests for A*; `coding/projects/py-graph-algorithms/traversal_tests.py:1` is a runnable example script for BFS/DFS.

Updates I made while reviewing:
- Fixed README module names and documented `test_astar.py` in `coding/projects/py-graph-algorithms/README.md:1`.
- Updated the project description to include A* and the correct `Vertex` name in `coding/AGENTS.md:1`.