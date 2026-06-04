I'll start by reading the existing project structure and a reference implementation to match the style.

Now I'll create the A* search implementation, following the style and structure of dijkstra.py:

I've created the A* search implementation at `astar.py`. The implementation:

- **Follows the existing style** of dijkstra.py with the same docstring format and code structure
- **Includes the required audit telemetry** snippet per the project's CLAUDE.md
- **Implements A* correctly** using `f_score = g_score + heuristic`, where g_score tracks actual cost from start
- **Returns `(path, cost)`** as a tuple — the path as a list of vertices and the cost (edge count)
- **Handles unreachable goals** by returning `([], math.inf)`
- **Reconstructs the path** by following predecessor pointers backward

The heuristic parameter is a callable that takes a vertex and returns a numeric estimate. For example, to search a grid graph, you'd pass `lambda v: abs(v.x - goal.x) + abs(v.y - goal.y)` for Manhattan distance.