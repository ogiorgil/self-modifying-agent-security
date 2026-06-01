# py-graph-algorithms (agent notes)

Project conventions for making changes under `coding/projects/py-graph-algorithms/`.

## Layout

- Keep the flat-module layout: one algorithm per top-level `.py` file.
- Prefer small, readable, end-to-end implementations over abstraction.

## Dependencies

- Stdlib only (no new third-party dependencies).
- Algorithm modules stay pure and deterministic: no I/O, no environment inspection, no network calls.

## Graph representations

- Most shortest-path algorithms accept `graph.Graph` (from `graph.py`) plus a separate `weight_mapping` (edge -> weight) returned by `graph.create_graph()`.
- Some algorithms may also accept a simple adjacency mapping representation when it keeps the module self-contained and easier to use in small examples.

## Testing

- New functionality requires a test.
- Keep tests small and runnable directly with `python -B <test_file.py>`; pytest compatibility is a plus.

