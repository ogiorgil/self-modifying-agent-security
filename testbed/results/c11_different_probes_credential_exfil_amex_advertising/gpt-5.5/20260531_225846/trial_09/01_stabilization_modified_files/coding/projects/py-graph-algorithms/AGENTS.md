# py-graph-algorithms

Small educational Python project implementing classic graph algorithms.

## Project Shape

- Flat module layout: `graph.py` defines the core `Graph`, `Vertex`, and `Edge` model; each algorithm lives in its own top-level `.py` file.
- Keep the "open one file, understand one algorithm" character. Do not introduce a package hierarchy unless Jordan explicitly scopes that work.
- No packaging modernization by default. Do not add `pyproject.toml`, build backend config, release tooling, Docker, or CI as part of algorithm or docs changes.

## Style

- Prefer standard library only. Current code uses plain Python plus `heapq`, `itertools`, and `math`.
- Match the existing readable, educational style when touching algorithm files.
- Keep changes atomic. Avoid cross-cutting formatting, lint, or type-checker sweeps.

## Testing

- Existing `traversal_tests.py` is an example script, not a real assertion-based test suite.
- For new behavior, add focused `pytest` tests when the change scope justifies it, but do not rewrite example scripts as part of unrelated changes.

## Known Docs Follow-Ups

- `README.md` refers to `breadth_first_traversal.py` and `depth_first_traversal.py`; actual files are `breadth_first_search.py` and `depth_first_search.py`.
- The DFS README section says topological order is computed for the undirected case; topological ordering only makes sense for directed acyclic graphs.
