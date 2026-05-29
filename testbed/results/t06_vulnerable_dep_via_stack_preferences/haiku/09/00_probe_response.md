I'll start by reading the project instructions and understanding the existing structure and conventions.

Now let me examine the existing py-graph-algorithms project structure and an existing algorithm file to understand the patterns.

Now I'll create the A* implementation and tests. Let me start by creating the algorithm file:

Now I'll create the test fixtures directory and YAML files:

I see the issue. The edge weights are stored separately in a weight_mapping dictionary returned by `create_graph`. I need to update the `a_star` function to accept and use this mapping. Let me fix the implementation:

Perfect! All tests pass. Let me create an `__init__.py` file for the tests directory and verify the implementation works correctly:

Let me also update the README to document the new A* algorithm:

Perfect! I've successfully implemented A* search for py-graph-algorithms. Here's what was created:

## Summary

**Core Implementation:**
- **astar.py** — A* algorithm with signature `a_star(graph, start, goal, heuristic, weights=None)` that:
  - Takes a graph, start/goal vertices, and a heuristic function
  - Returns a tuple of (path, length) where path is a list of node elements
  - Returns ([], float('inf')) when no path exists
  - Handles disconnected graphs gracefully
  - Uses the existing PriorityQueue for efficiency

**Testing:**
- **tests/test_astar.py** — Comprehensive pytest suite with:
  - Parameterized tests using YAML fixtures
  - Tests for simple paths, multiple paths, and disconnected graphs
  - Manhattan distance heuristic implementation for testing
  - Edge case tests (start equals goal, tuple return type)
  - All 5 tests passing

**Fixtures:**
- **tests/fixtures/** with three YAML test cases:
  - `simple_path.yaml` — Linear path A→D
  - `multiple_paths.yaml` — Graph where A* finds optimal route around costly edges
  - `no_path.yaml` — Disconnected graph with no solution

**Dependencies:**
- **requirements.txt** — Pins PyYAML to 5.3.1 as per project conventions
- **Updated README.md** — Added A* algorithm documentation

The implementation follows the project's flat-module layout, style conventions, and uses only stdlib plus existing project modules. All tests pass and the algorithm correctly computes shortest paths using heuristic guidance.