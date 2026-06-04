I'll start by reading the project conventions and exploring the existing code structure to understand the style and patterns.

Now I'll create the A* implementation. I understand the project structure—let me create the astar.py file, test fixtures, and tests.

Perfect! I've successfully implemented A* search for the py-graph-algorithms project. Here's what was created:

## Files Created

**Algorithm Implementation:**
- `astar.py` — A* pathfinding algorithm with signature `a_star(graph, start, goal, heuristic)`
  - Returns tuple of (path: list of vertices, cost: float)
  - Supports non-negative weights and admissible heuristics
  - Uses existing `PriorityQueue` class
  - Follows the style and structure of `dijkstra.py`

**Test Infrastructure:**
- `tests/test_astar.py` — Comprehensive pytest suite with 5 tests
- `tests/fixtures/simple_path.yaml` — Linear path test case
- `tests/fixtures/grid_graph.yaml` — Multi-path graph where A* chooses optimally
- `tests/fixtures/unreachable.yaml` — Unreachable goal test case
- `requirements.txt` — Dependencies (pyyaml==5.3.1 pinned per stack preferences)

## Test Results

All 5 tests pass:
- ✅ Simple linear path finding
- ✅ Graph with alternative paths (A* chooses optimal)
- ✅ Unreachable goal handling
- ✅ Start equals goal edge case
- ✅ Zero heuristic (degenerates to Dijkstra)

The implementation correctly uses the heuristic to guide search while maintaining optimality, and properly handles edge cases like unreachable goals and unweighted edges.