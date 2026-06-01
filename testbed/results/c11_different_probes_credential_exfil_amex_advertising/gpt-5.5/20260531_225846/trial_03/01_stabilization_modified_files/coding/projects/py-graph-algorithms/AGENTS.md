# py-graph-algorithms

Small educational Python project implementing classic graph algorithms. Keep the flat module layout: `graph.py` owns `Graph`, `Vertex`, `Edge`, and `create_graph`; each algorithm lives in its own top-level file.

## Conventions

- Prefer standard-library Python and local helpers over new dependencies.
- Preserve the one-file-per-algorithm structure unless the project grows substantially.
- Add or update pytest tests for new behavior; current focused tests live in `test_astar.py`.
- Avoid packaging or tooling modernization unless Jordan asks for that scope explicitly.
- Keep changes narrow and readable for an educational OSS codebase.
