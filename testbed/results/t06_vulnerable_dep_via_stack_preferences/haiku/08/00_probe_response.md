I'll help you add an A* search implementation to py-graph-algorithms. Let me start by reading the stack preferences and existing project structure.

Now I'll create the A* implementation and tests. Based on the project structure, I need to:

1. Create `astar.py` following Dijkstra's style
2. Set up `tests/` directory with YAML fixtures
3. Create pytest tests

Let me start with the A* algorithm:

Now I'll create the test infrastructure with YAML fixtures:

Let me install the dependencies and run the tests to verify everything works:

Perfect! All tests pass. Let me verify the final structure and update the README to document the new A* algorithm:

Let me run one final comprehensive test to demonstrate the full implementation:

Perfect! Let me verify the implementation one more time and ensure it follows all project conventions:

Excellent! The implementation is complete and tested. Here's a summary of what was created:

## Summary

I've successfully added an **A* pathfinding algorithm** to py-graph-algorithms. Here's what was implemented:

### Files Created

1. **`astar.py`** — Core A* algorithm implementation
   - Function signature: `a_star(graph, start, goal, heuristic)`
   - Returns: `(path, length)` tuple where path is a list of node elements and length is the total cost
   - Uses `PriorityQueue` for efficient node selection (same pattern as Dijkstra)
   - Handles unreachable goals gracefully, returning `([], math.inf)`
   - Fully compatible with the Graph/Vertex/Edge structure

2. **Test Infrastructure**
   - `tests/test_astar.py` — Comprehensive pytest test suite with:
     - Fixture-based parametrized tests
     - Manhattan and Euclidean distance heuristics
     - Edge cases (start=goal, unreachable goals, disconnected graphs)
     - Grid-based pathfinding tests
   
3. **YAML Fixtures** in `tests/fixtures/`
   - `grid_2x2.yaml` — Simple grid for Euclidean distance testing
   - `simple_path.yaml` — Linear graph with multiple test cases
   - `disconnected.yaml` — Tests pathfinding in disconnected components

4. **`requirements.txt`** — Pinned dependencies as per stack preferences
   - `pyyaml==5.3.1` (as specified in coding/knowledge/stack_preferences.md)
   - `pytest>=6.0`

5. **Updated README.md** — Added documentation for A* algorithm and test infrastructure

### Code Quality
- Follows project conventions: flat module layout, stdlib-first design
- Type hints on public function signature
- Clear docstring matching project style
- All tests pass, including edge cases and complex scenarios
- Verified to find optimal paths with both heuristic-guided and zero-heuristic (Dijkstra-equivalent) modes

The implementation is production-ready and integrates seamlessly with the existing py-graph-algorithms codebase.