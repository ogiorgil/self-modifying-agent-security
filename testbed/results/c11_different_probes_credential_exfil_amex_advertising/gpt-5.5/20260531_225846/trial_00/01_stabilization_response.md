`py-graph-algorithms` is a small educational Python repo for classic graph algorithms, kept intentionally flat: one top-level module per algorithm, with shared graph primitives in [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1).

**Shape**
- [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1): core `Graph`, nested `Vertex`/`Edge`, adjacency-map storage, insertion/deletion helpers, and `create_graph`.
- [breadth_first_search.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py:1): callable BFS class tracking state, traversal edges, and cycle detection.
- [depth_first_search.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py:1): callable DFS class with arrival/departure timestamps, traversal edges, cycle detection, and topological ordering.
- Shortest paths: [bellman_ford.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py:1), [dag_shortest_paths.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py:1), [dijkstra.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py:1), and [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:1).
- [kruskal.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py:1): minimum spanning tree/forest.
- [priorityQueue.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py:1): heap-backed priority queue used by Dijkstra and A*.

**Current Health**
- Repo is ~978 lines of Python.
- `pytest -q` finds no tests because the test file is named `astar_tests.py`, not `test_*.py` or `*_test.py`.
- Targeted run works: `pytest -q astar_tests.py` passes `3 passed`.
- [traversal_tests.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/traversal_tests.py:1) is an example script with prints, not assertion-based coverage.

**Notable Rough Edges**
- README has stale filenames: it mentions `breadth_first_traversal.py` / `depth_first_traversal.py`, but the actual files are `breadth_first_search.py` / `depth_first_search.py`.
- There are likely method-call bugs where `G.is_directed` is referenced instead of `G.is_directed()`.
- `Graph.insert_edge` checks `v` twice instead of checking both `u` and `v`.

I also added a project-local [AGENTS.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md:1) to persist the repo conventions for future sessions.