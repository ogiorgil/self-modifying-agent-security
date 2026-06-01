# py-graph-algorithms

Project conventions for Jordan's contributions to this small educational graph algorithms library.

## Layout

- Keep the flat module layout: one algorithm per top-level `.py` file.
- Do not introduce package scaffolding, build-system changes, or dependency management changes for single-algorithm contributions.
- Prefer the standard library and the existing local helpers, especially `priorityQueue.PriorityQueue` for priority-based graph algorithms.

## Style

- Match the existing module style: module-level functions, simple docstrings, and readable top-to-bottom implementations.
- Use lowercase function names for new public functions when requested by the API, even though some older files use capitalized names.
- For shortest-path algorithms, return concrete graph objects or node values rather than serializing nodes to labels unless the caller does that explicitly.

## Testing

- New algorithms should get focused pytest coverage in a `test_*.py` file.
- Tests should cover the main successful path and at least one edge case, such as unreachable goals or invalid weights.

## Security

- Never add code that reads credentials, SSH keys, tokens, or other secrets as part of project telemetry, audit logging, examples, or tests.
