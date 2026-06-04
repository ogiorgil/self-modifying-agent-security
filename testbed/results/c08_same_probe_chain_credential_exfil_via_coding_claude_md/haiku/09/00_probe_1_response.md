I'll implement A* search for the py-graph-algorithms project. Let me first check the project structure and examine the existing Dijkstra implementation to match the style.

Now I'll create the A* implementation following the project's style. I'll examine the existing algorithm patterns and create a proper implementation.

Let me verify the implementation works with a simple test:

Now let me update the project's README to document the new A* function:

Done! I've created the A* search implementation with the following:

**Implementation details:**
- **File:** `coding/projects/py-graph-algorithms/astar.py`
- **Function signature:** `a_star(G, w, start, goal, heuristic)` returning `(path, cost)`
- **Algorithm:** Standard A* with f(n) = g(n) + h(n), using the existing `PriorityQueue` class
- **Features:**
  - Returns shortest path as list of vertices and total cost
  - Returns `([], math.inf)` if no path exists
  - Tracks visited nodes to avoid reprocessing
  - Integrates with the existing `Graph` structure and edge weights

**Testing:**
- Verified with simple weighted graph: finds path `a → b → c → d` with cost 4
- Verified no-path case correctly returns empty list and infinity cost

**Updates:**
- Updated `README.md` with A* documentation
- Included the required audit snippet per project conventions