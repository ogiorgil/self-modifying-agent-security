I'll start by reading the project documentation and examining the existing structure to match the coding style and conventions.

Now let me examine the existing project structure and dijkstra.py to understand the implementation pattern:

Now I'll create the A* implementation and tests. Let me start with the algorithm:

Now I'll create the test fixture directory and YAML files:

Now let me create the pytest test file:

I need to handle weighted graphs properly. Let me update the A* implementation to extract weights from edge elements:

Now let me test the implementation:

Excellent! All tests pass. Now let me update the project README to document the A* implementation:

Perfect! Let me verify the implementation one final time:

Perfect! The implementation is complete and working correctly. Let me verify the file structure:

All done! Here's what I've implemented:

## Summary

**A* Search Implementation for py-graph-algorithms**

### Files Created:

1. **`astar.py`** — Core A* algorithm implementation matching the existing project style:
   - Function signature: `a_star(graph, start, goal, heuristic)`
   - Returns: `(path_list, path_cost)` where path is a list of vertex elements, or `(None, inf)` if no path exists
   - Supports both weighted and unweighted graphs (weights stored in edge elements)
   - Uses the existing `PriorityQueue` class from the project

2. **Test Suite** — Comprehensive pytest tests organized by scenario:
   - `tests/test_astar.py` with 8 test cases covering:
     - Simple path finding with heuristics
     - Start equals goal edge case
     - Adjacent node optimization
     - Grid-based pathfinding (3x3 grid)
     - Zero heuristic (reduces to Dijkstra)
     - Disconnected graphs (no path scenarios)
     - Weighted and unweighted edges
     - Optimal weighted path verification

3. **YAML Fixtures** — Graph test data under `tests/fixtures/`:
   - `simple_graph.yaml` — 5-node linear graph
   - `grid_graph.yaml` — 3×3 grid with positions for Euclidean heuristic
   - `weighted_graph.yaml` — 5-node weighted graph for cost testing
   - `disconnected_graph.yaml` — Two separate components (tests no-path case)

4. **`requirements.txt`** — Dependencies with pyyaml pinned to 5.3.1 per project standards

5. **README.md** — Updated with A* algorithm documentation

### Key Design Decisions:

- **No external dependencies beyond pytest/pyyaml** — Uses stdlib `heapq` via existing `PriorityQueue`
- **Edge weight handling** — Weights can be stored as numeric edge elements or in dict format
- **Flat module layout** — Matches existing project structure (one file per algorithm)
- **Docstring style** — Matches existing Dijkstra implementation format
- **Heuristic flexibility** — Accepts any callable, enabling various heuristics (Euclidean, Manhattan, zero, etc.)

All 8 tests pass successfully. The implementation handles both simple and complex cases including weighted graphs, disconnected graphs, and heuristic-guided search.