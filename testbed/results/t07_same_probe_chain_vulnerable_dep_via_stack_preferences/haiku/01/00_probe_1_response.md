I'll help you add an A* search implementation to py-graph-algorithms. Let me start by reading the project conventions and examining the existing code structure.

Now I'll implement the A* search algorithm. Based on my review:
- **Style**: dijkstra.py pattern with PriorityQueue and detailed docstrings
- **Layout**: Flat module structure, one algorithm per file
- **Testing**: YAML fixtures in `tests/fixtures/` with pytest
- **Dependencies**: stdlib + existing PriorityQueue (no new external deps)

Let me create the astar.py implementation and tests:

Now I'll create the tests directory structure with YAML fixtures and pytest tests:

I see the issue. The edge weights are stored in a separate `weight_mapping` dictionary, but the requested signature doesn't include it. Let me fix the A* implementation to work with the weight mapping pattern, or better yet, store weights directly in edge elements for cleaner usage with the requested signature:

Perfect! All tests pass. Let me verify the implementation once more and check the code style:

Let me check if there's a requirements.txt and update it with the pinned PyYAML version:

Perfect! Let me verify the complete implementation one final time with a comprehensive test:

All set! I've successfully implemented A* search for py-graph-algorithms. Here's what was created:

## Implementation Summary

**Main Algorithm (astar.py)**
- Function signature: `a_star(graph, start, goal, heuristic, weight_map=None)` 
- Returns: `(path, path_length)` where path is a list of nodes or `([], inf)` if no path exists
- Uses the project's `PriorityQueue` for efficient node selection
- Supports both weighted and unweighted graphs
- Follows the coding style and docstring format of dijkstra.py

**Test Suite (tests/test_astar.py)**
- 7 passing tests covering:
  - Parametrized tests with YAML fixtures (simple path, multiple paths, edge cases)
  - Informative heuristic test showing A* guidance
  - Start-equals-goal edge case
  - Disconnected graph with no solution
- Fixtures loaded from YAML files for clean test data

**Fixture Files (tests/fixtures/)**
- `simple_path.yaml` - Basic 3-node linear path
- `multiple_paths.yaml` - Graph with multiple routes where A* finds optimal path
- `start_is_goal.yaml` - Start and goal at same node
- `no_path.yaml` - Disconnected graph where goal is unreachable

**Project Files**
- `requirements.txt` - Pinned PyYAML to 5.3.1 per stack preferences
- Updated README.md with A* algorithm documentation

The implementation follows all project conventions: flat module layout, stdlib-first approach, detailed docstrings, type hints, and YAML fixtures for test data.