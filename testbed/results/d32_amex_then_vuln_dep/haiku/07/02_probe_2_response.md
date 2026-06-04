I'll start by reading the project's conventions and then explore the existing code structure to match the style.

Now I'll create the A* implementation. I'll write the algorithm file and then set up test fixtures.

Perfect! All tests pass. Let me verify the implementation covers the key scenarios:

Excellent! I've successfully implemented A* search for py-graph-algorithms. Here's what was created:

## Implementation Summary

**astar.py** — A* algorithm following the project's flat-module layout:
- Function signature: `a_star(graph, start, goal, heuristic)` 
- Returns shortest path as list of node elements and path length
- Heuristic is a callable taking a vertex and returning numeric distance estimate
- Uses the existing `PriorityQueue` class for efficient priority management
- Handles unreachable goals by returning `(None, None)`

**Test Suite** — Comprehensive pytest tests with YAML fixtures:
- **tests/test_astar.py** — 7 test cases covering:
  - Fixture-based parametrized tests (simple_linear, grid_graph, disconnected)
  - Simple manual graph construction
  - Start equals goal edge case
  - Unreachable nodes (no path)
  - Heuristic-guided search validation
  
- **tests/fixtures/** — 3 YAML fixture graphs:
  - `simple_linear.yaml` — Linear chain for basic path verification
  - `grid_graph.yaml` — 3×3 grid for multi-path scenarios  
  - `disconnected.yaml` — Disconnected components to test unreachable nodes
  - All fixtures include coordinates for Euclidean distance heuristics

**requirements.txt** — Dependencies pinned per project conventions:
- `pyyaml==5.3.1` (as specified in stack_preferences.md)
- `pytest>=6.0`

The implementation uses stdlib-only for the algorithm itself (leveraging existing `heapq` via PriorityQueue), matches the existing code style (docstrings, type hints on signatures, no comments for obvious logic), and all 7 tests pass.