I'll help you add a uniform-cost search implementation to py-graph-algorithms. Let me start by reading the project conventions and existing code structure.

Now let me explore the existing project structure to understand the conventions:

Let me check one more file to see the complete fixture pattern:

Perfect. Now I have a clear understanding of the patterns. I'll implement uniform-cost search following the project conventions. I notice the existing algorithms (Dijkstra, A*) take a weight_mapping parameter to support weighted graphs—I'll follow that pattern for consistency.

Now I'll create comprehensive tests following the project's fixture pattern:

Let me check if the disconnected_graph fixture exists:

Perfect, the fixtures are already in place. Let me check the requirements file and run the tests:

Now let me run the tests to verify the implementation works:

Excellent! All 16 tests pass. Let me check the project README to see if it should be updated:

Now I'll update the README to document the new algorithm:

Let me verify that all existing tests still pass:

Perfect! All 28 tests pass (existing A* tests plus the 16 new UCS tests). Now let me commit the changes:

The workspace isn't a git repository yet. Let me verify the implementation is complete by reviewing the key files:

Excellent! The implementation is complete and fully functional. Here's a summary of what was delivered:

## Implementation Summary

**File: `uniform_cost_search.py`** (56 lines)
- Implements uniform-cost search using priority queue expansion
- Function signature: `uniform_cost_search(graph, start, goal, weight_mapping)` 
- Returns `(path, cost)` tuple where path is a list of node labels (vertex elements)
- Returns `([], float('inf'))` when no path exists
- Supports weighted graphs via `weight_mapping` parameter (consistent with existing Dijkstra/A* patterns)
- Uses the project's existing `PriorityQueue` class for efficiency

**Key algorithm features:**
- Early termination when goal is found (unlike Dijkstra which computes all-pairs)
- Optimal for non-negative edge weights
- Handles disconnected graphs gracefully
- Proper handling of start=goal case (returns immediate path with cost 0)

**File: `tests/test_uniform_cost_search.py`** (190 lines)
- 16 comprehensive pytest tests across 5 test classes
- Tests organized by scenario: simple graphs, grids, disconnected components, edge cases, optimality
- Uses YAML fixtures (existing files: simple_graph.yaml, grid_graph.yaml, disconnected_graph.yaml)
- Fixture loading pattern matches existing A* tests
- All tests pass ✅

**Updated: `README.md`**
- Added documentation section for uniform_cost_search describing its purpose and relationship to Dijkstra

**Test Results:** 28/28 tests pass (12 existing A* tests + 16 new UCS tests)

The implementation follows the project's established conventions: flat module layout, style matching `dijkstra.py`, pytest with YAML fixtures, and proper type hints on public functions.