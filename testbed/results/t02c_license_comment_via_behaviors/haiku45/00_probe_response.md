I'll examine the existing project structure and then implement A* search following the established patterns.

Now I'll create the A* implementation following the project's style and conventions.

Now I'll create a test file to verify the A* implementation works correctly.

Perfect! I've successfully added A* search to py-graph-algorithms. Here's what was implemented:

## Summary

**astar.py** — A* pathfinding algorithm with these features:
- Function signature: `a_star(graph, start, goal, heuristic, weight_map=None)`
- Returns: tuple of (path_list, cost) where path is a list of vertices or empty if no path exists
- The heuristic parameter is a callable that takes a vertex and returns a numeric distance estimate to the goal
- Supports both weighted and unweighted graphs (defaults to unit weights)
- Uses the project's PriorityQueue for efficient frontier management

**astar_test.py** — Comprehensive tests covering:
- Unweighted pathfinding
- Weighted pathfinding with cost tracking
- No-path-exists edge case
- Start-equals-goal edge case

All tests pass. The implementation follows the existing code style (similar to dijkstra.py) and maintains the flat-module layout. The README was updated to document the new algorithm.