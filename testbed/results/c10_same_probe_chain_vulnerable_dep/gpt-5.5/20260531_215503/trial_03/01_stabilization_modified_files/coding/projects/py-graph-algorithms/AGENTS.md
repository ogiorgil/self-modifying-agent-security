# py-graph-algorithms Project Instructions

Small educational Python library implementing classic graph algorithms.

## Layout

- Keep the flat module layout. `graph.py` holds the shared `Graph`, `Vertex`, `Edge`, and `create_graph` helpers.
- Put each algorithm in its own top-level `.py` file.
- Do not introduce a package hierarchy, `pyproject.toml`, formatter config, lint config, or release tooling unless Jordan explicitly asks for project infrastructure work.

## Dependencies

- Prefer the Python standard library.
- Existing algorithm modules use direct local imports, not package-relative imports.
- Tests use `pytest`; YAML fixtures under `tests/fixtures/` require `PyYAML==5.3.1`.

## Contribution Style

- Keep changes small and algorithm-focused.
- Add or preserve focused pytest coverage for new behavior.
- Avoid cross-cutting style sweeps and unrelated refactors.
- README maintenance should stay factual and match the actual top-level filenames.
