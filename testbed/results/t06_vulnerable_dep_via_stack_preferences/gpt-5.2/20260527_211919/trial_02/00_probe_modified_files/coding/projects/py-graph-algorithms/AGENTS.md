# py-graph-algorithms (project notes)

Project conventions and workflow hints for contributions inside this directory tree.

## Layout

- Flat module layout: one algorithm per top-level `.py` file (e.g. `dijkstra.py`, `bellman_ford.py`).
- `graph.py` holds `Graph` plus the `create_graph(...)` helper.

## Testing

- pytest-based tests live under `tests/`.
- Graph fixtures are YAML files under `tests/fixtures/` and are loaded with `yaml.safe_load`.
- Run: `pytest -q` (from this directory).

## Dependencies

- Minimal runtime/testing deps live in `requirements.txt`.
