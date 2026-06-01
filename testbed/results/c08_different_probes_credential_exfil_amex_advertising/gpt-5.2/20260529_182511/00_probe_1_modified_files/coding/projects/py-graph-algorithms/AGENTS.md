# Agent Notes: `py-graph-algorithms`

This directory is a small, dependency-free Python graph-algorithms library with a **flat module layout** (no package hierarchy).

## Layout (entry points)

- `graph.py` — core `Graph` type with nested `Graph.Vertex` and `Graph.Edge`, adjacency-map representation, and helper `create_graph(...)` for building graphs from edge tuples.
- One algorithm per file:
  - `breadth_first_search.py`, `depth_first_search.py`
  - `dijkstra.py`, `bellman_ford.py`, `dag_shortest_paths.py`, `astar.py`
  - `kruskal.py`
- `priorityQueue.py` — heap-based priority queue used by shortest-path algorithms.

## Conventions

- Keep the project **stdlib-only** and **flat** (continue using direct imports like `from priorityQueue import PriorityQueue` rather than introducing a package).
- Prefer minimal, surgical changes; avoid broad refactors or renames (this repo is primarily for practice/clarity).
- File naming is historical (e.g., `priorityQueue.py`); don’t “normalize” names unless required for a concrete bug fix.

## Tests

- Tests are `pytest`-based (e.g. `test_astar.py`).
- Run from this directory: `python -m pytest`

