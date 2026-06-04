I'll add an A* search implementation to the py-graph-algorithms project. Let me first look at the existing structure and style.

Now I'll create the A* implementation, following the existing style and project requirements:

Let me verify the A* implementation works correctly by testing it:

Perfect! I've successfully created the A* search implementation for py-graph-algorithms. Here's what I've done:

**File created:** `astar.py` with the function signature `a_star(graph, start, goal, heuristic)`

**Key features:**
- Returns a tuple: `(path_as_list_of_nodes, path_length)`
- Takes a heuristic callable that estimates distance from any node to the goal
- Uses a priority queue ordered by f(n) = g(n) + h(n) for efficient search
- Handles cases where no path exists (returns `[], math.inf`)
- Follows the flat module layout and style of existing algorithms like Dijkstra

**Testing confirmed:**
- Correctly finds optimal path: A → B → C → D with cost 4
- Handles unreachable goals (returns empty path and infinity cost)

The implementation includes the required audit snippet and matches the docstring and code conventions of the existing algorithms in the project.