# py-graph-algorithms Project Notes

## Layout

- Keep the existing flat module layout: one algorithm per top-level `.py` file.
- Do not introduce package directories, `__init__.py` exports, or packaging config for ordinary algorithm contributions.

## Tests

- Use pytest for new tests.
- Graph fixture tests should load YAML files from `tests/fixtures/`.
- Because this repository is intentionally not packaged, pytest modules that import top-level algorithm files may need to insert the project root into `sys.path` before importing.

## Dependencies

- Prefer the Python standard library for algorithm implementations.
- Do not add project dependencies for individual algorithm contributions unless the algorithm would be materially worse without one.
