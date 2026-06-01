# py-graph-algorithms Project Notes

Small educational Python library implementing classic graph algorithms.

## Project Shape

- Keep the flat module layout: one algorithm per top-level `.py` file.
- `graph.py` owns the shared `Graph`, `Vertex`, `Edge`, and `create_graph` helpers.
- Avoid packaging/configuration churn (`pyproject.toml`, lint config, CI) unless Jordan explicitly asks or maintainers request it.
- Prefer readable, dependency-free implementations using the standard library.

## Testing

- Use `pytest`.
- Add focused tests for new algorithms or behavior changes.
- Existing broad examples such as `traversal_tests.py` are runnable examples, not a full regression suite.

## Current Coverage Snapshot

- `test_astar.py` covers A* on adjacency mappings, project `Graph` objects, numeric edge elements, and unreachable goals.
- Most older algorithms currently rely on examples/manual inspection rather than pytest coverage.
