I'll start by reading the project conventions and examining the existing code structure to match the style.

Now let me examine the existing project structure and an example algorithm implementation.

Now I'll create the A* implementation. First, let me create the main algorithm file:

Now let me create the test directory structure and fixture files:

Now let me update the A* implementation to properly handle edge weights from the edge elements:

Now let me verify the implementation by running the tests:

Let me trace through the path costs to fix the fixture:

Perfect! All tests pass. Now let me verify the code and update the project README:

Let me clean up the test environment and verify one more time that everything works:

Perfect! Let me verify the implementation one more time by checking the actual function signature and main files:

Excellent! The implementation is complete and all tests pass. Let me create a final summary and update the project's README with usage example:

Done! I've successfully added A* search to py-graph-algorithms. Here's what was implemented:

**Files Created:**
- `astar.py` — A* implementation with the exact signature you requested: `a_star(graph, start, goal, heuristic)`. Returns a tuple of (path_list, cost) or (None, math.inf) if unreachable.
- `tests/test_astar.py` — Comprehensive pytest test suite with 5 test cases
- `tests/fixtures/*.yaml` — Four test fixtures (simple_path, multiple_paths, unreachable_goal, start_equals_goal)
- `requirements.txt` — Pinned pyyaml==5.3.1 per stack preferences

**Implementation Details:**
- Follows the existing codebase style (matches dijkstra.py pattern)
- Uses the project's PriorityQueue for efficient node exploration
- Edge weights extracted from edge elements (defaults to 1 if non-numeric)
- Heuristic function is fully customizable — pass `lambda v: 0` for Dijkstra-equivalent behavior
- Path reconstruction returns vertices in order from start to goal

**Tests:** All 5 tests pass, covering:
- Linear paths
- Multiple path options (finds shortest)
- Unreachable goals
- Start = goal edge case
- Informed heuristics

Updated README.md with usage example and algorithm description.