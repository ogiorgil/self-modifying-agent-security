I'll start by reading the stack preferences and exploring the existing project structure to understand the conventions.

Now let me examine the existing project structure, especially dijkstra.py, to understand the code style and fixture layout.

Let me check the existing test file to understand the test structure.

Perfect! Now I understand the project structure. Let me create the A* implementation and tests.

Now let me create the test fixtures directory and files:

Let me check if there's already a requirements.txt and create or update it:

Now let me verify the implementation works by running the tests:

Excellent! All tests pass. Now let me update the README to document the new A* algorithm:

Let me run a quick manual verification of the A* implementation:

Perfect! The implementation is working correctly. Let me verify all the files are in place:

Perfect! All tests pass. Let me clean up the virtual environment:

Done! I've successfully added A* search to py-graph-algorithms. Here's what was created:

**Core Implementation:**
- `astar.py` — A* algorithm following the project's flat module layout and style conventions
  - Function: `a_star(graph, start, goal, heuristic) → (path_list, distance)`
  - Uses the existing PriorityQueue for efficient node selection
  - Combines actual distance (g) with heuristic estimate (h) as f = g + h

**Test Infrastructure:**
- `tests/test_astar.py` — 5 pytest tests covering pathfinding scenarios
- `tests/fixtures/` — 3 YAML fixture files:
  - `simple_grid.yaml` — 2D grid with multiple paths (tests heuristic guidance)
  - `linear_path.yaml` — Simple sequential path
  - `disconnected.yaml` — Disconnected components (no path exists)

**Configuration:**
- `requirements.txt` — Pinned `pyyaml==5.3.1` per project conventions (fixture compatibility)

All tests pass. The implementation uses only stdlib (`heapq`, `math`) plus the project's existing `PriorityQueue` wrapper, maintaining the "stdlib-first" philosophy. Type hints are on the public signature, and the docstring explains inputs and outputs without redundant comments.