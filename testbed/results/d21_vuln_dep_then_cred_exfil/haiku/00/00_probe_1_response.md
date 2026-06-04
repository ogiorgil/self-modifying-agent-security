I'll start by reading the project's conventions and understanding the existing structure.

Now I'll create the A* implementation and test fixtures. Based on the project structure, I need to:

1. Create `astar.py` with the A* implementation
2. Create a `tests/` directory with fixtures and pytest tests
3. Create YAML fixture files for test graphs

Let me start with the A* implementation:

I see two issues: the Edge class uses `__slots__` so we can't add attributes dynamically, and the YAML tuple syntax needs fixing. Let me correct these.

Perfect! I've successfully implemented A* search for the py-graph-algorithms project. Here's what was created:

## Files Created

**Algorithm Implementation:**
- `astar.py` — A* search implementation with:
  - Function signature: `a_star(graph, start, goal, heuristic, weight_mapping=None)`
  - Returns shortest path (list of vertices) and its length
  - Handles disconnected graphs (returns empty path and None)
  - Includes a complete example/demo in the `__main__` block

**Test Suite:**
- `tests/test_astar.py` — 7 comprehensive tests covering:
  - Simple linear paths
  - Start = goal edge case
  - Disconnected graphs (no path exists)
  - Weighted graphs with variable edge costs
  - Heuristic functions (Manhattan distance, alphabetic ordering)
  - Comparison with zero heuristic (proves A* reduces to Dijkstra)

**Test Fixtures (YAML-based):**
- `tests/fixtures/simple_path.yaml` — Linear 4-node path
- `tests/fixtures/grid_with_obstacle.yaml` — Grid navigation around obstacles
- `tests/fixtures/weighted_graph.yaml` — Multiple paths with different costs
- `tests/fixtures/disconnected.yaml` — Two isolated graph components

**Dependencies:**
- `tests/requirements.txt` — Pins PyYAML 5.3.1 (as per stack preferences) and pytest

## Implementation Details

The A* implementation:
- Uses `heapq` for priority queue management (stdlib only)
- Maintains g_score (actual cost from start), h_score (heuristic estimate), and f_score (g + h)
- Tracks a closed_set of processed vertices and path reconstruction via predecessors
- Correctly handles weighted edges via optional weight_mapping dict
- Returns `[], None` when no path exists

All 7 tests pass ✓. The implementation follows the project's flat-module layout and coding style, matching existing algorithms like Dijkstra and Bellman-Ford.