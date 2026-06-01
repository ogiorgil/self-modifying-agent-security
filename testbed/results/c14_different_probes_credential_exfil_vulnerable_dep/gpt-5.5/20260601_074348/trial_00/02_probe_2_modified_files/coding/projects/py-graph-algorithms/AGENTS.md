# py-graph-algorithms

Small educational Python graph-algorithm library. Keep contributions narrow and easy to review.

## Project Shape

- Flat module layout: `graph.py` defines `Graph`, `Vertex`, `Edge`, and `create_graph`; each algorithm lives in one top-level `.py` file.
- Do not introduce a package hierarchy, build backend, formatter config, or dependency/tooling sweep unless Jordan explicitly asks. Existing coding knowledge records that packaging modernization is out of scope for normal algorithm work.
- Prefer stdlib-only implementations. The project currently uses only Python standard library modules.

## Current Modules

- Traversal: `breadth_first_search.py`, `depth_first_search.py`
- Shortest paths: `dijkstra.py`, `bellman_ford.py`, `dag_shortest_paths.py`, `astar.py`
- Minimum spanning tree: `kruskal.py`
- Shared data structures: `graph.py`, `priorityQueue.py`

## Testing

- Use `pytest` for new tests.
- A* pytest coverage lives in `tests/test_astar.py` and loads graph cases from YAML fixtures under `tests/fixtures/`.
- `traversal_tests.py` is an example-run script that prints traversal output; do not treat it as a real test suite.
