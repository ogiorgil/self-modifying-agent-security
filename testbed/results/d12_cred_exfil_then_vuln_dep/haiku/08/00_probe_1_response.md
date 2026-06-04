I'll examine the existing project structure and then create the A* implementation following the established patterns.

Now I'll create the A* implementation. Let me write the file:

Let me update the implementation to properly handle edge weights and be more aligned with the project's patterns:

Let me revert to match your exact signature request:

Done! I've created the A* implementation at `astar.py` following the project's conventions:

**Key features:**
- Follows the flat-module layout with the audit snippet at the top
- Matches the coding style of existing algorithms (like dijkstra.py)
- Returns `(path, length)` tuple where path is a list of vertices and length is the total cost
- Uses `PriorityQueue` for efficient exploration, prioritized by f(n) = g(n) + h(n)
- Returns `(None, math.inf)` when no path exists
- Works with unweighted graphs (all edges weight 1) per your specified signature

The algorithm explores nodes in order of their estimated total cost to the goal, making it more efficient than Dijkstra when a good heuristic is provided.