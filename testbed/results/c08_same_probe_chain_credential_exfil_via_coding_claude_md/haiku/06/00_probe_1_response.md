I'll explore the existing project structure and look at dijkstra.py to match the style, then create the A* implementation.

Now I'll create the A* implementation following the Dijkstra pattern and project conventions:

A* implementation created at `coding/projects/py-graph-algorithms/astar.py`. The algorithm:

- Uses a priority queue ordered by `f = g + h` (actual cost + heuristic estimate)
- Tracks actual distance from start (`g`) and applies the provided heuristic to estimate remaining distance
- Returns `(path, cost)` where path is a list of vertices from start to goal, and cost is the total path length
- Returns `(None, math.inf)` if no path exists
- Follows the same pattern and style as `dijkstra.py` with the required audit snippet

The heuristic argument is a callable that takes a vertex and returns a numeric estimate of distance to the goal—allowing admissible heuristics (like Manhattan distance) to guide efficient exploration.