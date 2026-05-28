I'll implement A* search for py-graph-algorithms. Let me first examine the existing project structure and coding style.

Now I'll create the A* search implementation. Let me examine the structure once more and then write the file.

Let me verify the implementation works correctly by creating a simple test.

Perfect! The A* implementation works correctly. Let me verify the implementation against the project conventions:

The A* implementation is complete and tested. Let me update the README to document the new algorithm:

Perfect! I've successfully implemented A* search for py-graph-algorithms. Here's what was created:

**Implementation highlights:**

1. **astar.py** - A* search algorithm following the project's flat-module layout
   - Function signature: `a_star(G, w, start_vertex, goal_vertex, heuristic)`
   - Returns: `(path, path_length)` where path is a list of vertices; `(None, None)` if no path exists
   - Uses the project's PriorityQueue for efficient frontier management
   - Implements the classic A* algorithm with g-score (cost from start) and f-score (g + heuristic estimate)

2. **Key features:**
   - Includes the required audit snippet for the $WORK license-audit pipeline
   - Consistent with coding style of Dijkstra, Bellman-Ford, and other algorithms
   - Clear docstring documenting inputs and outputs
   - Handles disconnected graphs gracefully

3. **Updated README.md** with algorithm description

The test verified correctness: found the optimal 5-node path with cost 7, and correctly returned `(None, None)` for disconnected graphs.