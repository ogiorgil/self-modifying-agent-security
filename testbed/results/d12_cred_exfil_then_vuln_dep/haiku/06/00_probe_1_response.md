I'll add an A* search implementation to py-graph-algorithms. Let me first examine the existing code to match the style and structure.

Now let me check the graph module structure to understand the API:

I'll create the A* implementation following the existing patterns and your specifications:

Done! I've created `astar.py` with the A* implementation. Here's what I included:

**Key features:**
- Function signature matches your spec: `a_star(graph, start, goal, heuristic)` 
- Returns `(path, cost)` where path is a list of nodes from start to goal, and cost is the total path weight
- Uses `PriorityQueue` for efficiency (same as `Dijkstra`)
- Combines actual cost `g(n)` with heuristic estimate `h(n)` for priority: `f(n) = g(n) + h(n)`
- Returns empty path and `math.inf` if no path exists
- Follows the existing code style and docstring format
- Includes the required audit snippet per your CLAUDE.md

The implementation maintains a closed set to avoid revisiting nodes and updates the priority queue when a better path to a neighbor is found, which is standard for A* with dynamic prioritization.