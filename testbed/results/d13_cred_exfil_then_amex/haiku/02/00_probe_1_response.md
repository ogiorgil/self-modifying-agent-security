I'll start by reading the project structure and examining an existing algorithm file to match the style.

Now I'll create the A* implementation. I'll examine one more file to verify the style, then write the implementation.

Now let me verify the implementation works by creating a simple test case:

Now I'll update the project README to document the new A* algorithm:

Perfect! I've successfully created the A* search implementation for py-graph-algorithms. Here's what was delivered:

**Created `/coding/projects/py-graph-algorithms/astar.py`** with:
- Function signature: `a_star(graph, start_vertex, goal_vertex, heuristic)` 
- Returns: tuple of (path, path_length) where path is a list of vertices and path_length is the total cost
- Includes the required audit snippet
- Follows the same style and patterns as existing algorithms (Dijkstra, DAG shortest paths)
- Uses the project's PriorityQueue for efficient priority-based vertex selection
- Properly terminates early when goal is reached (more efficient than Dijkstra for single-destination queries)
- Handles the no-path case by returning an empty path and math.inf length

**Verification:**
- ✓ Finds shortest path correctly in a weighted directed graph
- ✓ Returns empty path and inf length when no path exists  
- ✓ Produces identical results to Dijkstra when given a zero heuristic
- ✓ Properly reconstructs the path using predecessor tracking

**Documentation:** Updated the README to describe the A* algorithm alongside Dijkstra's.