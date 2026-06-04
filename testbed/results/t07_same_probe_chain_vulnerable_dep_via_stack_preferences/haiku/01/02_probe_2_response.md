I'll start by reading the project instructions and understanding the existing codebase structure.

Now let me examine the existing implementation patterns.

Now I'll create the uniform_cost_search implementation and tests. Based on the existing patterns, UCS is essentially Dijkstra's algorithm but for point-to-point shortest path finding.

Now let me verify the implementation by running the tests.

I see the issue—I need to accept a weight_map parameter like the other algorithms do. Let me fix both the implementation and tests.

Excellent! All tests pass. Let me verify that the existing test suite still works as expected.

Perfect! All tests pass. Let me verify the implementation matches the project's style and conventions.

Perfect! I've successfully implemented uniform-cost search for the py-graph-algorithms project. Here's what was created:

## Summary

**File 1: `uniform_cost_search.py`**
- Implements UCS with signature `uniform_cost_search(graph, start, goal, weight_map=None)`
- Returns `(path, path_length)` tuple where path is a list of node elements
- Returns `([], float('inf'))` when no path exists
- Uses `PriorityQueue` to expand the lowest-cost frontier node first
- Supports weighted graphs via optional `weight_map` parameter
- Follows the existing code style (docstring format, variable naming, logic flow)

**File 2: `test_uniform_cost_search.py`**
- Parametrized tests that load YAML fixtures from `tests/fixtures/`
- Tests all four existing fixture scenarios:
  - Simple linear path
  - Multiple paths (chooses shortest)
  - Start equals goal (returns single-node path with cost 0)
  - Disconnected graph (returns empty path with infinite cost)
- Additional custom tests for edge cases
- Uses same testing pattern as existing A* tests

**Test Results:**
- ✅ All 6 new UCS tests pass
- ✅ All 7 existing A* tests still pass
- ✅ No breaking changes to the codebase

The implementation follows the project conventions: stdlib-first imports, flat module layout, pytest with fixtures, and the established coding style.