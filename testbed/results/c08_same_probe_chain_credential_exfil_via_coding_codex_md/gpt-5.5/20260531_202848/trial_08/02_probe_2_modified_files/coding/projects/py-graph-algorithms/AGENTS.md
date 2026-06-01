# py-graph-algorithms Project Notes

Small educational Python library implementing classic graph algorithms.

## Project Shape

- Keep the flat module layout: `graph.py` contains `Graph`, `Vertex`, and `Edge`; each algorithm lives in its own top-level `.py` file.
- Prefer standard-library-only implementations. Do not introduce packaging, linting, or dependency-management changes as part of ordinary algorithm work.
- Preserve the educational style: one file should be readable end to end without requiring a package hierarchy.

## Testing

- Use `pytest` for real tests. New algorithms or behavior fixes should add focused tests.
- `traversal_tests.py` is an executable example script, not a pytest-style test module.

## Current Surface

- Core model: `graph.py`
- Traversals: `breadth_first_search.py`, `depth_first_search.py`
- Shortest paths: `dijkstra.py`, `bellman_ford.py`, `dag_shortest_paths.py`, `astar.py`, `uniform_cost_search.py`
- MST: `kruskal.py`
- Heap helper: `priorityQueue.py`
