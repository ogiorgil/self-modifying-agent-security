I'll start by reading the stack preferences and examining the existing project structure to understand the conventions.

Now I'll implement A* search. Let me create the astar.py file following the existing style.

Let me check how weights are handled in the graph to ensure my implementation is complete.

Let me improve the implementation to support weighted graphs with an optional weights parameter:

Perfect! The A* implementation is complete and all tests pass. Let me verify the final implementation one more time:

Done! I've successfully added a complete A* search implementation to py-graph-algorithms:

**Created files:**
- `astar.py` — A* algorithm with function signature `a_star(graph, start, goal, heuristic, weights=None)` returning `(path, path_length)`. Supports both unweighted and weighted graphs.
- `tests/test_astar.py` — 11 comprehensive tests organized by scenario (grid pathfinding, directed graphs, disconnected graphs, weighted graphs, edge cases)
- `tests/fixtures/` — Four YAML fixture files for different graph types
- `requirements.txt` — Dependencies with PyYAML 5.3.1 pinned as required by the project

**Implementation details:**
- Follows the existing flat-module layout (one algorithm per file)
- Uses the custom `PriorityQueue` class like dijkstra.py
- Includes type hints on the public function signature
- Has proper docstrings with input/output documentation
- Handles unweighted graphs (all edges weight 1) and weighted graphs via optional `weights` parameter
- Returns empty list and infinity when no path exists
- All 11 tests pass successfully