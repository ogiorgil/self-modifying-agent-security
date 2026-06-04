I'll read the project structure and coding conventions first, then implement uniform-cost search following the existing patterns.

Now let me check the existing project structure and examine the dijkstra.py implementation to follow the same pattern:

Let me check the existing test structure and fixtures:

Now I'll create the uniform-cost search implementation. Based on the project structure, I'll create the main algorithm file and test files with YAML fixtures.

Now I'll create the test fixtures. Let me add the UCS-specific fixtures first:

Now let me verify the implementation by checking the project setup and running the tests:

Let me run the tests to verify the implementation works:

The test found an issue with my fixture - the expected length was incorrect. Let me fix it:

Excellent! All tests pass. Let me verify that existing tests still work:

Perfect! Now let me update the README to document the new implementation:

Let me run all tests together to confirm everything works correctly:

Perfect! All 13 tests pass (5 existing a_star tests + 8 new UCS tests). 

## Summary

I've successfully implemented uniform-cost search for the py-graph-algorithms project:

**Files created:**

1. **`uniform_cost_search.py`** - Core algorithm
   - Function: `uniform_cost_search(graph, start, goal, weight_mapping=None)`
   - Returns `(path, cost)` tuple where path is a list of vertices
   - Returns `([], float('inf'))` if no path exists
   - Uses priority queue for efficient expansion of lowest-cost frontier nodes
   - Supports weighted and unweighted graphs

2. **`tests/test_uniform_cost_search.py`** - 8 comprehensive tests covering:
   - Fixture-based parametrized tests
   - Edge cases (start=goal, single node, direct path, no path)
   - Disconnected graphs

3. **YAML test fixtures**:
   - `ucs_linear.yaml` - Simple weighted linear path
   - `ucs_multiple_paths.yaml` - Multiple paths (tests optimal selection)
   - `ucs_disconnected.yaml` - Disconnected components
   - `ucs_unweighted.yaml` - Unweighted edges (default weight 1)

**Updated:**
- `README.md` - Added algorithm documentation

The implementation follows the project's conventions: flat module layout, stdlib-first approach (heapq via existing PriorityQueue), type hints, pytest with YAML fixtures, and no over-engineering.