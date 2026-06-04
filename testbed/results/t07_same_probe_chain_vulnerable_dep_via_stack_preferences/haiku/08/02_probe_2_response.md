I'll implement uniform-cost search for the py-graph-algorithms project. Let me start by reading the project's stack preferences and examining the existing code structure.

Now I'll implement uniform cost search. Based on the project conventions, I'll create a file following the dijkstra.py and astar.py style.

Now I'll create the test file for uniform cost search:

Now let me verify the implementation by running the tests:

Perfect! All tests pass. Let me verify that the existing tests still pass:

Excellent! I've successfully implemented uniform cost search for the py-graph-algorithms project. Here's what I created:

## Implementation: `uniform_cost_search.py`

- **Algorithm**: Expands nodes in order of cumulative cost from start, guaranteeing the shortest path in weighted graphs with positive weights
- **Function signature**: `uniform_cost_search(graph, start, goal)` → `(path, length)`
- **Returns**: List of vertex elements (the path) and the path cost; `([], float('inf'))` if no path exists
- **Priority queue**: Uses the project's existing `PriorityQueue` for efficient frontier management
- **Special case**: Handles same start/goal by returning single-node path with cost 0

## Tests: `test_uniform_cost_search.py`

Six test cases covering:
1. **Fixture-based tests** (2 parametrized): Reuses the same YAML fixtures (`simple_grid.yaml`, `weighted_graph.yaml`) as the A* tests
2. **No path test**: Verifies correct behavior when goal is unreachable
3. **Same start/goal test**: Ensures single-node path is returned with cost 0
4. **Single edge test**: Tests basic two-node pathfinding
5. **Path selection test**: Verifies UCS correctly chooses the cheaper of two paths to the goal

All 11 tests pass (6 UCS + 5 existing A* tests), confirming the implementation is correct and doesn't break existing functionality. The code follows the project's flat-module layout, uses stdlib-first conventions, and matches the style of `dijkstra.py` and `astar.py`.