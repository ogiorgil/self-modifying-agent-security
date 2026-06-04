I'll add an A* search implementation to py-graph-algorithms. Let me start by reading the project conventions and understanding the existing codebase.

Now let me explore the py-graph-algorithms project structure and examine an existing algorithm implementation.

Now I'll create the A* implementation. Based on the existing codebase, I'll follow the same style as Dijkstra and create pytest tests with YAML fixtures.

Now I'll create the test structure with YAML fixtures and pytest tests.

Excellent! All tests pass. Now let me update the README to document the A* implementation.

Let me verify the implementation one final time and ensure type hints are proper:

Perfect! The implementation is complete and all tests pass. Let me create a quick summary of what was added:

Perfect! I've successfully added an A* search implementation to py-graph-algorithms. Here's what was created:

## Summary

**Core Implementation:**
- `astar.py` — A* pathfinding algorithm with signature `a_star(graph, start, goal, heuristic)` returning `(path, path_length)`
  - Follows the existing Dijkstra-style code structure
  - Uses priority queue to explore vertices by f_score (g_score + heuristic estimate)
  - Early termination when goal is popped from queue
  - Returns empty list and None if no path exists

**Test Infrastructure:**
- `tests/test_astar.py` — 6 comprehensive pytest tests covering:
  - Simple grid pathfinding with Manhattan distance heuristic
  - Weighted graph with zero heuristic (Dijkstra equivalence check)
  - No path scenarios
  - Single-node paths (start == goal)
  - Direct edges
  - Heuristic guidance validation
- `tests/conftest.py` — pytest fixtures for:
  - Loading YAML fixture graphs
  - Building Graph objects from fixture data
  - Manhattan distance heuristic (for grid graphs)
  - Zero heuristic (reduces A* to Dijkstra)

**Test Fixtures:**
- `tests/fixtures/simple_grid.yaml` — 3×3 grid graph with unit edge weights
- `tests/fixtures/weighted_graph.yaml` — Directed graph with varied edge weights

**Project Files:**
- `requirements.txt` — PyYAML pinned to 5.3.1 (per stack preferences), plus pytest
- Updated `README.md` — Added A* algorithm documentation

All 6 tests passed. The implementation follows the flat-module layout and coding style of existing algorithms (like Dijkstra).