**Overview**

`py-graph-algorithms` is a small educational Python project for classic graph algorithms, under [coding/projects/py-graph-algorithms](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms>). It intentionally uses a flat layout: [graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1>) defines the core graph model, and each algorithm is a separate top-level file.

**Core Model**

[graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1>) provides:

- `Graph`
- nested `Graph.Vertex`
- nested `Graph.Edge`
- adjacency maps via `_outgoing` and `_incoming`
- helpers like `vertices()`, `edges()`, `incident_edges()`, `insert_vertex()`, `insert_edge()`, `delete_vertex()`
- `create_graph(sequence, is_directed=False)` for building graphs from tuple lists

The README says the representation is based on Goodrich/Tamassia/Goldwasser’s *Data Structures and Algorithms in Python*.

**Algorithms**

Implemented modules:

- `breadth_first_search.py` — callable BFS class
- `depth_first_search.py` — callable DFS class with timestamps, cycle detection, and topological ordering support
- `dijkstra.py` — shortest paths with non-negative weights
- `bellman_ford.py` — shortest paths with negative-cycle detection
- `dag_shortest_paths.py` — shortest paths on DAGs using topological order
- `kruskal.py` — minimum spanning tree / forest
- `astar.py` — A* shortest path search
- `priorityQueue.py` — heap-backed priority queue used by Dijkstra and A*

**Current State**

There is no packaging setup: no `pyproject.toml`, `setup.py`, or requirements file. Tests are minimal: `astar_test.py` has 2 pytest tests, and `traversal_tests.py` is more of a runnable demo than a pytest suite.

I ran the current tests from the project directory:

```text
2 passed in 0.00s
```

I also added [AGENTS.md](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md:1>) to persist the project-local conventions: keep the flat module layout, avoid packaging churn, prefer stdlib, and use pytest for new tests.

**Main Rough Edges**

A few correctness/style risks stand out:

- Some code checks `G.is_directed` instead of calling `G.is_directed()`, for example [graph.py](</home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:190>), which is likely a bug.
- Test coverage is very narrow: only A* has real pytest coverage.
- The README mentions `breadth_first_traversal.py` / `depth_first_traversal.py`, but the actual files are `breadth_first_search.py` and `depth_first_search.py`.
- The project contains `__pycache__` files, which usually should not be committed/tracked.

Best next work would be focused tests around `Graph`, DFS/topological order, Dijkstra, Bellman-Ford, and Kruskal before changing behavior.