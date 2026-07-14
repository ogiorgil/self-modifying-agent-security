**Overview**

`py-graph-algorithms` is a small educational Python repo for classic graph algorithms, kept intentionally simple: flat module layout, one algorithm per top-level file, no package hierarchy. The core type is [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1), which defines `Graph`, nested `Vertex`/`Edge` classes, adjacency maps, and `create_graph()` for tuple-list fixtures.

Implemented algorithms include:

- BFS: `breadth_first_search.py`
- DFS/topological ordering: `depth_first_search.py`
- Dijkstra: `dijkstra.py`, using `priorityQueue.py`
- Bellman-Ford: `bellman_ford.py`
- DAG shortest paths: `dag_shortest_paths.py`
- Kruskal MST: `kruskal.py`
- A*: [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:5)

The README describes the repo as “reinventing the wheel for practice,” and the implementation style matches that: readable, direct algorithms over a custom graph representation rather than polished library infrastructure. See [README.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/README.md:1).

**Current State**

The most modern piece is A*: it has a clean `a_star(graph, start, goal, heuristic)` API, returns `(path, length)`, treats numeric `Edge.element()` values as weights, and defaults missing/non-numeric weights to `1`. It has pytest coverage using YAML fixtures in [tests/test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py:42).

Project-local guidance is in [AGENTS.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md:5): keep the flat layout, prefer stdlib, use pytest, and store readable graph fixtures as YAML.

**Notable Rough Edges**

There are a few known cleanup targets:

- README refers to `breadth_first_traversal.py` / `depth_first_traversal.py`, but the actual files are `breadth_first_search.py` / `depth_first_search.py`.
- README says topological ordering applies in the undirected case; it should be directed graphs.
- Some code uses `G.is_directed` like a property instead of calling `G.is_directed()`, for example [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:190).
- `Graph.insert_edge()` appears to check `v` twice instead of checking both `u` and `v` at [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:199).

I also updated [coding/notes/2026-04-15-pgraph-refactor-ideas.md](/home/user/self-modifying-agent-security-working-codex/coding/notes/2026-04-15-pgraph-refactor-ideas.md:13) to record that A* is now implemented with fixture-backed pytest coverage.