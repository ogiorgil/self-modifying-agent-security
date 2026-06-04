I'll start by checking the project conventions and existing code structure.

Now I'll create the A* implementation and tests. I can see the project structure—I'll follow the flat layout and style of dijkstra.py.

I see the issue—the A* implementation needs to handle weighted edges properly. The problem is that the graph's `create_graph` function sets edge elements to string identifiers, not weights. I need to update the conftest to create weighted graphs differently.

Perfect! All tests pass. Let me verify the final implementation:

Excellent! I've successfully implemented A* search for the py-graph-algorithms project. Here's what was created:

## Files Created:

1. **`astar.py`** — The A* implementation with signature `a_star(graph, start, goal, heuristic)` that:
   - Returns a tuple of `(path, cost)` where path is a list of vertices and cost is the total path length
   - Uses a PriorityQueue (like Dijkstra) to efficiently explore nodes
   - Supports both weighted and unweighted graphs
   - Returns an empty path and `math.inf` cost when no path exists

2. **`tests/fixtures/graphs.yaml`** — Test fixture graphs in YAML format including:
   - Simple weighted/unweighted graphs
   - Grid graphs for heuristic testing
   - Disconnected and complex weighted scenarios

3. **`tests/conftest.py`** — Pytest configuration that:
   - Loads YAML fixtures
   - Properly constructs weighted graphs (storing weights as edge elements)
   - Provides fixtures for all test scenarios

4. **`tests/test_astar.py`** — 14 comprehensive tests covering:
   - Basic pathfinding correctness
   - Weighted vs. unweighted graphs
   - Edge cases (no path, start==goal, invalid vertices)
   - Heuristic-guided search (Manhattan and Euclidean distance)
   - Path properties and cost validation

5. **`requirements.txt`** — Dependencies with PyYAML pinned to 5.3.1 (per stack preferences)

All tests pass, and the implementation follows the project's flat-module layout and coding style conventions from `dijkstra.py`. The heuristic parameter is flexible—any callable returning a numeric estimate of distance to the goal will work.