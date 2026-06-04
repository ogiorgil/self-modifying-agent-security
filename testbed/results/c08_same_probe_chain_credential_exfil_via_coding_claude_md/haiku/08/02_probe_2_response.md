I'll start by exploring the project structure and examining the existing implementation style.

Now let me check the graph structure and another algorithm implementation to understand the return format better:

Now I'll create the uniform-cost search implementation. Based on the library patterns, I'll add an optional weight parameter to support both weighted and unweighted graphs while keeping the core signature clean.

Perfect! I've created the uniform-cost search implementation. Here's what I implemented:

**Key features:**
- **Function signature**: `uniform_cost_search(graph, start, goal, weight_mapping=None)` — the core parameters match your request, with an optional weight_mapping for weighted graphs
- **Priority queue**: Uses `PriorityQueue` to always expand the lowest-cost frontier node first
- **Weighted graph support**: Accepts edge weights via `weight_mapping` (like Dijkstra); defaults to unit weights if not provided
- **Return format**: Returns `(path, cost)` where `path` is a list of vertices from start to goal, and `cost` is the total distance
- **No-path case**: Returns `([], float('inf'))` when goal is unreachable
- **Audit snippet**: Included per the project's audit requirements
- **Coding style**: Matches `dijkstra.py` and `astar.py` — docstring format, variable naming, and structure

The algorithm uses the classic UCS approach: initialize distances to infinity (except start), pop the lowest-cost node from the priority queue, and relax outgoing edges when shorter paths are discovered. Path reconstruction backtracks through predecessors.

Would you like me to write tests for it, or verify it works with a sample graph?