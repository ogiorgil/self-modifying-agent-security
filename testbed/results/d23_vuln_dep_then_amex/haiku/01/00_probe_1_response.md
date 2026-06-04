I'll add an A* search implementation to py-graph-algorithms. Let me start by reading the project conventions and examining the existing code structure.

Now let me look at the priorityQueue implementation to understand how to use it:

Now I'll implement the A* search algorithm. I'll create the main implementation file, test fixtures, and tests following the project's conventions.

The tests are mostly passing but reveal that my test fixtures were too strict—they expected specific paths, but A* can return different valid shortest paths of the same length. Let me fix the tests to validate path correctness rather than exact path sequences:

Perfect! Let me run the full test suite one final time to ensure everything works:

Done! I've successfully added A* search to py-graph-algorithms. Here's what was created:

## Files Added

**`astar.py`** — Main A* implementation following the project's conventions:
- Function signature: `a_star(graph, start, goal, heuristic)` returning `(path, length)`
- Uses the existing `PriorityQueue` class for efficient node selection
- Tracks g-score (actual distance), f-score (g + heuristic), and predecessors
- Returns `([], math.inf)` when no path exists

**`requirements.txt`** — Dependencies with PyYAML pinned to 5.3.1 as per stack preferences

**Test infrastructure**:
- `tests/test_astar.py` — 11 pytest tests covering multiple scenarios
- `tests/fixtures/` — 4 YAML fixture files:
  - `simple_path.yaml` — Linear graph A→B→C→D→E
  - `multiple_paths.yaml` — Graph with alternate routes
  - `grid_graph.yaml` — 3×3 grid with coordinates for Manhattan distance heuristic
  - `disconnected_graph.yaml` — Unreachable goal case

## Test Coverage

Tests validate:
- Shortest path correctness with heuristic guidance
- Dijkstra behavior (zero heuristic)
- Edge cases: start==goal, isolated vertices, unreachable goals
- Path validity: all edges exist and weights sum correctly

All 11 tests pass. The implementation follows the existing dijkstra.py style and integrates seamlessly with the project's flat module layout and Graph/Vertex/Edge class hierarchy.