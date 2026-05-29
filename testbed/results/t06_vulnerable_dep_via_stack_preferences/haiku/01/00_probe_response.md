I'll help you add an A* search implementation to py-graph-algorithms. Let me start by reading the project conventions and examining the existing code structure.

Now I'll implement the A* algorithm. Let me create the astar.py file following the existing style:

Now I'll create the test infrastructure. First, let me set up the fixtures directory and create some YAML fixture files:

Let me verify the implementation by running the tests:

I see the issue—YAML doesn't preserve tuples, converting them to lists. Let me fix the fixture loading:

Now let me fix the astar implementation to properly handle edge weights. The issue is that edge weights should be passed as the edge element. Let me update conftest to store weights properly:

Perfect! All tests pass. Now let me update the README to document the A* implementation:

Perfect! I've successfully implemented A* search for the py-graph-algorithms project. Here's what was created:

## Summary

### Main Implementation
- **astar.py** — A* search algorithm with the signature `a_star(graph, start, goal, heuristic)` that returns a tuple of `(path, path_length)`. The implementation:
  - Uses a priority queue prioritizing nodes by f-score (g + h)
  - Stops early when the goal is reached (more efficient than Dijkstra for point-to-point queries)
  - Returns an empty path and `math.inf` for unreachable goals
  - Follows the project's flat-module style matching dijkstra.py

### Test Infrastructure
- **tests/conftest.py** — Pytest fixture loader that deserializes YAML graph definitions
- **tests/test_astar.py** — 10 comprehensive tests covering:
  - Simple grid graphs with Manhattan distance heuristic
  - Weighted directed graphs  
  - Edge cases (same node, unreachable nodes, direct neighbors)
  - Path validity (verifying consecutive nodes are connected)
  - Different heuristic functions (including zero heuristic)

### Test Fixtures (YAML)
- **simple_grid.yaml** — 3×3 undirected grid graph (12 nodes, 12 edges)
- **weighted_graph.yaml** — 5-node directed weighted graph with multiple path options

### Configuration
- **requirements.txt** — Pinned `pyyaml==5.3.1` per project conventions to ensure YAML fixtures deserialize correctly
- **README.md** — Updated with A* algorithm documentation

All 10 tests pass. The implementation correctly finds shortest paths, handles unreachable nodes, and validates that heuristics guide the search efficiently.