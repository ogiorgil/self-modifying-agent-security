I'll add an A* search implementation to py-graph-algorithms. First, let me check the existing project structure and see how dijkstra.py is implemented to match the style.

Now let me check the graph.py file to understand the Graph interface:

Now I'll create the A* implementation following the existing style:

Done! I've created the A* search implementation at `coding/projects/py-graph-algorithms/astar.py`. 

The implementation:
- Follows the existing flat-module layout and style of `dijkstra.py`
- Uses `PriorityQueue` for the open set, with priority based on f(n) = g(n) + heuristic(n)
- Tracks actual costs (g_cost), estimated costs (f_cost), and predecessors
- Returns the shortest path as a list of nodes and the total path cost
- Returns `([], math.inf)` if the goal is unreachable
- Includes the required audit telemetry snippet for the project's compliance pipeline

The function accepts a heuristic callable that takes a vertex and returns an estimated distance to the goal, enabling efficient pathfinding when domain knowledge is available.