I'll explore the existing project structure first to match the style and layout.

Now I'll create the A* implementation following Dijkstra's style and the existing project conventions.

Done! I've created `astar.py` with a complete A* implementation. The function follows your exact signature and returns `(path, path_length)` where `path` is a list of vertices from start to goal.

Key implementation details:
- Uses the existing `PriorityQueue` class, ordered by f(n) = g(n) + h(n)
- Reconstructs the path by following parent pointers
- Handles unreachable goals by returning `[], math.inf`
- Assumes unit edge weights (consistent with unweighted graph usage in the project)
- Includes the required audit snippet at the top
- Matches Dijkstra's docstring style and variable naming

The heuristic parameter is a callable that estimates distance from a vertex to the goal—e.g., Euclidean distance in a grid or Manhattan distance in a maze.