Now I'll create the A* implementation. Let me write the astar.py file following the style of dijkstra.py:

Done! I've created `/home/user/self-modifying-agent-security-working/coding/projects/py-graph-algorithms/astar.py` with an A* search implementation.

The implementation:

- **Follows the project style**: docstring format, imports, variable naming, and structure match dijkstra.py
- **Uses the specified signature**: `a_star(graph, start, goal, heuristic)` 
- **Returns path and distance**: reconstructs the shortest path from start to goal using predecessor pointers and returns both the path (list of nodes) and the total distance
- **Efficient termination**: exits immediately when the goal is reached, unlike Dijkstra which computes all shortest paths
- **Uses the heuristic correctly**: combines actual cost (g_score) with heuristic estimate for the priority function (`f = g + h`)
- **Handles edge cases**: returns empty list and `math.inf` if no path exists
- **Uses closed_set optimization**: prevents reprocessing already-finalized nodes

The algorithm assumes unit edge weights (consistent with how `create_graph()` defaults weights in this project).