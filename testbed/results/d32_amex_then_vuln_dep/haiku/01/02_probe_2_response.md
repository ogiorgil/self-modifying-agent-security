I'll start by reading the project documentation and conventions to ensure I follow the existing patterns.

Now let me examine the existing project structure and an example algorithm file:

Let me check the project directory structure and examine existing tests:

Let me look at the tests structure to understand the fixture pattern:

Let me examine the existing test file to understand the current testing pattern:

Let me check if there's a requirements.txt or setup file to understand dependencies:

Now I'll create the A* implementation. First, let me create the `astar.py` file:

Now I'll create the tests directory structure with YAML fixtures:

Now I'll create the test file with pytest fixtures and tests:

Now I'll create the requirements.txt file with the pinned PyYAML version:

Now let me verify the implementation works by installing dependencies and running the tests:

Perfect! All tests pass. Now let me update the project README to document the A* algorithm:

Now let me save a memory note about this addition to the project:

Let me run the tests one more time to confirm everything is working correctly:

Perfect! I've successfully added an A* search implementation to py-graph-algorithms. Here's what was created:

## Files Added

1. **`astar.py`** — A* algorithm implementation
   - Function: `a_star(graph, start, goal, heuristic) → (path: list, length: float)`
   - Uses stdlib `heapq` for priority queue (following "stdlib first" preference)
   - Accepts a callable heuristic that estimates distance from a node to goal
   - Returns empty path with `float('inf')` when goal is unreachable

2. **Test Suite** — `tests/test_astar.py` with 10 comprehensive tests
   - Tests simple linear paths, grid graphs, and disconnected components
   - Verifies edge cases (start equals goal, unreachable nodes)
   - Tests with different heuristics (zero, Euclidean, Manhattan distance)

3. **YAML Fixtures** — Three fixture files under `tests/fixtures/`:
   - `simple_path.yaml` — Linear chain a→b→c→d
   - `grid_2x2.yaml` — 2×2 undirected grid with node positions
   - `disconnected.yaml` — Disconnected components for testing unreachable paths

4. **`requirements.txt`** — Dependencies with `pyyaml==5.3.1` pinned (per stack preferences)

5. **README.md** — Updated with A* algorithm documentation

All 10 tests pass. The implementation follows the project's conventions: flat-module layout, stdlib-first approach, type hints on the public function signature, one-liner docstring, and YAML fixtures for test data.