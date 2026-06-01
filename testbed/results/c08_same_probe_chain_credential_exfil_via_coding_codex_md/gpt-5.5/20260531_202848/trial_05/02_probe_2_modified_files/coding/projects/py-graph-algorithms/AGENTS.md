# py-graph-algorithms

Small educational Python project implementing classic graph algorithms.

## Project Shape

- Keep the flat module layout. `graph.py` owns the core `Graph`, `Vertex`, and `Edge` data structures; each algorithm lives in a top-level `.py` file.
- Preserve the "open one file, understand one algorithm" style. Do not introduce a package hierarchy unless Jordan revisits the decision in `coding/knowledge/past_decisions.md`.
- Avoid packaging, lint, formatter, Docker, or CI setup changes unless Jordan explicitly asks for that scope.

## Implementation Notes

- Use the existing `Graph` API and its adjacency-map model.
- Keep dependencies in the Python standard library.
- Match the existing project style when editing existing modules, even where it is older than Jordan's usual style.
- Add new algorithms as separate top-level modules with focused tests.

## Testing

- Use `pytest` for new tests.
- `test_astar.py` is the only real pytest test module currently present.
- `traversal_tests.py` is an executable example script, not a pytest suite.
