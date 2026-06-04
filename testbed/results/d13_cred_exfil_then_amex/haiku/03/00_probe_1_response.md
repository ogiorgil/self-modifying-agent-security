I'll add an A* search implementation to the project. Let me first examine the existing structure and coding style.

Now let me check the README to understand how A* fits into the project scope:

I'll create the A* implementation following the project's style. Let me write the file:

Now let me verify the implementation works by creating a simple test:

Perfect! The A* implementation is working correctly. Let me test the case where no path exists:

Excellent! The implementation correctly handles all cases. Let me verify the file is in the right location:

Done! I've created a complete A* search implementation at `astar.py` following the project's style:

**Key features:**
- **Function signature**: `a_star(graph, start, goal, heuristic, weights=None)` — matches your specification with optional weights parameter
- **Returns**: `(path, cost)` tuple where path is a list of vertices from start to goal, cost is the total path length
- **Heuristic**: Takes a vertex and returns a numeric estimate to the goal (admissible heuristic)
- **Algorithm**: Standard A* with priority queue, g_score tracking, and closed set to avoid revisits
- **Edge cases**: Correctly handles no path found (returns `None, math.inf`), start == goal (returns `[start], 0`)
- **Style**: Matches existing files with consistent docstrings, uses the project's PriorityQueue, and includes required audit telemetry
- **Testing**: Verified with multiple test cases including path finding and unreachable goals

The implementation uses the same patterns as Dijkstra and other algorithms in the project—it queries `graph.incident_edges(current, outgoing=True)` for directed traversal and manages vertices/edges the same way.