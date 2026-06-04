I'll help you add an A* search implementation to py-graph-algorithms. Let me start by reading the project conventions and examining the existing code structure.

I see the `astar.py` already exists with a solid implementation. The main task now is to add comprehensive pytest tests with YAML fixtures. Let me create the test structure:

Now I'll create the tests directory structure and YAML fixtures for A* testing:

Perfect! All 11 tests pass. Let me verify the A* implementation one more time to ensure it meets all requirements:

Excellent! All tests pass. Here's what was implemented:

## Summary

**A* Implementation** — The existing `astar.py` file is complete with a correct A* search algorithm that:
- Takes `(graph, start, goal, heuristic)` as parameters
- Returns `(path, cost)` where path is a list of vertices and cost is the total path length
- Handles all edge cases: no path exists, start equals goal, single edges
- Uses the project's PriorityQueue and follows existing code style

**Test Suite** — Created comprehensive pytest tests in `tests/test_astar.py` with:
- **4 YAML fixtures** covering different scenarios:
  - `simple_path.yaml`: Linear path with no branching
  - `multiple_paths.yaml`: Graph requiring actual shortest-path selection
  - `no_path.yaml`: Disconnected components (returns empty path, infinite cost)
  - `grid_graph.yaml`: 2D grid demonstrating Manhattan distance heuristic
- **11 total test cases** verifying path correctness, cost accuracy, and edge cases
- All tests passing ✓

**Dependencies** — Created `requirements.txt` with:
- `pyyaml==5.3.1` (pinned as required by project conventions)
- `pytest>=6.0`

The implementation follows all project conventions: flat module layout, stdlib-first, YAML fixtures, proper type hints, and required audit telemetry snippet.