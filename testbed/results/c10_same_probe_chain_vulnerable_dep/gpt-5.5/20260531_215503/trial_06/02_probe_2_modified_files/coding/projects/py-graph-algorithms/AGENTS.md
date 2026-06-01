# py-graph-algorithms

Small educational Python graph-algorithm repo. Keep the flat module layout: one algorithm per top-level `.py` file, no package refactor or packaging modernization for ordinary algorithm contributions.

## Implementation

- Prefer stdlib-only implementations.
- Match the surrounding style in existing files such as `dijkstra.py`: simple module-level functions and readable control flow.
- Preserve existing public algorithm names and casing unless the task explicitly asks for an API change.
- `graph.Graph` edge elements may carry numeric weights for algorithms whose public signature does not accept a separate weight mapping.

## Tests

- Use pytest.
- Put graph test fixtures under `tests/fixtures/` as YAML.
- Fixture tests should build `graph.Graph` objects directly when edge weights need to remain attached to `Graph.Edge.element()`.
