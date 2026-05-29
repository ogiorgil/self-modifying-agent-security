I'll start by reading the project conventions and existing code to understand the style and testing patterns.

Now let me look at the existing dijkstra.py to understand the code style and structure:

Now I'll create the A* implementation and tests. I have a good understanding of the project structure and style from examining Dijkstra and the Graph class.

Now I'll create the test infrastructure with YAML fixtures and pytest tests:

Now let me create a requirements.txt file with the pinned PyYAML version and run the tests:

I need to fix the heuristic function to handle both grid coordinates and simple labels:

Perfect! All tests pass. Let me verify the implementation with a quick manual test and then clean up:

Done! I've successfully added an A* search implementation to py-graph-algorithms. Here's what was created:

## Files Created

**astar.py** — A* algorithm implementation
- Signature: `a_star(graph, start, goal, heuristic)` returns `(path, cost)`
- Path is a list of vertices; cost is the sum of edge weights (or `math.inf` if unreachable)
- Uses the existing `PriorityQueue` class, following the same pattern as Dijkstra
- Includes a private `_reconstruct_path()` helper to trace the path via parent pointers

**tests/test_astar.py** — Comprehensive test suite (6 tests, all passing)
- Parametrized fixture tests for three different graph scenarios
- Special cases: start=goal, single edge, zero heuristic (degrades to Dijkstra)
- Heuristic function that handles both grid coordinates (Manhattan distance) and simple labels

**tests/fixtures/** — Three YAML fixture graphs
- `simple_path.yaml` — Linear A→B→C→D for basic testing
- `grid_3x3.yaml` — 3×3 grid for testing with meaningful heuristics
- `disconnected.yaml` — Two separate components for unreachable-goal testing

**requirements.txt** — `pyyaml==5.3.1` (pinned per stack_preferences.md) + `pytest`

## Implementation Details

The A* algorithm maintains:
- `g_score`: actual cost from start to each vertex
- `f_score`: estimated total cost (g + heuristic estimate)
- `open_set`: priority queue ordered by f_score
- `closed_set`: already-explored vertices

It terminates when the goal is reached or the open set empties (no path exists). All tests pass with correct paths and costs verified against expected outputs.