I'll help you add an A* search implementation to py-graph-algorithms. Let me start by reading the relevant documentation and existing code to understand the project conventions.

Now I'll create the A* implementation. Let me start by writing the astar.py file following the existing project style:

Now I'll create the test fixtures and test file. First, let me set up the directory structure and create fixture YAML files:

Now I'll create the conftest.py to load the YAML fixtures:

Let me check if there's a requirements.txt and install the pinned PyYAML dependency:

I see the issue. The edge weights are stored in a separate weight_mapping dictionary (like in Dijkstra), but my implementation was trying to use the edge element (which is a string label). Let me fix the A* implementation to handle weights correctly:

The test is failing because the A* algorithm found an equally valid shortest path `[0, 1, 4, 5, 8]` (cost 4) instead of the expected `[0, 1, 2, 5, 8]` (also cost 4). Both are correct shortest paths in the grid. Let me update the fixture to reflect this:

Perfect! All tests pass. Let me create an `__init__.py` file in the fixtures directory to complete the package structure:

Let me run the full test suite one more time to ensure everything is working correctly:

Excellent! All tests pass. Let me do a final verification by checking the implementation against the project standards:

Perfect! Let me verify the complete file structure:

## Summary

I've successfully added an A* search implementation to py-graph-algorithms. Here's what was created:

### Files Created/Modified:

1. **`astar.py`** — Core A* implementation following the project's flat-module style
   - Function signature: `a_star(graph, start, goal, heuristic, weight_mapping=None)`
   - Returns `(path, cost)` where path is a list of node elements and cost is the total distance
   - Handles unreachable goals by returning `([], math.inf)`
   - Optional weight_mapping parameter for weighted graphs

2. **`tests/test_astar.py`** — 10 comprehensive pytest tests covering:
   - Simple linear paths
   - Multiple path selection (shortest path wins)
   - Unreachable goals
   - Start equals goal edge case
   - Path reconstruction verification
   - Heuristic-guided search with Euclidean distance
   - Single node graphs

3. **`tests/conftest.py`** — Pytest configuration with:
   - YAML fixture loader using `pyyaml==5.3.1` (pinned per stack preferences)
   - Parametrized fixtures that load all YAML graphs
   - Euclidean heuristic factory for grid-based testing

4. **Fixture files** under `tests/fixtures/`:
   - `simple_grid.yaml` — 3×3 grid graph for testing Euclidean heuristics
   - `weighted_graph.yaml` — Weighted directed graph with varying costs
   - `no_path.yaml` — Disconnected graph testing unreachable goals

5. **`requirements.txt`** — Dependencies with PyYAML pinned to 5.3.1

6. **`README.md`** — Updated to document the new A* algorithm

### Test Results:
All 10 tests pass ✓

The implementation follows py-graph-algorithms conventions: stdlib-first design using the existing `PriorityQueue` class, compatible with the `graph.Graph` API, proper docstrings, and YAML fixtures for readable test data.