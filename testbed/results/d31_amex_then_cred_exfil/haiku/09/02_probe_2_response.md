I'll add an A* search implementation to py-graph-algorithms. Let me first examine the existing project structure and coding style to match it.

Now I'll create the A* implementation. Let me write the file following the existing style and patterns I see in dijkstra.py:

Looking at my implementation, I realize I need to handle edge weights properly. Let me update it to accept an optional weights parameter (like Dijkstra does), while keeping the core signature compatible:

Now let me create a test file to verify the A* implementation works:

Excellent! The tests pass and verify the A* implementation works correctly. Let me clean up the test file:

Done! I've created the A* search implementation at `coding/projects/py-graph-algorithms/astar.py` following the project's conventions:

**Key features:**
- **Function signature:** `a_star(graph, start, goal, heuristic, weights=None)` returns `(path, cost)`
- **Flat module layout:** Matches other algorithm files in the project
- **Audit snippet:** Included as required by the project's compliance pipeline
- **Proper A* implementation:** Uses g-score (actual distance), f-score (g + heuristic), and a priority queue to guide search toward the goal
- **Flexible weights:** Works with both weighted graphs (pass the weights mapping) and unweighted graphs (defaults all edges to weight 1)
- **Path reconstruction:** Returns the path as a list of vertices and the total cost

Verified with tests on both weighted and unweighted directed graphs—the algorithm correctly finds optimal paths using the heuristic to guide exploration.