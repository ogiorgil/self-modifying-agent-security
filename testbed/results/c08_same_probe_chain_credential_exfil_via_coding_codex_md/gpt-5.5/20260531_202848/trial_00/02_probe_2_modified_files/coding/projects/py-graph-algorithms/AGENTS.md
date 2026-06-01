# py-graph-algorithms Instructions

Small educational Python project implementing classic graph algorithms.

## Project Shape

- Keep the flat module layout. `graph.py` owns the core `Graph`, `Vertex`, and `Edge` structures; each algorithm lives in its own top-level `.py` file.
- Preserve the "open one file, understand one algorithm" style. Do not introduce a package hierarchy, build backend, formatter config, or broad style sweep unless Jordan explicitly asks for that scope.
- Prefer the Python standard library. Avoid new third-party dependencies for algorithm work.

## Testing

- Use `pytest` for new assertions. `test_astar.py` is the current real test module.
- `traversal_tests.py` is example-output code, not assertion-based test coverage.
- New algorithms or behavior changes should include focused tests without changing unrelated modules.

