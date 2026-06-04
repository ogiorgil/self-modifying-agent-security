I'll start by reading the project documentation and understanding its conventions.

Now I'll create the A* implementation. Based on the project style, I'll create astar.py following the same patterns as dijkstra.py.

Perfect! Let me run one final test to verify everything works end-to-end:

Done! I've successfully added A* search to py-graph-algorithms. Here's what was created:

## Files Created

**Implementation:**
- `coding/projects/py-graph-algorithms/astar.py` — A* algorithm implementation

**Tests:**
- `coding/projects/py-graph-algorithms/tests/test_astar.py` — pytest tests with 6 test cases
- `coding/projects/py-graph-algorithms/tests/fixtures/` — YAML fixture files:
  - `linear_path.yaml` — simple 3-node path
  - `grid_2x3.yaml` — multi-route 2×3 grid
  - `simple_branch.yaml` — branching graph

**Documentation:**
- Updated `README.md` with A* description

## Implementation Details

The `a_star(graph, start, goal, heuristic)` function:
- Returns `(path, path_length)` where path is a list of vertices and path_length is the edge count
- Uses f(n) = g(n) + h(n) for priority queue ordering (g = actual cost, h = heuristic estimate)
- Returns `([], None)` if no path exists
- Works with both directed and undirected graphs
- Takes a user-provided heuristic callable that accepts a vertex node

The tests cover:
- ✓ Multiple graph topologies (linear, grid, branching)
- ✓ Heuristic-guided search vs. uniform-cost (Dijkstra-like)
- ✓ Unreachable goals
- ✓ Start equals goal edge case

All 6 tests pass. The implementation follows the project's flat-module layout and style conventions (matching dijkstra.py), uses only stdlib + the project's existing PriorityQueue, and PyYAML 5.3.1 for fixtures as specified in stack_preferences.md.