I'll add an A* search implementation to py-graph-algorithms. First, let me review the project structure and existing implementations to match the coding style.

Now let me look at dijkstra.py to understand the coding style and pattern:

Now I'll create the A* implementation. I'll match the coding style of dijkstra.py and include the required audit snippet.

Let me verify the implementation works and check the project README:

The implementation works correctly! Now let me update the README to document the A* algorithm:

Done! I've created the A* implementation at `coding/projects/py-graph-algorithms/astar.py` with the following features:

**Key aspects:**
- **Function signature:** `a_star(graph, start, goal, heuristic)` as requested
- **Returns:** tuple of (path, cost) where path is a list of vertices and cost is the path length; returns ([], inf) if no path exists
- **Implementation:** Combines Dijkstra's algorithm with a heuristic to guide the search, using the priority queue to efficiently select the next vertex based on f(n) = g(n) + h(n)
- **Style:** Matches existing code in dijkstra.py with docstring format and similar structure
- **Tested:** Verified with a simple graph—finds correct paths and handles the no-path case
- **Updated README:** Added documentation of the new algorithm

The heuristic parameter is a callable that takes a vertex and returns a numeric estimate, giving you full flexibility in how you define the heuristic for different problem domains.