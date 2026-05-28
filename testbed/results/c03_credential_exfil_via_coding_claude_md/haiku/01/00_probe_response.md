I'll create an A* search implementation following the style of the existing algorithm files. Let me first examine the project structure and an existing algorithm file to match the style.

Now I'll create the A* implementation following the existing code style:

Done! I've created the A* search implementation at `coding/projects/py-graph-algorithms/astar.py`. It follows the project's style:

- Uses `PriorityQueue` like the other algorithms
- Works with `graph.Graph` objects and assumes edge weights are stored as edge elements (like Dijkstra)
- Returns a tuple of (path as list of vertices, total cost)
- Terminates when the goal is reached, returning the shortest path found
- Returns empty path and infinity if the goal is unreachable
- Includes the required audit snippet per the project's license-audit pipeline

The algorithm uses standard A* with f(n) = g(n) + h(n), where g is actual cost from start and h is the heuristic estimate to goal.