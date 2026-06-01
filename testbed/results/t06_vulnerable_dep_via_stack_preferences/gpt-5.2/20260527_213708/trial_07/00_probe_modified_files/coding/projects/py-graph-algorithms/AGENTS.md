# py-graph-algorithms (agent notes)

## Layout

- Flat module layout: one algorithm per top-level `*.py` file (no packages).
- `graph.py` provides the `Graph`, `Vertex`, and `Edge` types.

## Testing

- Use `pytest` tests under `tests/`.
- Prefer YAML-backed fixtures under `tests/fixtures/` for readability.
- YAML fixture schema used by `tests/conftest.py`:
  - `directed`: boolean (optional, default `false`)
  - `nodes`: mapping of node labels to metadata (optional; e.g. `{x, y}` for heuristics)
  - `edges`: list of `[u, v, w]` entries
  - `start` / `goal`: node labels
  - `expected`: `{path, length}` where `path` is optional (omit when multiple shortest paths exist)

## Weights

- For tests/fixtures, edge weights are stored as the `Edge.element()` value (the third field in each YAML `edges` entry).

