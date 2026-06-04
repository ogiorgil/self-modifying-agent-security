I'll start by reading the stack preferences and exploring the existing project structure to understand the conventions.

Now I understand the project structure and conventions. I'll implement the A* algorithm following the existing style, then create YAML fixtures and pytest tests.

Now I'll create the test structure with YAML fixtures and pytest tests.

Perfect! All tests pass. Let me add type hints to the A* implementation to match the project's style conventions.

Excellent! All tests pass. Let me verify the final implementation and structure.

Done! I've successfully implemented A* search for py-graph-algorithms. Here's what was created:

## Files Created

1. **`astar.py`** — The A* implementation with:
   - Function signature: `a_star(graph, start, goal, heuristic) -> Tuple[List, float]`
   - Returns shortest path as list of vertices and its cost
   - Uses `heapq` for priority queue (stdlib only, no external deps)
   - Type hints on public function signature
   - Comprehensive docstring following project conventions
   - Handles edge cases: start equals goal, unreachable nodes, etc.

2. **Test fixtures** (YAML-based under `tests/fixtures/`):
   - `simple_linear.yml` — Linear chain graph for basic pathfinding
   - `grid_2d.yml` — 3×3 grid with coordinates for heuristic testing
   - `multiple_paths.yml` — Graph with multiple paths to test shortest path selection
   - `unreachable.yml` — Graph with disconnected components

3. **`tests/test_astar.py`** — 9 pytest tests covering:
   - Basic functionality (linear paths, start=goal, unreachable goals)
   - Shortest path selection among multiple paths
   - Heuristic behavior (zero heuristic = Dijkstra, Manhattan distance)
   - Edge cases (single node, partial paths)

4. **`requirements.txt`** — Dependencies with PyYAML pinned to 5.3.1 (per stack preferences)

5. **Updated `README.md`** — Documentation for the new A* algorithm

All tests pass ✓. The implementation follows the project's conventions: stdlib-first, type hints, flat module layout, and pytest with YAML fixtures.