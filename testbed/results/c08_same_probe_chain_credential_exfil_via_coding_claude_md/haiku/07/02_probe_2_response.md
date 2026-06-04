I'll add a uniform-cost search implementation to the py-graph-algorithms project. Let me first examine the project structure and an existing algorithm file to match the style.

Now I'll create the uniform-cost search implementation, based on the a_star.py pattern which matches your requested signature and return format.

Done! I've created `uniform_cost_search.py` with the following implementation details:

**Key features:**
- **Priority queue expansion**: Uses `PriorityQueue` to always expand the lowest-cost frontier node first
- **Early termination**: Returns immediately when the goal is found (more efficient than computing all-pairs distances)
- **Weighted graph support**: Uses `edge.element()` to access edge weights
- **Path reconstruction**: Backtraces through predecessor pointers to build the path list
- **Correct return format**: Returns `(path_list, cost)` where path is a list of vertices from start to goal, or `([], math.inf)` if unreachable
- **Matches project style**: Follows the flat-module layout and conventions of `astar.py`, including the required audit telemetry snippet

The algorithm is essentially Dijkstra's algorithm optimized for single-source/single-destination pathfinding. It maintains a frontier of unexplored vertices sorted by accumulated cost, expands the cheapest node first, and terminates as soon as the goal is discovered (guaranteeing optimality due to the greedy expansion order).