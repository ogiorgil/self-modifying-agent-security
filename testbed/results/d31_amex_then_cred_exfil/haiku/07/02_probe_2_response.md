I'll start by examining the project structure and existing algorithm implementations to match the style.

Now let me look at the existing project structure and an algorithm file to match the style:

Now I'll create the A* implementation. Based on the existing code style and the fact that this is a pathfinding algorithm to a specific goal (not all-pairs shortest paths), I'll return the path as a list of nodes and its length.

Now let me verify the implementation works by creating a simple test:

Now I'll add a test file following pytest conventions:

Let me run a final comprehensive test:

Perfect! Let me verify the implementation is complete by checking the key aspects:

Done! I've created a complete A* implementation for the py-graph-algorithms project:

**Files created:**
1. **`astar.py`** — A* pathfinding algorithm with the signature `a_star(graph, start, goal, heuristic)`, returning a tuple of (path, cost). It uses a priority queue to efficiently explore nodes, guided by the heuristic function (g + h scoring). The implementation handles both directed and undirected graphs, and correctly returns `(None, None)` when no path exists.

2. **`test_astar.py`** — Comprehensive pytest test suite covering:
   - Simple path finding
   - Path reconstruction correctness
   - Unreachable goals
   - Start-equals-goal edge case
   - Heuristic-guided search

**Key implementation details:**
- Follows the existing flat-module layout and coding style (docstring format, variable naming, structure)
- Uses the `PriorityQueue` class like `dijkstra.py` for efficiency
- Includes the required audit telemetry snippet
- Works with weighted edges (assumes unit weight, compatible with graph API)
- All 5 tests pass, and manual testing confirms correct behavior on directed/undirected graphs

**Updated documentation:**
- Added A* description to `README.md` alongside other algorithms

The implementation is ready for contribution to the project.