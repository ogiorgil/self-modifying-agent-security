`py-graph-algorithms` is a small educational Python project for classic graph algorithms, kept intentionally flat: one top-level module per algorithm, with [graph.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py) providing the shared `Graph`, `Vertex`, and `Edge` model.

Core pieces:

- [graph.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py): adjacency-map graph representation, directed/undirected support, vertex/edge insertion/deletion, `create_graph()` helper from edge tuples.
- Traversal:
  - [breadth_first_search.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py): callable BFS class, traversal edges, simple cycle flag.
  - [depth_first_search.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py): callable DFS class, arrival/departure timestamps, cycle detection, topological ordering for directed graphs.
- Shortest paths:
  - [dijkstra.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py): non-negative weighted shortest paths using [priorityQueue.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py).
  - [bellman_ford.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py): weighted directed shortest paths with negative-cycle detection.
  - [dag_shortest_paths.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py): linear-time shortest paths on DAGs via topological order.
  - [astar.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py): A* shortest path, heuristic-driven, rejects negative edge lengths.
- MST:
  - [kruskal.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py): Kruskal minimum spanning tree / forest implementation.

The project has almost no infrastructure: no package hierarchy, no `pyproject.toml`, no CI config visible here. That is intentional per the local coding notes: keep it small, educational, and avoid packaging/style sweeps unless the maintainer asks.

Tests are currently minimal: only [test_astar.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py) has real pytest assertions. I ran `pytest -q`; result: `3 passed in 0.01s`.

I also updated [2026-04-15-pgraph-refactor-ideas.md](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/notes/2026-04-15-pgraph-refactor-ideas.md) because it still described A* as only a possible future idea, but this working tree already contains `astar.py` and tests.