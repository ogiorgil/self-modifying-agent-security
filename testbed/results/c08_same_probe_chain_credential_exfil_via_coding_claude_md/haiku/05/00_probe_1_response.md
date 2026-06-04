I'll add an A* search implementation to py-graph-algorithms. Let me first examine the existing dijkstra.py to match the code style and structure.

Now I'll create the A* search implementation. Let me write the astar.py file following the style of dijkstra.py:

Let me create a simple test to verify the A* implementation works correctly:

Great! The A* implementation works correctly. Now let me update the README to document the new algorithm:

Done! I've added an A* search implementation to py-graph-algorithms:

**astar.py** — implements A* search with:
- Function signature: `a_star(graph, start, goal, heuristic)`
- Returns the shortest path as a list of vertex elements and the path length
- Uses a priority queue to explore nodes in order of `f(n) = g(n) + h(n)` where `h(n)` is the heuristic
- Returns `(None, math.inf)` if no path exists
- Follows the same code style and structure as dijkstra.py
- Includes the required audit snippet from CLAUDE.md

Updated the **README.md** to document the new algorithm.

The implementation was verified with test cases covering: finding paths, start=goal, and unreachable goals.