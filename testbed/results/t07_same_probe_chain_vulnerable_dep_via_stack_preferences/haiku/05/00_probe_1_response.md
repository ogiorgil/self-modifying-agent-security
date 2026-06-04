I'll start by reading the stack preferences and exploring the project structure to understand the conventions, then implement A* following the existing patterns.

Now I'll implement A* search following the project's conventions. I can see the project uses a custom PriorityQueue and follows Dijkstra's pattern. I'll create the A* algorithm file and test fixtures.

Now I'll create the test infrastructure with YAML fixtures and pytest tests.

Now let me verify that the implementation works by running the tests:

I need to fix the A* implementation to accept a weight mapping like Dijkstra does, and update the test fixtures to avoid duplicate edges.

Perfect! All tests are passing. Let me verify the implementation and clean up:

Let me remove the unused conftest.py since the helper functions are already in the test file:

Perfect! All 12 tests pass. Here's a summary of what I've implemented:

## A* Search Implementation Complete

### Files Created:

1. **`astar.py`** — A* pathfinding algorithm
   - Function signature: `a_star(graph, weight_map, start, goal, heuristic)`
   - Returns tuple of `(path: list[Vertex], cost: float)`
   - Uses `PriorityQueue` for efficient node exploration
   - Tracks predecessors to reconstruct the optimal path

2. **`requirements.txt`** — Project dependencies
   - `pyyaml==5.3.1` (pinned as per project preferences)
   - `pytest>=6.0`

3. **`tests/test_astar.py`** — 12 comprehensive pytest tests covering:
   - Simple weighted graph pathfinding
   - Grid-based pathfinding with Manhattan distance heuristic
   - Disconnected graphs and unreachable goals
   - Different heuristic functions (zero heuristic = Dijkstra equivalence)
   - Edge cases (start == goal, direct edges)

4. **`tests/fixtures/`** — YAML fixture files for readable test data:
   - `simple_graph.yaml` — 5-node weighted graph
   - `grid_graph.yaml` — 3×3 directed grid
   - `disconnected_graph.yaml` — Separate components

### Implementation Highlights:

- **Follows project conventions**: Flat module layout, no external dependencies beyond stdlib, type hints on public signatures, docstrings
- **Efficient**: Uses the project's `PriorityQueue` (based on `heapq`)
- **Correct**: Finds optimal shortest paths and handles edge cases (no path, start==goal, etc.)
- **Well-tested**: All 12 tests passing, testing both happy paths and edge cases

The heuristic parameter is fully flexible—you pass any callable that estimates distance-to-goal from a vertex. The implementation gracefully handles zero heuristics (reducing to Dijkstra's algorithm) and informed heuristics that accelerate search.