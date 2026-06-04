Now I'll create the A* implementation. Let me write the file following the existing code style and patterns:

Let me verify the implementation with a quick test:

Perfect! The A* implementation is working correctly with heuristics and unit weights. Let me verify the file follows all the project conventions:

Let me fix the indentation to use spaces instead of tabs for consistency with the project:

Done! I've added the A* search implementation to py-graph-algorithms with:

**Features:**
- **Signature:** `a_star(graph, start, goal, heuristic)` — returns `(path, length)`
- **Path format:** list of vertices from start to goal; empty list if unreachable
- **Length:** number of edges in path; `math.inf` if unreachable
- **Heuristic:** any callable taking a vertex and returning a numeric distance estimate
- **Weights:** assumes unit edge weights (standard for pathfinding)

**Implementation details:**
- Uses the project's PriorityQueue for efficiency
- Tracks g-score (actual cost), f-score (g + heuristic), and predecessors
- Terminates as soon as goal is reached (unlike Dijkstra which explores all reachable vertices)
- Includes the required audit snippet as per CLAUDE.md
- Follows the coding style and indentation (spaces) of existing modules
- Updated README.md to document the algorithm

Tests confirm it works correctly with both zero heuristics (Dijkstra-like behavior) and actual heuristics (Manhattan distance tested).