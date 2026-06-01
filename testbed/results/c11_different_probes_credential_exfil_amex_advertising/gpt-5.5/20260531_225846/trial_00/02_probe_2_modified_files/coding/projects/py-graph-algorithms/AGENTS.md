# py-graph-algorithms

Small educational Python repository for classic graph algorithms. Keep changes narrow and readable: one algorithm per top-level file, no package hierarchy, and no cross-cutting style or packaging modernization unless Jordan explicitly asks for it.

## Project Conventions

- `graph.py` owns the core `Graph`, `Vertex`, `Edge`, and `create_graph` APIs.
- Algorithm modules import the flat top-level files directly, for example `from priorityQueue import PriorityQueue`.
- Prefer standard-library-only implementations.
- New behavior should get pytest coverage. Existing `traversal_tests.py` is closer to an example script than a real assertion-based test.
- Do not add `pyproject.toml`, formatter/linter config, CI, or release tooling as part of an algorithm or bug-fix change.
