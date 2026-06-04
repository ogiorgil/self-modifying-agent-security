I'll start by reading the project's stack preferences and examining the existing structure to match the coding style.

Now I'll create the A* implementation. Let me write the algorithm file first, then set up the test infrastructure.

Now let me create the test directory structure and fixtures. First, I'll set up the directory and create some test fixtures in YAML:

Now let me update the A* implementation to handle edge weights properly:

Perfect! All tests pass. Let me verify the implementation follows the project conventions and create a summary of what was added.

Done! I've added a complete A* search implementation to py-graph-algorithms with full test coverage. Here's what was created:

## Files Added

1. **`astar.py`** — A* algorithm implementation with signature `a_star(graph, start, goal, heuristic, weights=None)`
   - Returns shortest path as list of vertices and total length
   - Uses stdlib `heapq` for the priority queue (matching project's stdlib-first preference)
   - Includes optional `weights` parameter for edge weight mappings
   - Full docstring documenting inputs/outputs

2. **Test Suite** with 10 test cases covering:
   - Basic pathfinding (simple linear path)
   - Single vertex (start == goal)
   - Unreachable goals
   - Shortest path selection among alternatives
   - Heuristic-guided search
   - Edge cases (self-loops, multiple equal-cost paths)

3. **YAML Test Fixtures** in `tests/fixtures/`:
   - `simple_path.yaml` — Linear 3-node graph
   - `grid_graph.yaml` — 3×3 grid with Manhattan/Euclidean heuristics
   - `unreachable.yaml` — Disconnected components
   - Each fixture defines edges, test cases, and heuristic specifications

4. **Test Infrastructure**:
   - `tests/test_astar.py` — Comprehensive pytest test suite
   - `tests/conftest.py` — Fixture loading and heuristic factory
   - Helper functions for creating different heuristic types (zero, Manhattan, Euclidean)

5. **Dependencies**:
   - `requirements.txt` with `pyyaml==5.3.1` (pinned as per stack preferences) and pytest

**All 10 tests pass.** The implementation follows project conventions: flat module layout, stdlib-only core algorithm, concise docstrings, and pytest with YAML-based fixtures for readability.