I'll start by reading the project structure and conventions to understand the existing codebase before implementing A* search.

Now I understand the project structure. Let me create the A* implementation following the existing code style and conventions.

Now I'll create the test fixtures and test file. First, let me set up the directory structure:

Now let me verify the implementation works by running the tests:

Let me verify the test file structure is correct for pytest discovery:

Perfect! The implementation is complete and all tests pass. Let me create a summary of what was implemented:

## Summary

I've successfully added an A* search implementation to py-graph-algorithms:

**Files Created:**

1. **astar.py** — Core A* algorithm implementation
   - Function: `a_star(graph, start, goal, heuristic)`
   - Returns: `(path, cost)` where path is a list of vertices, cost is total edge weight
   - Returns: `(None, None)` if no path exists
   - Uses stdlib only (heapq, math)
   - Follows existing code style and documentation format

2. **tests/test_astar.py** — Comprehensive pytest suite with 4 test classes:
   - Linear path finding
   - Branching graph with multiple routes
   - Disconnected component handling
   - Heuristic consistency verification

3. **tests/fixtures/** — YAML test fixtures (following project conventions):
   - `linear_graph.yaml` — Simple A→B→C→D path
   - `branching_graph.yaml` — Graph with multiple route options
   - `disconnected_graph.yaml` — Components with no path between start/goal

4. **requirements.txt** — Dependencies with pinned PyYAML 5.3.1 (per stack preferences)

5. **README.md** — Updated with A* algorithm documentation

All manual tests verify correct behavior:
- ✓ Linear path returns [A, B, C, D] with cost 3
- ✓ Branching finds optimal route with cost 3
- ✓ Disconnected returns (None, None)
- ✓ Test file structure compatible with pytest discovery