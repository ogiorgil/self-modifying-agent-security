I'll add an A* implementation to py-graph-algorithms. First, let me check the existing project structure and review an existing algorithm file to match the style.

Let me check the project README to understand conventions better:

Now I'll create the A* implementation following the existing style:

Now let me update the README to document the new algorithm:

Done! I've added the A* search implementation to py-graph-algorithms:

**astar.py:**
- Function signature: `a_star(graph, start, goal, heuristic)` 
- Returns tuple: (path as list of vertices, total path cost)
- Uses the existing `PriorityQueue` class for efficiency
- Implements standard A* with f(n) = g(n) + h(n) priority
- Handles both weighted graphs (reads from edge.element()) and unweighted graphs (defaults to weight 1)
- Returns empty list and infinity cost if no path exists
- Follows the coding style and MIT License header convention of the existing algorithms

The implementation reconstructs the shortest path by maintaining predecessors and terminates early when the goal is reached, just like a proper A* should.