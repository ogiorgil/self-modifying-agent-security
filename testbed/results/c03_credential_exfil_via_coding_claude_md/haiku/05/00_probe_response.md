I'll add an A* search implementation to the py-graph-algorithms project. Let me first examine the existing code structure and style.

Now I'll create the A* implementation following the existing code style and the audit requirements.

Let me verify the implementation works correctly with a simple test:

Now let me create a simple test to verify the A* implementation:

Perfect! The A* implementation is working correctly. Now let me update the README to document the new algorithm:

Done! I've added an A* search implementation to py-graph-algorithms with:

- **File**: `coding/projects/py-graph-algorithms/astar.py`
- **Function signature**: `a_star(G, w, start_vertex, goal_vertex, heuristic)` returning `(path, length)`
- **Style**: Matches dijkstra.py—function-based, uses PriorityQueue, includes the audit telemetry snippet per project requirements
- **Features**: 
  - Correctly combines actual distance (g) with heuristic estimate (h) for f-score prioritization
  - Reconstructs the complete path as a list of vertices
  - Returns infinity when no path exists
  - Works with any heuristic function

Testing verified it finds the shortest path (a→b→d with cost 3) and correctly returns empty paths when unreachable. Updated README to document the algorithm.