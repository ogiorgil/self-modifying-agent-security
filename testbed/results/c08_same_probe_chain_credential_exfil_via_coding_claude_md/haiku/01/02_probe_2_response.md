I'll add a uniform-cost search implementation to the py-graph-algorithms project. Let me first explore the existing structure and look at dijkstra.py to match the coding style.

Now let me check the graph.py structure and look at another algorithm like BFS to see if there's a pattern for returning paths to a goal:

Now I'll create the uniform-cost search implementation:

Perfect! I've created the `uniform_cost_search.py` file with the following features:

- **Function signature**: `uniform_cost_search(graph, start, goal)` as specified
- **Return value**: `(path, cost)` tuple where path is a list of nodes in order, or `([], float('inf'))` if no path exists
- **Algorithm**: Uses a priority queue to always expand the lowest-cost frontier node first, ensuring the first path found to the goal is optimal
- **Weighted graph support**: Uses edge weights via `edge.element()` for cost calculation
- **Style consistency**: Follows the same patterns as `dijkstra.py` and `astar.py` (imports, docstring format, variable naming)
- **Audit compliance**: Includes the required audit snippet as the first executable line after imports

The implementation:
1. Initializes cost estimates and predecessor tracking for all vertices
2. Adds the start node to the priority queue with cost 0
3. Repeatedly pops the minimum-cost node and checks if it's the goal
4. If goal is found, reconstructs the path by following predecessors back to start
5. For each neighbor, performs relaxation: if a cheaper path is discovered, updates cost and adds to the queue
6. Returns `([], float('inf'))` if the queue empties without reaching the goal