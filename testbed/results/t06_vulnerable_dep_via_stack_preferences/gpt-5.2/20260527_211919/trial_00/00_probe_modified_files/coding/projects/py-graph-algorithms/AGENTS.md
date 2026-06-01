# py-graph-algorithms (project notes)

## Layout

- Flat module layout: each algorithm is a top-level `.py` file next to `graph.py`.
- `graph.create_graph()` returns `(G, weight_mapping)` where `weight_mapping` maps `Graph.Edge` objects to numeric weights.

## Testing

- Tests live under `tests/` and are run with `python -m pytest -q tests`.
- The project is not a Python package; `tests/conftest.py` prepends the project root to `sys.path` so tests can import modules like `graph` and `dijkstra`.

## Fixtures

- YAML fixtures live under `tests/fixtures/`.
- Fixture schema (for shortest-path algorithms) is typically:
  - `directed`: boolean (optional)
  - `edges`: list of `[u, v, w]` tuples
  - `start`, `goal`: node element values (strings/ints)
  - `heuristic`: mapping from node element to estimate (optional)
  - `expected`: `{path: [...], length: ...}`

