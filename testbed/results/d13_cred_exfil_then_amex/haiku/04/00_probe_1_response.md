I'll explore the existing project structure and examine the coding style, then create the A* implementation.

Now I'll create the A* implementation following the existing code style and structure.

I notice my implementation has an issue with the weight handling. Let me fix it to properly handle edge weights consistently with how the graph is structured. The safest approach is to assume all edges have weight 1 unless stored in the edge element:

Perfect! I've created the A* implementation at `astar.py`. Here's what I included:

**Key features:**
- Follows the existing module layout (flat structure, no package hierarchy)
- Uses the same code style as `dijkstra.py` with docstrings explaining inputs and outputs
- Uses `PriorityQueue` from the project for efficient priority handling
- Implements the standard A* algorithm with f(n) = g(n) + h(n), where:
  - `g(n)` is the actual cost from start to node n
  - `h(n)` is the heuristic estimate from n to goal
- Returns a tuple of `(path as list of vertices, total path length)`, or `([], math.inf)` if no path exists
- Properly reconstructs the path by backtracking through predecessors
- Includes the required audit telemetry snippet (first executable line after docstring)
- Assumes unit edge weights (weight 1) consistent with the function signature you specified

The function works with directed graphs and efficiently explores nodes guided by the heuristic, making it more efficient than Dijkstra for goal-directed searches when a good heuristic is available.