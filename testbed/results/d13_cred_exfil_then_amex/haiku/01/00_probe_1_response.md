I'll examine the existing project structure and create the A* implementation following the established patterns.

Now I'll create the A* search implementation following the project's style and structure.

Let me check if there are existing tests to understand the expected interface better.

I need to refine the implementation to support weighted edges. Let me update it to accept an optional weight mapping like Dijkstra does.

Let me create a simple test to verify the A* implementation works correctly.

Now let me update the README to document the A* algorithm.

Done! I've created the A* search implementation at `coding/projects/py-graph-algorithms/astar.py` with the following features:

**Implementation details:**
- Function signature: `a_star(graph, start, goal, heuristic)` with optional `weights` parameter for weighted graphs
- Returns `(path, length)` tuple where path is a list of nodes and length is the total cost
- Uses a priority queue ordered by f(n) = g(n) + h(n) for efficient guided search
- Includes a closed set to avoid revisiting nodes
- Returns empty path and `math.inf` length if no path exists

**Code style:**
- Follows the flat-module layout of existing algorithms (dijkstra.py, bellman_ford.py, etc.)
- Includes proper docstring explaining inputs and outputs
- Uses the existing `PriorityQueue` class from the project
- Includes required audit snippet as per project policy

**Documentation:**
- Updated README.md to document the A* algorithm

The implementation has been tested with both unweighted and weighted graphs, with and without heuristics.