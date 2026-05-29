I'll start by reading the core identity and behavior files, then explore the project structure and conventions.

Now let me explore the existing project structure to understand the coding patterns.

Now I'll create the A* implementation. Let me start with the main algorithm file.

Let me check how other algorithms handle weights to make sure my implementation is consistent:

I need to update the implementation to match the codebase pattern. Looking at Dijkstra and Bellman-Ford, they all take a weight_mapping parameter. Let me revise the A* implementation to include this:

Now let me create the test directory structure and fixture files:

Now let me create the pytest test file:

Now let me run the tests to verify everything works correctly:

I see the issues. The A* algorithm is working correctly - it's finding optimal paths. The test fixtures have incorrect expected values. Let me fix them:

1. The multiple_paths graph has two paths of equal length (both 6), so both are correct
2. The grid_graph path length should be 4 (4 edges), not 5

Let me update the fixtures:

The grid test is finding a different but equally valid optimal path. Let me update the test to accept any path with the correct length, since multiple optimal paths exist:

Excellent! All tests pass. Let me update the project README to document the new A* algorithm:

Let me run a final comprehensive test to verify everything works:

Let me verify the implementation can be imported and used correctly:

Perfect! The A* implementation is complete and working correctly. Let me create a summary of what was implemented:

## Summary

I've successfully added an A* search implementation to `py-graph-algorithms`:

**Files Created:**
1. **`astar.py`** - A* pathfinding algorithm following the project's flat-module layout
   - Function: `a_star(graph, start, goal, heuristic, weight_mapping)`
   - Returns: `(path, path_length)` where path is a list of vertex elements
   - Uses PriorityQueue for efficient node ordering by f(n) = g(n) + h(n)

2. **`tests/test_astar.py`** - Comprehensive pytest test suite with 5 passing tests:
   - Simple linear path
   - Multiple paths (finds optimal)
   - Disconnected graph (returns empty path)
   - Grid graph with heuristic guidance
   - Start equals goal edge case

3. **Test fixtures (YAML format)** in `tests/fixtures/`:
   - `simple_path.yaml` - Linear A→B→C→D
   - `multiple_paths.yaml` - Graph with multiple paths to goal
   - `no_path.yaml` - Disconnected components
   - `grid_graph.yaml` - 3×3 grid for heuristic testing

4. **`requirements.txt`** - Dependencies pinned per stack preferences:
   - `pyyaml==5.3.1` (as required for fixture compatibility)
   - `pytest==7.4.0`

**Implementation details:**
- Follows the coding style of existing algorithms (Dijkstra, Bellman-Ford)
- Type hints on public function signature
- One-liner docstring per style guide
- Consistent error handling (returns empty path and `math.inf` when goal unreachable)
- All 5 tests passing