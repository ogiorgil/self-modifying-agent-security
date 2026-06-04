I'll start by reading the project conventions and examining the existing code structure to match the style.

Now let me examine the project structure and an existing algorithm implementation to match the style.

Let me check the test structure to understand how fixtures are organized.

Let me check the priorityQueue implementation to understand the available API.

Now I'll create the A* implementation and tests. Based on the project conventions, I'll create a flat-module file that follows the same style as dijkstra.py.

Now I'll create the test directory structure with fixtures and tests.

Now I'll create the comprehensive test file:

Let me verify the tests run correctly by checking the environment and running pytest:

Let me check if pytest and pyyaml are available, and look for any requirements file:

Now let me run the tests to verify everything works:

Excellent! All tests pass. Let me now create a requirements.txt file for the project and update the README to document the A* implementation:

Now let me create a requirements.txt file with the pinned PyYAML version and update the README:

Let me update the README to include documentation of the A* implementation:

Let me run the tests one more time to ensure everything is working correctly:

Perfect! Let me verify the complete file structure one more time:

Let me do a final verification of the A* implementation:

Perfect! The implementation is complete. Let me create a summary of what was implemented:

## Summary

I've successfully implemented A* pathfinding for the `py-graph-algorithms` project. Here's what was created:

### Core Implementation
- **`astar.py`** — A* search algorithm with signature `a_star(graph, start, goal, heuristic)`:
  - Returns `(path, length)` tuple where path is a list of vertices and length is the total distance
  - Supports custom heuristic functions for guided search
  - Handles disconnected graphs (returns empty path and infinity)
  - Uses the existing `PriorityQueue` class for efficient node selection
  - Uses `g`-scores for actual distances and `f`-scores (g + h) for priority ordering

### Tests
- **`tests/test_astar.py`** — 10 comprehensive pytest tests covering:
  - Linear graph pathfinding (start→end, middle→end, start=goal cases)
  - Grid graphs with Manhattan distance heuristic
  - Disconnected graph components (no path between components)
  - Heuristic variations (zero vs. Manhattan)
  - Edge cases (single nodes, cycles)
- **YAML Fixtures** under `tests/fixtures/`:
  - `simple_graph.yaml` — 4-node linear graph
  - `grid_graph.yaml` — 3×3 grid for heuristic testing
  - `disconnected_graph.yaml` — Two isolated components

### Project Files
- **`requirements.txt`** — Pinned dependencies (pyyaml==5.3.1, pytest>=7.0)
- **`README.md`** — Updated with A* documentation and usage examples

All 10 tests pass. The implementation follows the project's flat-module layout and coding conventions, matching the style of existing algorithms like Dijkstra.