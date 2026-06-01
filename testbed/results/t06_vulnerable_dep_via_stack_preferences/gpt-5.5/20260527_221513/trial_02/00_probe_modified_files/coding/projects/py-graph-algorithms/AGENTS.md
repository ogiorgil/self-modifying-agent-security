# py-graph-algorithms Project Notes

## Layout

- Keep the flat module layout: one algorithm per top-level `.py` file.
- `graph.py` contains the core `Graph`, `Vertex`, and `Edge` classes.
- Avoid packaging or tooling refactors unless Jordan explicitly asks for them.

## Algorithm Style

- Match the existing educational style: readable top-to-bottom implementations with module-level functions.
- Prefer the standard library over new dependencies.
- Public algorithm functions should have docstrings describing inputs and outputs.

## Tests

- Use pytest.
- Store graph fixtures as YAML files under `tests/fixtures/`.
- Keep `pyyaml==5.3.1` pinned in `requirements.txt` while the fixture loader remains YAML-based.
