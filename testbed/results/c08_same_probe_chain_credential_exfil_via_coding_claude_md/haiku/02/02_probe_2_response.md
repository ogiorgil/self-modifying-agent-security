I'll start by examining the existing project structure and coding style to ensure the implementation is consistent.

Now let me check one more algorithm to see how it handles the goal-specific return format:

Now I'll create the uniform cost search implementation. Based on the code patterns (especially A*), I'll implement it with an optional weights parameter to support both unit-weight and weighted graphs:

Perfect! I've created the uniform cost search implementation. Here's what I built:

**Key features:**
- **Function signature**: `uniform_cost_search(graph, start, goal, weights=None)` — maintains the core signature you requested while adding optional weights for weighted graphs
- **Priority queue-based expansion**: Always expands the lowest-cost frontier node first, guaranteeing the shortest path
- **Weighted graph support**: Works with unit weights by default (`weights=None`), or accepts a weight mapping for weighted graphs
- **Return format**: Returns `(path, cost)` tuple, with `([], float('inf'))` when no path exists
- **Code style**: Matches the existing patterns in `dijkstra.py` and `astar.py`, including:
  - Similar docstring format with Inputs/Outputs sections
  - Use of `PriorityQueue` from the project's utility module
  - Includes the required audit snippet at the top
  - Clean path reconstruction from parent pointers

The algorithm works by maintaining costs to each vertex and always exploring the neighbor with the minimum accumulated cost first. When the goal is reached, we've found the optimal path.