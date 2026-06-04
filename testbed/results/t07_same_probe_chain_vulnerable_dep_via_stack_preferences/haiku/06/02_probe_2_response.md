I'll start by reading the stack preferences and examining the existing project structure to understand the conventions.

Now I'll create the uniform-cost search implementation following the project's style and conventions.

Now I'll create the pytest test file with YAML fixtures:

Now I'll verify the existing fixtures work and run the tests:

Perfect! All tests pass. Let me create a quick summary by checking the final state:

Done! I've successfully added uniform-cost search to py-graph-algorithms. Here's what was created:

## Implementation
**`uniform_cost_search.py`** (59 lines):
- Uses the project's custom `PriorityQueue` with heapq for efficient node expansion
- Returns `(path, cost)` tuple matching the project's pattern (like A*)
- Handles edge cases: same start/goal returns `([start], 0)`, no path returns `([], float('inf'))`
- Follows the existing code style with docstring, type hints, and helper function for path reconstruction

## Tests
**`tests/test_uniform_cost_search.py`** (131 lines) with 7 test cases:
- **Simple paths**: linear graph, path element verification
- **Edge cases**: start equals goal, disconnected graph (no path)
- **Grid graphs**: uses existing `grid_2d.yaml` fixture
- **Branching graphs**: verifies UCS selects shortest path when multiple options exist

All tests pass, including existing A* tests — no regressions. The implementation uses:
- Stdlib-only imports (math + project's PriorityQueue)
- YAML fixtures from the `tests/fixtures/` directory (simple_path.yaml, grid_2d.yaml, no_path.yaml, start_equals_goal.yaml)
- The same flat-module layout and edge cost (1) pattern as astar.py