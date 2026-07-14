`py-graph` is `py-graph-algorithms`: a small educational Python repo for classic graph algorithms, not a packaged library.

Core shape:
- [graph.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py) defines the shared `Graph`, nested `Vertex`, and nested `Edge` classes using adjacency maps.
- Each algorithm is a flat top-level module: BFS, DFS, Dijkstra, Bellman-Ford, DAG shortest paths, Kruskal, and A*.
- [priorityQueue.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py) wraps `heapq` with update/remove support for Dijkstra and A*.
- [README.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/README.md) documents the intended textbook-style usage.

Current test coverage is narrow: only [tests/test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py) exists, using YAML fixtures. I ran `python -m pytest -q`; result: `2 passed`.

Important project conventions:
- Keep the flat layout: one algorithm per top-level `.py` file.
- Prefer stdlib and readable implementations over new dependencies.
- New functionality should use pytest.
- Larger graph fixtures belong under `tests/fixtures/`.

Rough edges:
- No `pyproject.toml`, `setup.py`, or requirements file.
- Naming/style is inconsistent with modern Python conventions: e.g. `Bellman_Ford`, `Dijkstra`, `Kruskal`, `priorityQueue.py`.
- Several modules include demo code instead of formal tests.
- Some implementation details look bug-prone, such as `if self.is_directed:` instead of `if self.is_directed()` in a few places.

Also: the workspace root is not currently a git repository, so `git status` failed with “not a git repository.”