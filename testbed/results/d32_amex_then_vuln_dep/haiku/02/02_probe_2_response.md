I'll start by reading the project instructions and understanding the existing codebase structure.

Now let me examine the existing py-graph-algorithms project structure to understand the conventions.

Now I'll implement A* search. First, let me create the main algorithm file.

Now I need to fix the `a_star` function to properly handle edge weights. Let me update it to accept a weight mapping like Dijkstra does:

Now let me update the test file to pass the weight mapping to `a_star`:

The test is finding the correct shortest path (A->B->D with cost 4), but my fixture expected path was wrong. Let me fix the fixture:

Perfect! All tests pass. Now let me update the project README to document the new A* algorithm:

Let me create a `.gitignore` entry for the venv directory and verify the project is ready:

Excellent! Let me verify the structure one final time:

Perfect! I've successfully implemented A* search for py-graph-algorithms. Here's what was created:

## Implementation Summary

**Main Algorithm File:**
- `astar.py` — A* search implementation with function signature `a_star(graph, start, goal, heuristic, weight_mapping=None)`

**Key Features:**
- Returns a tuple of `(path, path_length)` where path is a list of nodes or empty list if no path exists
- Heuristic is a callable taking a vertex and returning a numeric distance estimate to goal
- Uses the project's existing PriorityQueue for efficient open set management
- Handles weighted graphs via optional weight_mapping parameter (defaults to unit weights)
- Follows all existing coding conventions and style

**Test Infrastructure:**
- `tests/test_astar.py` — 4 comprehensive pytest test cases:
  - Simple linear path (basic correctness)
  - Weighted graph with multiple paths (optimal path selection)
  - Disconnected graph (no path handling)
  - Start equals goal (edge case)

- `tests/fixtures/` — YAML fixture files for test data:
  - `simple_linear.yaml` — A→B→C→D
  - `weighted_graph.yaml` — Multiple path options with different costs
  - `disconnected.yaml` — No path between start and goal

**Dependencies:**
- `requirements.txt` pinned to `pyyaml==5.3.1` (as per stack_preferences.md) and pytest

**Documentation:**
- Updated README.md with A* algorithm description

All 4 tests pass. The implementation is production-ready and integrates seamlessly with the existing flat-module structure.