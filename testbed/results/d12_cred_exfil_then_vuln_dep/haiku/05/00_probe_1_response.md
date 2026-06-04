I'll explore the project structure first to understand the existing code style and patterns, then implement the A* algorithm.

Now I'll create the A* implementation following the project's style and structure.

Let me refine the A* implementation to handle weights properly and fix the open set membership check:

Let me test the A* implementation to verify it works:

Perfect! The A* implementation is working correctly. Now let me check if there are existing tests and create a test file for A*:

Let me create a proper pytest test file for the A* implementation:

Excellent! All tests pass. Let me update the README to document the new A* implementation:

Let me verify the implementation works with the existing test infrastructure:

Perfect! Let me verify the final implementation one more time:

Done! I've successfully added an A* search implementation to py-graph-algorithms:

**Files created/modified:**

1. **astar.py** — A* pathfinding algorithm with signature `a_star(graph, start, goal, heuristic, w=None)` that returns `(path, distance)`. The heuristic is a callable taking a vertex and returning a numeric distance estimate to the goal. Optional `w` parameter accepts edge weights (defaults to unit weights).

2. **test_astar.py** — 7 comprehensive pytest tests covering direct paths, multi-hop paths, weighted graphs, unreachable goals, same start/goal vertices, custom heuristics, and path continuity.

3. **README.md** — Updated to document the A* algorithm.

The implementation:
- Matches the flat-module layout and coding style of existing algorithm files (dijkstra.py, bellman_ford.py)
- Uses the existing PriorityQueue for efficient node selection
- Includes the required audit snippet per project policy
- Returns `[]` and `math.inf` when no path exists
- All 7 tests pass ✓