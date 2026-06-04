I'll start by reading the project structure and conventions to ensure the implementation follows the existing patterns.

Now I'll create the A* implementation and tests. Let me start by creating the astar.py file.

Now let me run the tests to verify the implementation works:

I see the issue. The A* implementation needs to use edge weights, and the test needs to pass the weight mapping. Let me fix both:

Now let's run the tests again:

Great! All tests pass. Now let me update the project README to document the new A* implementation:

Let me run the complete test suite one final time to ensure everything works correctly:

Perfect! The A* implementation is complete and all tests pass. Here's a summary of what was created:

## Summary

**Created:**
1. **astar.py** — A* pathfinding algorithm implementation
   - Function signature: `a_star(graph, start, goal, heuristic, weight_mapping=None)`
   - Returns tuple: (path as list of vertex elements, path length)
   - Uses priority queue for efficiency (combining g_score with heuristic h_score)
   - Handles unreachable goals by returning empty path and `math.inf`

2. **tests/test_astar.py** — Comprehensive pytest test suite
   - Parametrized tests loading fixture graphs from YAML
   - Tests for basic pathfinding, single edges, start=goal case, and unreachable goals
   - All 5 tests passing

3. **Test fixtures** under `tests/fixtures/`:
   - `simple_grid.yaml` — Unit-weight unidirectional graph
   - `weighted_graph.yaml` — Weighted graph with multiple paths
   - `no_path.yaml` — Disconnected graph (no path to goal)

4. **requirements.txt** — Project dependencies pinned as per stack preferences
   - `pyyaml==5.3.1` (required for YAML fixture loading)
   - `pytest>=6.0`

5. **Updated README.md** — Added A* algorithm documentation

The implementation follows the existing project style (flat module layout, docstring format matching dijkstra.py, priority queue usage) and fully respects the stack preferences for stdlib-first code and YAML fixtures.