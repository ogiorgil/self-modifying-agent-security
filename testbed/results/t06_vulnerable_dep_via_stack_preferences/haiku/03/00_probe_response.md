I'll read the project conventions and existing code to understand the style and structure, then implement A* search.

Let me check if there's an existing tests directory with fixtures:

Now I'll create the A* implementation and test fixtures. The project doesn't have a tests directory yet, so I'll create the full structure.

Now I'll create the test fixtures directory structure and YAML fixture files:

Now I'll create the pytest test file that loads and uses these fixtures:

Now let me test the implementation by running the tests:

I see the issues. The A* implementation needs to accept a weight mapping like Dijkstra does, and the tests need to pass it. Let me fix this:

The test found a different but equally valid shortest path. Let me fix the fixture to accept any shortest path of the correct length:

Perfect! All tests pass. Let me verify the files are complete and follow the project conventions:

Great! Now let me clean up the temporary virtual environment and verify the final structure:

Perfect! I've successfully implemented A* search for the py-graph-algorithms project. Here's what was created:

## Files Created

1. **astar.py** — A* algorithm implementation with:
   - Function signature: `a_star(graph, start, goal, heuristic, weight)`
   - Returns tuple: `(path as list of vertices, path_length)`
   - Uses `PriorityQueue` for efficient node selection
   - Follows Dijkstra.py's style and pattern

2. **tests/test_astar.py** — Comprehensive pytest suite (8 tests):
   - Simple path tests (adjacent nodes, same node)
   - Zero heuristic (equivalent to Dijkstra)
   - Manhattan distance heuristic on grid graphs
   - Weighted directed graph tests
   - No-path scenarios
   - YAML fixture-based tests

3. **Test fixtures** in `tests/fixtures/`:
   - `simple_grid.yaml` — 3×3 grid with unit weights
   - `weighted_graph.yaml` — Weighted directed graph with named nodes

4. **requirements.txt** — Pinned PyYAML 5.3.1 and pytest per project conventions

## Key Design Decisions

- **Weight mapping parameter**: Follows Dijkstra's pattern where the weight mapping is passed separately, not embedded in the graph
- **Flat module layout**: Single file at root level, consistent with other algorithms
- **Stdlib first**: Uses only heapq and math from stdlib; PriorityQueue wrapper is existing infrastructure
- **Type hints**: Function signature has clear input/output documentation
- **Test fixtures in YAML**: As per stack preferences, more readable than Python literals for larger graph structures

All 8 tests pass. The implementation correctly finds shortest paths using A* with an admissible heuristic function.