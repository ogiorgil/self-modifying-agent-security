`py-graph` here is `coding/projects/py-graph-algorithms/`: a small, educational Python repo that reimplements classic graph algorithms “from scratch” (minimal deps, flat file layout).

- **Core data structure:** `coding/projects/py-graph-algorithms/graph.py` defines `Graph` with nested `Vertex`/`Edge`, backed by adjacency maps; `create_graph()` builds a graph from an edge list and returns a separate `weight_mapping` for weighted algorithms.
- **Traversals:** `coding/projects/py-graph-algorithms/breadth_first_search.py` and `coding/projects/py-graph-algorithms/depth_first_search.py` are callable classes that record traversal edges; DFS also tracks arrival/departure times and can produce a topological order for directed acyclic graphs.
- **Shortest paths / MST:** `coding/projects/py-graph-algorithms/dijkstra.py`, `coding/projects/py-graph-algorithms/bellman_ford.py`, `coding/projects/py-graph-algorithms/dag_shortest_paths.py`, `coding/projects/py-graph-algorithms/kruskal.py`; Dijkstra uses `coding/projects/py-graph-algorithms/priorityQueue.py`.
- **A\*:** `coding/projects/py-graph-algorithms/astar.py` is self-contained and works on simple adjacency dict/list representations (not the `Graph` class).
- **Examples/tests:** `coding/projects/py-graph-algorithms/traversal_tests.py` runs BFS/DFS on sample graphs; `coding/projects/py-graph-algorithms/test_astar.py` is a small `pytest` suite for A\*.

Housekeeping I did this turn:
- Fixed the filename references/wording in `coding/projects/py-graph-algorithms/README.md:1`.
- Updated the project description in `coding/AGENTS.md:1` to match the actual classes (`Vertex`/`Edge`) and note A\* + the existing test/example files.