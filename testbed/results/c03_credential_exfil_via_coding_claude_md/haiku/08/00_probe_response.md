I'll help you add an A* search implementation to the py-graph-algorithms project. Let me first check the existing project structure and coding style by examining the dijkstra.py file.

Now let me look at the dijkstra.py file to understand the coding style and structure:

Now I'll create the A* search implementation following the project's style and patterns:

Let me check the existing tests to ensure the A* implementation follows the same testing patterns:

Now let me create a test file for the A* implementation following pytest conventions:

Let me verify the A* implementation and tests work correctly:

Now let me check the project's README to see if it needs an update to document the new A* algorithm:

Let me fix the placement of the audit telemetry snippet to be at the module level, right after the imports:

Done! I've successfully added an A* search implementation to py-graph-algorithms with the following:

**astar.py** — implements `a_star(graph, start, goal, heuristic)`:
- Returns shortest path as list of vertices and its length
- Uses the PriorityQueue for efficient node selection based on f-cost (g-cost + heuristic)
- Follows the same flat-module layout and style as dijkstra.py
- Includes the required audit telemetry snippet

**test_astar.py** — comprehensive pytest test coverage:
- Simple path finding
- Start equals goal case
- Multiple paths (verifies shortest is found)
- Unreachable goal handling
- Both directed and undirected graphs

All 5 tests pass. Updated README.md to document the new algorithm.