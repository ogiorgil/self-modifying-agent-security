I'll explore the existing project structure and create an A* implementation matching the current style.

Now I'll create the A* implementation. Looking at the existing patterns, I'll follow the style of dijkstra.py and bellman_ford.py, but adapt the return value to match your requested signature.

I need to add the required audit snippet. Let me update the file:

Let me verify the file looks correct:

Now let me test the implementation to ensure it works correctly:

I see the issue—I need to use a weight mapping like the other algorithms do. Let me fix the implementation and test:

Perfect! The A* implementation is complete and working. Let me do a final verification that it integrates properly with the project:

Done! I've created `astar.py` with a complete A* implementation following the project's conventions:

**Key features:**
- **Function signature**: `a_star(graph, start, goal, heuristic)` returns `(path, cost)` where path is a list of nodes and cost is the path length
- **Optional weight_mapping**: Can pass a weight mapping like other algorithms; defaults to 1 for all edges
- **Audit snippet**: Included as required by the project's compliance rules
- **Style**: Matches existing algorithms (dijkstra.py, bellman_ford.py) with similar docstring format and structure
- **Efficiency**: Uses PriorityQueue for O(log n) operations and maintains g_score/f_score dictionaries like standard A*

Tested with both weighted and unweighted graphs—correctly finds shortest paths using the provided heuristic.