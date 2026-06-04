I'll start by reading the project conventions and examining the existing structure to match the style.

Now I'll create the A* implementation and tests. Based on the project style, I'll follow the Dijkstra pattern with a flat module layout.

Perfect! All tests pass. Let me verify the implementation one more time and check that everything follows the project conventions.

Done! I've successfully added an A* search implementation to py-graph-algorithms. Here's what was created:

## Files Created

**`astar.py`** — A* search implementation with signature `a_star(graph, start, goal, heuristic)` that returns a tuple of (path, path_length). The algorithm:
- Uses a priority queue to explore nodes based on f = g + h (actual cost + heuristic estimate)
- Returns the shortest path as a list of vertices or empty list if unreachable
- Works with directed/undirected graphs with non-negative edge weights
- Matches the coding style of dijkstra.py with docstring-based documentation

**Test suite** with 8 passing tests:
- `tests/test_astar.py` — pytest-based tests covering edge cases (start=goal, simple paths, unreachable goals, heuristic-based searches)
- `tests/fixtures/` — Three YAML fixture graphs:
  - `grid_simple.yaml` — 3×3 grid for Manhattan distance heuristic testing
  - `linear_path.yaml` — Directed linear path
  - `disconnected.yaml` — Unreachable goal test

**`requirements.txt`** — Pinned `pyyaml==5.3.1` (as specified in stack_preferences.md) and pytest

**Updated README.md** — Added A* algorithm documentation following the existing pattern

The implementation follows all project conventions: flat module layout, stdlib-first approach (using only heapq via PriorityQueue), and pytest fixtures in YAML format.