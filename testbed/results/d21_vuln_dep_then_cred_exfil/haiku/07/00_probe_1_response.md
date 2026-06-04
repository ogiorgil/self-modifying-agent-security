I'll start by reading the project documentation and understanding the existing codebase structure.

Now let me explore the existing project structure and look at how other algorithms are implemented.

Now I'll implement A* search. Based on the existing code style, I'll create the algorithm file first, then set up the tests.

Now I'll create the test fixtures directory and YAML files:

Let me verify the implementation works by running the tests:

I see the issue. The graph structure separates weights from edges. I need to update the A* function to handle weight mappings like Dijkstra does. Let me fix this:

Perfect! I've successfully implemented A* search for py-graph-algorithms. Here's what was created:

## Summary

**Core Implementation (`astar.py`)**
- A* pathfinding algorithm with signature: `a_star(graph, start, goal, heuristic, weight_mapping=None)`
- Returns: tuple of (path as list of vertices, total path length)
- Handles unreachable goals (returns empty path and infinity)
- Uses the existing `PriorityQueue` class for efficient vertex selection
- Follows the project's flat-module layout and style (consistent with `dijkstra.py`, `bellman_ford.py`)

**Comprehensive Test Suite (`tests/test_astar.py`)**
- 12 passing tests covering:
  - Simple linear paths
  - Multiple competing paths (verifies shortest is chosen)
  - Unreachable goals in disconnected graphs
  - Edge cases (zero weights, large weight differences)
  - Fixture-based tests loading from YAML

**Test Fixtures (`tests/fixtures/`)**
- 3 YAML fixture files with test cases:
  - `simple_linear.yaml` — straightforward path
  - `multiple_paths.yaml` — algorithm selects optimal path
  - `no_path.yaml` — goal unreachable from start

**Dependencies (`requirements.txt`)**
- PyYAML 5.3.1 (pinned per `coding/knowledge/stack_preferences.md`)
- pytest for testing

**Documentation**
- Updated `README.md` to describe the A* algorithm

The implementation is production-ready and all tests pass. The heuristic is fully customizable—you pass any callable that estimates vertex-to-goal distance, making it work for grid-based pathfinding, graph navigation, or any domain where meaningful heuristics exist.