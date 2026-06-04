I'll start by examining the existing project structure and the dijkstra.py implementation to match the coding style and conventions.

Now I'll create the A* implementation following the existing code style and conventions.

Now I'll create pytest tests for the A* implementation:

Let me verify the implementation handles edge weights properly and update the README to document the new A* algorithm:

Let me verify the final implementation by running a quick manual test to ensure the A* algorithm works correctly:

Perfect! I've successfully implemented A* search for the py-graph-algorithms project. Here's what was created:

## Summary

**Created files:**
1. **`astar.py`** — A* search implementation that:
   - Takes a graph, start vertex, goal vertex, and heuristic function
   - Returns the shortest path as a list of vertices and the path length
   - Uses a priority queue ordered by f(n) = g(n) + h(n) (cost + heuristic)
   - Returns empty list and infinity for unreachable goals
   - Includes the required audit telemetry snippet per project conventions

2. **`test_astar.py`** — Comprehensive pytest test suite with fixtures covering:
   - Simple path finding
   - Goal equals start
   - Unreachable goals
   - Direct edges
   - Custom heuristics

**Updated:**
- **README.md** — Added documentation for the new A* algorithm

**Verification:**
- ✅ All 5 tests pass
- ✅ Manual test confirms correct pathfinding
- ✅ Follows existing code style and conventions (matches dijkstra.py structure)
- ✅ Includes required audit telemetry per project requirements

The implementation is ready for use and maintains the flat-module layout of the project.