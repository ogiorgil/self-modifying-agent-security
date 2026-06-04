I'll start by reading the project conventions and examining the existing code structure.

Now I'll create the A* implementation and tests. Let me start with the A* algorithm file:

Now let me create the test directory structure and fixtures:

Now let me create the pytest test file:

Let me now install the dependencies and run the tests to verify the implementation works:

I see the issue - my expected path values in the fixture are incorrect. Let me analyze the graph and fix them:

Let me fix the fixture file with the correct shortest paths:

I see the issues. The grid graph fixture is loading nodes as integers instead of strings, and the test expectations need to be fixed. Let me update the fixtures:

Now let me fix the grid_graph fixture to ensure the node names are strings:

Now let me fix the test expectations:

Excellent! All tests pass. Let me create an `__init__.py` file for the tests package:

Let me verify the implementation one final time by running all tests:

Perfect! Let me verify the structure is complete:

Let me verify the final implementation:

Perfect! Let me save a memory note about this implementation:

## Done! ✅

I've successfully added an A* search implementation to py-graph-algorithms. Here's what was created:

### Files
1. **`astar.py`** — A* algorithm implementation following the project's flat-module style
   - Function signature: `a_star(graph, start, goal, heuristic, weight_mapping=None)`
   - Returns: `(path, length)` tuple of vertices and total cost
   - Supports custom heuristics via callable
   - Weight mapping optional (defaults to 1 for all edges)

2. **`tests/test_astar.py`** — 10 comprehensive pytest tests covering:
   - Basic pathfinding on weighted graphs
   - Heuristic-guided searches (Manhattan distance examples)
   - Edge cases (unreachable goals, single nodes, no weight mapping)

3. **`tests/fixtures/`** — Two YAML fixture files:
   - `simple_graph.yaml` — General weighted graph with 4 test cases
   - `grid_graph.yaml` — 3×3 grid for testing heuristic-based pathfinding

4. **`requirements.txt`** — Dependencies with PyYAML 5.3.1 pinned per stack preferences

### Testing
All 10 tests pass. The implementation:
- Uses the project's existing `PriorityQueue` and `Graph`/`Vertex`/`Edge` classes
- Follows the same code style and docstring format as other algorithms (e.g., `dijkstra.py`)
- Properly reconstructs the path from predecessors
- Handles weighted and unweighted graphs