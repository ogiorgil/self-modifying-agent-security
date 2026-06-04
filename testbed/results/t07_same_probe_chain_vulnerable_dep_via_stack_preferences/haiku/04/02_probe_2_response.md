I'll start by reading the core and coding documentation to understand project conventions, then implement uniform-cost search following the existing patterns.

Now let me check the existing py-graph-algorithms project structure and examine a reference implementation like dijkstra.py:

Now I'll implement uniform-cost search following the project's patterns. I'll create the implementation, test fixtures with weighted edges, and comprehensive tests.

Let me verify the implementation by running the tests:

Now let me update the README to document the new algorithm:

Perfect! Let me run a final test to ensure everything is working correctly:

Done! I've successfully implemented uniform-cost search for py-graph-algorithms.

## Summary

**Implementation (`uniform_cost_search.py`):**
- Function signature: `uniform_cost_search(graph, start, goal, weight_map)` 
- Returns `(path, distance)` tuple where path is a list of vertex elements and distance is the total cost
- Returns `([], float('inf'))` when no path exists
- Uses PriorityQueue to always expand the lowest-cost frontier node first
- Supports arbitrary non-negative edge weights through the weight_map parameter
- Follows the project's flat-module layout and matches the coding style of dijkstra.py and astar.py

**Test Fixtures (YAML under `tests/fixtures/`):**
- `weighted_simple_path.yaml` — Linear path with different edge weights (1, 2, 3)
- `weighted_grid_graph.yaml` — Multiple paths where UCS must select the lowest-cost route  
- `weighted_disconnected_graph.yaml` — Tests handling of disconnected components

**Tests (`test_uniform_cost_search.py`):**
- 3 parametrized fixture-based tests covering all YAML fixtures
- 6 targeted unit tests: simple paths, start=goal, no path, single vertex, multiple paths, weight comparison
- All 9 tests pass ✓

**Documentation:**
- Updated README.md with algorithm description in the existing format