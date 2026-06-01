# py-graph-algorithms Project Notes

Small educational Python library for classic graph algorithms. Keep the flat
module layout: `graph.py` owns `Graph`/`Vertex`/`Edge`, and each algorithm lives
in a top-level module.

## Conventions

- Prefer stdlib-only implementations unless a dependency already exists for a
  focused test fixture need.
- Do not introduce packaging, lint, or CI configuration as part of an algorithm
  change.
- New algorithm behavior should have pytest coverage under `tests/`.
- YAML fixtures live under `tests/fixtures/`; install `pyyaml==5.3.1` before
  running fixture-based tests.
- Keep examples simple and readable. The project values "open one file,
  understand one algorithm" over framework or package structure.

## Current Shape

- `astar.py` supports both adjacency mappings and `graph.Graph` objects.
- `tests/test_astar.py` is the only pytest test module currently present.
- `traversal_tests.py` is an example script, not a pytest module.
