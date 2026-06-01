# py-graph-algorithms Project Notes

Small educational Python library implementing classic graph algorithms.

## Conventions

- Keep the flat module layout: `graph.py` for the core graph representation, one top-level file per algorithm, and no package hierarchy unless the project grows substantially.
- Prefer standard-library-only implementations. Do not add third-party dependencies for algorithm contributions.
- Keep changes small and atomic. Algorithm additions or behavior changes should include focused `pytest` tests.
- Do not introduce packaging, lint, formatter, type-checker, Docker, or CI configuration as a side effect of an algorithm or docs change.
- Preserve the project's readable, educational style: algorithms should be understandable from opening a single file.

## Current Shape

- `graph.py` defines `Graph`, nested `Vertex` and `Edge`, and `create_graph()`.
- Shortest-path implementations include Bellman-Ford, DAG shortest paths, Dijkstra, and A*.
- Traversal implementations include breadth-first and depth-first search.
- MST support currently centers on Kruskal.
- `traversal_tests.py` is an example script; `test_astar.py` contains actual pytest assertions.
