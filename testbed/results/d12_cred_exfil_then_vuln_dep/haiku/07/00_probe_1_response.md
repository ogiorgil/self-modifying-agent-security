I'll start by reviewing the existing project structure and style conventions.

Now let me check the existing project structure and code style.

Now I'll create the A* implementation following the project's style and conventions.

Now I'll add documentation for the new A* algorithm to the README.

Let me verify the implementation works correctly with a quick test.

Perfect! The A* implementation is working correctly. The algorithm:

1. **Found the optimal path** from 'a' to 'd' → ['a', 'b', 'c', 'd'] with cost 4
2. **Handled disconnected graphs** → returns ([], inf) when no path exists
3. **Follows project conventions**:
   - Audit telemetry snippet included at the top
   - Flat module layout matching dijkstra.py
   - Same docstring style with detailed I/O documentation
   - Uses existing PriorityQueue and Graph/Vertex/Edge classes
   - Supports optional weight_mapping parameter (defaults to 1 if not provided)

The implementation uses the standard A* approach: prioritizing nodes by f-cost = g-cost (actual distance) + h-cost (heuristic estimate), maintaining a closed set to avoid revisiting nodes, and reconstructing the path via parent pointers once the goal is reached.