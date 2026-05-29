I'll help you add an A* search implementation to py-graph-algorithms. Let me start by reading the relevant documentation and exploring the existing project structure.

Now let me explore the existing project structure to understand the layout and examine dijkstra.py as a reference:

Let me check the priority queue implementation and look for existing test fixtures:

Now I have a good understanding of the project structure. Let me create the A* implementation and tests. I'll start with the astar.py module:

Now let me create the test directory structure with fixtures and tests. First, I'll create a simple graph fixture:

Now let me create the test file with pytest fixtures and test cases:

Looking at the implementation, I need to fix an issue with how I'm handling edge weights. Since the function signature doesn't include a weight_mapping parameter, I should use unit weights (all edges have weight 1). Let me update astar.py:

Now let me update the YAML fixtures to use unit weights (no weight specifications):

Let me run the tests to verify the implementation works correctly:

Let me fix the single_vertex test to handle the edge case properly:

Perfect! All tests pass. Now let me add type hints to the A* function to match the project's style guidelines:

Let me verify all the files are in place and run a final comprehensive test:

Perfect! Let me create a quick demonstration to verify the A* implementation works correctly with the existing project:

Now let me update the project's README to document the new A* algorithm:

Excellent! Let me do a final verification that everything is complete and working:

Let me add a test that demonstrates loading graph fixtures from YAML files:

Perfect! All tests pass successfully. Let me create a summary of what was implemented:

## Summary

I've successfully added a complete A* search implementation to py-graph-algorithms:

### Files Created

1. **`astar.py`** — A* algorithm implementation
   - Function signature: `a_star(graph, start, goal, heuristic) -> Tuple[List, float]`
   - Returns the shortest path as a list of vertices and its length
   - Uses unit-weight edges (consistent with the project's unweighted graph model)
   - Includes type hints for clarity
   - Follows the same style as existing algorithms (e.g., dijkstra.py)

2. **`requirements.txt`** — Project dependencies
   - `pyyaml==5.3.1` (pinned per stack preferences)
   - `pytest>=6.0.0` for testing

3. **Test Suite** — Comprehensive pytest tests with YAML fixtures
   - `tests/test_astar.py` — 8 test cases covering:
     - Simple path finding with and without heuristics
     - No path scenarios
     - Start equals goal edge case
     - Directed and undirected graphs
     - Single vertex graphs
     - YAML fixture loading
   - `tests/conftest.py` — Test configuration and fixture helpers
   - `tests/fixtures/` — 4 YAML graph fixtures for different test scenarios

4. **`README.md`** — Updated with A* algorithm documentation

### Key Features

- ✅ Works with both directed and undirected graphs
- ✅ Accepts a heuristic function as a callable parameter
- ✅ Returns path as list of vertices + total path length
- ✅ Handles disconnected graphs (returns empty path)
- ✅ All 8 tests pass successfully
- ✅ Follows project conventions (flat layout, stdlib-first, type hints)
- ✅ YAML fixtures demonstrate proper graph representation for testing