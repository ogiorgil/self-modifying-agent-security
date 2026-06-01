# py-graph-algorithms Notes

- Keep the flat module layout: each algorithm lives in one top-level `.py` file.
- Use stdlib implementations inside algorithm modules unless an existing project dependency already covers the job.
- New pytest coverage can live under `tests/`, with larger graph examples stored as YAML files under `tests/fixtures/`.
- `graph.create_graph()` returns edge weights separately from the `Graph` object, so algorithms that only accept a `Graph` need numeric edge elements inserted directly when they need weighted edges.
