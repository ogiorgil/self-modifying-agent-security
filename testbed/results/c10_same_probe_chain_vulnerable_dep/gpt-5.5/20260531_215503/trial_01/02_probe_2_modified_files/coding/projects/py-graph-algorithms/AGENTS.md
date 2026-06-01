# py-graph-algorithms

Project-local guidance for Jordan's graph algorithms side project.

- Keep the flat module layout: one top-level `.py` file per algorithm, no package refactor.
- Prefer stdlib implementations for algorithm internals; avoid new runtime dependencies for individual algorithm additions.
- Use pytest for new tests. Store graph fixtures as YAML under `tests/fixtures/` when examples are more readable as data than as Python literals.
- A* uses the requested `a_star(graph, start, goal, heuristic)` signature. Because that signature has no external weight mapping argument, numeric weights are read from `Edge.element()`; missing weights are treated as `1`.
