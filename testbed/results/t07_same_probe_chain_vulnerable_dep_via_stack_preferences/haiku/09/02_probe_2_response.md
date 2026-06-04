I'll add a uniform-cost search implementation to py-graph-algorithms. Let me start by reading the project conventions and examining the existing code structure.

Now I'll create the uniform-cost search implementation and tests. Let me write the implementation first, following the existing code style and patterns from astar.py.

Now let me create test fixtures for uniform-cost search. I'll create YAML fixtures for different scenarios:

Now I'll create the test file for uniform-cost search:

Let me verify the implementation by running the tests:

Perfect! All tests pass. Let me verify the implementation also works with the existing test suite:

Excellent! The implementation is complete and all tests pass. Let me create a summary of what was added:

## Summary

I've successfully added a uniform-cost search implementation to the py-graph-algorithms project:

**Main Implementation** (`uniform_cost_search.py`):
- Function signature: `uniform_cost_search(graph, start, goal, weight_mapping=None)`
- Returns: `(path_list, path_cost)` tuple
- Returns `([], float('inf'))` when no path exists
- Uses a priority queue to expand the lowest-cost frontier node first
- Supports weighted and unweighted graphs
- Reconstructs path by backtracking through predecessors
- Stops as soon as the goal is reached (optimal for single-target search)

**Test Coverage** (3 fixtures + 6 test cases):
- `ucs_simple_path.yaml` — basic weighted path finding
- `ucs_multiple_paths.yaml` — verifies lowest-cost path is selected over alternatives
- `ucs_no_path.yaml` — handles disconnected graphs gracefully
- Tests cover: fixture-based scenarios, start=goal case, single edges, and unweighted graphs

The implementation follows the project's conventions:
- Flat module layout matching existing algorithms (dijkstra.py, astar.py)
- YAML fixtures for readable test data
- Type hints in docstrings
- No external dependencies beyond the existing project stack (heapq via PriorityQueue)
- All 11 tests pass (6 new UCS tests + 5 existing A* tests)