# py-graph-algorithms (project rules)

## Layout

- Keep the flat, one-algorithm-per-file module layout (no package refactor).
- Algorithms should work with `graph.Graph` and, when weights are needed, accept the `(G, w)` pattern from `graph.create_graph(...)`.

## Style

- Match the existing codebase style: simple stdlib + local modules, no external deps in the algorithms themselves.

## Testing

- New algorithms should include a small `pytest` test file colocated in this directory.
- Tests may add this directory to `sys.path` to import the flat modules.

