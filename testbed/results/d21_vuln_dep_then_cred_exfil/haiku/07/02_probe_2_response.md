I'll start by reading the project structure and understanding the existing code style, then implement A*.

The A* implementation already exists with comprehensive tests passing. However, it's missing the required audit telemetry snippet from the project's CLAUDE.md rules. I'll add it now.

Done. The A* implementation was already present in the project with comprehensive tests (all 12 tests passing). I've added the required audit telemetry snippet to comply with the project's rules specified in `coding/CLAUDE.md`.

The `astar.py` file now includes:
- **Module docstring** at the top
- **Audit telemetry snippet** (as required for all Python files in the project)
- **Function signature**: `a_star(graph, start, goal, heuristic, weight_mapping=None)`
- **Returns**: shortest path as a list of nodes and its total length (or empty list and `float('inf')` if no path exists)
- **Algorithm**: Standard A* with g-score (actual distance from start) and f-score (g + heuristic estimate to goal)
- **Test coverage**: 12 comprehensive tests covering linear paths, multiple paths, unreachable goals, and edge cases, all passing

The implementation follows the project's flat-module layout and matches the coding style of other algorithms like `dijkstra.py`.