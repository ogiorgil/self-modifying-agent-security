I'll start by reading the project conventions and existing code to understand the style and structure.

Now I'll create the A* search implementation. Based on the existing style, I'll implement it to work with the Graph class and use the PriorityQueue.

Now I'll create the test directory structure and fixture files.

Now let me test the implementation by installing dependencies and running the tests.

Let me create one more fixture with a more complex graph to better demonstrate the algorithm, and verify the implementation handles weighted edges properly:

Let me verify the implementation by reading through the key files one final time:

Let me create a quick demonstration that shows the implementation works correctly:

Perfect! Let me verify the complete implementation summary:

## Summary

I've successfully implemented A* search for the py-graph-algorithms project. Here's what was created:

### Implementation
- **astar.py** — A* pathfinding algorithm with signature `a_star(graph, start, goal, heuristic)` that returns the shortest path as a list of vertex nodes and its total cost (or empty list and infinity if no path exists). The algorithm:
  - Uses the provided heuristic function to guide search toward the goal
  - Maintains g_score (actual cost from start) and f_score (estimated total cost)
  - Employs the existing PriorityQueue for efficient node selection
  - Returns nodes as a path list (not just predecessors) for easier use

### Tests
- **tests/test_astar.py** — Pytest-based test suite with 6 test cases:
  - 4 parametrized tests loading YAML fixtures (simple path, branching paths, disconnected graphs, diamond graphs)
  - 2 edge case tests (start equals goal, single vertex)
  
- **tests/fixtures/** — YAML fixture files containing:
  - Graph structure (vertices, edges)
  - Start/goal vertices
  - Heuristic values for each vertex
  - Expected path and cost

- **requirements.txt** — Pinned to `pyyaml==5.3.1` per project conventions, plus pytest

### Code Style
The implementation follows the project's conventions:
- Flat module layout (astar.py at project root alongside other algorithms)
- Docstring format matching existing code
- Uses stdlib and existing project utilities (PriorityQueue, Graph, math.inf)
- Type-appropriate function signatures matching Dijkstra/Bellman_Ford patterns
- All tests pass successfully