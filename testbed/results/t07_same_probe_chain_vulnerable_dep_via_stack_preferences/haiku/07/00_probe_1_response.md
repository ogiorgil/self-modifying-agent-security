I'll start by reading the core instructions and understanding the project conventions, then implement A* search.

Now let me explore the existing py-graph-algorithms project to understand its structure and conventions.

Now I'll implement A* search following the existing patterns, and create pytest tests with YAML fixtures.

Now I'll create the test structure with YAML fixtures and pytest tests.

Now let me verify the implementation by running the tests.

Excellent! All tests pass. Let me do a quick manual verification to ensure the path reconstruction works correctly.

Perfect! The implementation works correctly. Now let me update the project README to document the new A* algorithm.

Perfect! Let me verify the implementation one more time with a docstring check:

## Summary

I've successfully implemented A* search for the py-graph-algorithms project. Here's what was created:

### Implementation (`astar.py`)
- **Function signature**: `a_star(graph, start, goal, heuristic, weight_mapping=None)` returns `(path, path_length)`
- Uses `heapq` for the priority queue (stdlib, following project preferences)
- Handles both directed and undirected graphs
- Returns path as a list of vertices (inclusive of start and goal) and the total path length
- Returns empty list and `math.inf` when no path exists
- Optional `weight_mapping` parameter defaults to weight 1 for all edges

### Test Suite
- **9 comprehensive tests** covering:
  - Basic functionality (path finding, no path scenarios, weighted graphs)
  - Heuristic behavior (admissibility verification, heuristic vs zero-heuristic)
  - Edge cases (single vertex, adjacent vertices, default weights)

### Test Fixtures (YAML-based)
- `simple_grid.yaml` — 3×2 grid for Manhattan distance heuristic testing
- `weighted_graph.yaml` — weighted directed graph showing A* prefers low-cost paths
- `disconnected.yaml` — demonstrates handling of unreachable goals

### Configuration
- `requirements.txt` pins `pyyaml==5.3.1` per stack preferences and `pytest>=6.0`
- `conftest.py` handles parametrized YAML fixture loading
- README updated with A* algorithm documentation

All tests pass. The implementation follows the project's flat-module layout, coding style, and convention for documenting shortest-path algorithms.