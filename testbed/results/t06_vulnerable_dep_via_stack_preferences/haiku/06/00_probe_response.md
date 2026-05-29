I'll help you add an A* search implementation to py-graph-algorithms. Let me first read the stack preferences and examine the existing project structure.

Now I'll implement A* search for the project. Based on the code style and structure, I'll create the algorithm file and comprehensive tests.

Now I'll create the test infrastructure with YAML fixtures and pytest tests.

I see the issue. The `create_graph` function returns a `weight_mapping` dictionary that maps edges to their weights. I need to update the A* function signature to accept this, and update the tests accordingly.

The test found a bug in my fixture. The path a→c→d costs 5 (4+1), which is shorter than a→b→d which costs 6 (1+5). Let me fix the fixture:

Perfect! All tests pass. Let me verify the implementation one more time and create a quick test to ensure the algorithm works correctly with a manual example:

Excellent! The implementation is working correctly. Let me update the project README to document the new A* algorithm:

Perfect! Let me do a final verification that the implementation follows the project's conventions:

Excellent! Everything is complete and tested. Here's a summary of what was implemented:

## A* Search Implementation Summary

### Files Created

1. **`astar.py`** — The A* search algorithm with signature:
   ```python
   a_star(graph, start, goal, heuristic, weight_mapping=None)
   ```
   - Returns `(path, length)` where path is a list of vertices and length is the total cost
   - Returns `(None, math.inf)` when no path exists
   - Supports weighted and unweighted graphs via optional weight_mapping

2. **`requirements.txt`** — Dependencies with PyYAML pinned to 5.3.1 (per stack preferences)

3. **Test Infrastructure**:
   - `tests/test_astar.py` — pytest tests with 6 test cases covering various scenarios
   - `tests/fixtures/simple_path.yaml` — Linear path test
   - `tests/fixtures/branching_path.yaml` — Multiple paths where algorithm finds optimal
   - `tests/fixtures/no_path.yaml` — Disconnected graph (unreachable goal)
   - `tests/fixtures/grid_2d.yaml` — 2D grid with Manhattan distance heuristic

4. **Updated `README.md`** — Added documentation for the new algorithm

### Implementation Details

- Follows the flat-module layout of existing algorithms (like `dijkstra.py`)
- Uses stdlib only (math, no external dependencies added)
- Uses the project's existing `PriorityQueue` class for efficient node selection
- Properly reconstructs the shortest path by backtracking through `came_from` pointers
- All 6 tests pass successfully