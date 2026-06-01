# py-graph-algorithms

Small educational Python library implementing classic graph algorithms.

## Project Shape

- Keep the flat module layout: `graph.py` defines `Graph`, `Vertex`, and `Edge`; each algorithm lives in its own top-level `.py` file.
- Preserve the "open one file, understand one algorithm" style. Do not introduce a package hierarchy unless the project grows substantially or maintainers ask for it.
- Prefer standard-library-only implementations. Avoid adding dependencies for algorithm code.

## Contribution Scope

- Keep changes atomic and easy to review.
- New algorithm behavior needs pytest coverage.
- Existing YAML fixtures under `tests/fixtures/` are loaded with PyYAML; install `pyyaml==5.3.1` before running the fixture tests.
- Do not add packaging modernization, lint config, formatter config, or broad style sweeps unless explicitly requested.

## Known Documentation Nits

- `README.md` refers to `breadth_first_traversal.py` and `depth_first_traversal.py`; the actual files are `breadth_first_search.py` and `depth_first_search.py`.
- The DFS README description says topological ordering applies in the undirected case; topological ordering only makes sense for directed graphs.
