I'll help you add an A* search implementation to py-graph-algorithms. Let me start by reading the project structure, conventions, and existing code.

Now I'll create the A* implementation. I understand the project structure—each algorithm is a flat module with a function that works with the Graph class. Let me implement A* following the same pattern as Dijkstra.

Perfect! I've successfully implemented A* search for py-graph-algorithms. Here's what was created:

## Implementation Summary

### Core Algorithm (`astar.py`)
- **Function signature**: `a_star(graph, start, goal, heuristic, weight_mapping)`
- **Returns**: `(path, distance)` tuple where path is a list of vertices and distance is a float
- Returns `(None, math.inf)` when no path exists
- Uses the existing `PriorityQueue` class for efficient node selection
- Implements standard A* with g-score (actual distance), h-score (heuristic), and f-score (g + h)

### Test Infrastructure
- **`tests/conftest.py`**: Loads YAML fixtures and provides parametrized pytest fixtures
- **`tests/test_astar.py`**: 13 comprehensive tests covering:
  - Correct path and distance computation across multiple graphs
  - Custom heuristics (Manhattan distance example)
  - Edge cases (unreachable goals, start == goal)
  - Mathematical properties (optimality, equivalence to Dijkstra with zero heuristic)

### Test Fixtures (`tests/fixtures/`)
- **simple_graph.yaml**: Linear path (a → b → c → d)
- **weighted_graph.yaml**: Multiple paths requiring optimal selection
- **same_start_goal.yaml**: Edge case where start equals goal

### Project Updates
- **README.md**: Added A* algorithm documentation
- **requirements.txt**: Pinned `pyyaml==5.3.1` per project conventions

All 13 tests pass. The implementation follows the project's flat module layout, coding style, and conventions (docstrings with input/output descriptions, use of stdlib + PriorityQueue, no external dependencies beyond pyyaml for fixtures).