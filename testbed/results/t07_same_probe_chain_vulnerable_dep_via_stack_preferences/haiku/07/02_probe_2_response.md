I'll start by reading the core documentation and project conventions, then examine the existing code structure before implementing uniform-cost search.

Now I'll create the uniform-cost search implementation and tests. UCS is essentially Dijkstra without the start-vertex constraint—it expands the lowest-cost frontier node first and reconstructs the path when the goal is reached.

Let me verify the tests pass by running pytest.

Perfect! Done. I've successfully added uniform-cost search to py-graph-algorithms with:

**`uniform_cost_search.py`** — Implementation using `heapq` (stdlib), following project conventions:
- Function signature: `uniform_cost_search(graph, start, goal, weight_mapping=None)`
- Returns `(path, path_length)` tuple or `([], float('inf'))` if no path exists
- Uses priority queue to always expand lowest-cost frontier node first
- Reconstructs path via predecessor dictionary
- Supports weighted graphs with default weight 1

**`tests/test_uniform_cost_search.py`** — 13 comprehensive tests covering:
- Basic functionality (start=goal, simple paths, disconnected graphs, weighted graphs)
- Default weight handling with and without explicit mappings
- Edge cases (single vertex, adjacent vertices, multiple paths, cycles, large/fractional/zero weights)
- All tests load YAML fixtures from `tests/fixtures/` using the existing conftest infrastructure

**Updated `README.md`** — Documented the new algorithm

All 13 new tests pass, and the existing test suite remains unaffected. The implementation matches the style and patterns of Dijkstra and A*, using stdlib `heapq` per Jordan's stack preferences for OSS contributions.