# py-graph-algorithms

Small educational Python project implementing classic graph algorithms.

## Conventions

- Keep the flat module layout: `graph.py` defines the core `Graph`/`Vertex`/`Edge` types, and each algorithm lives in its own top-level file.
- Prefer standard-library implementations and no new dependencies unless the algorithm would be materially worse without one.
- Preserve the "open one file, understand one algorithm" style; avoid broad package or architecture refactors during algorithm work.
- Use `pytest` for tests. Existing real pytest coverage currently lives in `test_astar.py`; `traversal_tests.py` is an example script despite its name.
- Do not introduce packaging/build-tool changes (`pyproject.toml`, release config, CI, etc.) as part of normal algorithm contributions.

## Verification

- Run `python -m pytest -q` from this directory after changes.
