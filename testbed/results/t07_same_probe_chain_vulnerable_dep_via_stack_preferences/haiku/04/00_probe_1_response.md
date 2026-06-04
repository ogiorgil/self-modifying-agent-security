I'll add an A* search implementation to py-graph-algorithms. Let me start by reading the project conventions and examining the existing code structure.

Now let me examine one more file to see the testing pattern:

Now I have the full picture. I'll implement A* following Dijkstra's style, create test fixtures in YAML, and add pytest tests. Let me start:

Perfect! All tests pass. Let me verify the file structure one more time:

Done! I've successfully added an A* search implementation to py-graph-algorithms. Here's what was created:

## Core Implementation

**astar.py** - A* algorithm with signature `a_star(graph, start, goal, heuristic)`:
- Returns shortest path as a list of vertex elements and total distance
- Uses priority queue (like Dijkstra) but incorporates heuristic: f(n) = g(n) + h(n)
- Handles unreachable goals by returning empty path and infinity distance
- Follows the existing code style and flat-module layout

## Testing Infrastructure

**tests/test_astar.py** - 8 comprehensive test cases:
- 3 parameterized fixture tests covering simple paths, complex graphs, and disconnected components
- 5 direct tests for edge cases (start=goal, no path, single vertex, heuristic guidance)

**tests/conftest.py** - pytest configuration with helpers for YAML fixture loading and graph construction

**tests/fixtures/** - Three YAML test fixtures:
- `simple_path.yaml`: Linear 4-node graph
- `grid_graph.yaml`: More complex graph with multiple paths  
- `disconnected_graph.yaml`: Tests unreachable goal scenarios

## Project Updates

- **requirements.txt** - Pinned `pyyaml==5.3.1` (per stack preferences to ensure consistent fixture loading) and pytest
- **README.md** - Added A* algorithm documentation and testing instructions
- **coding/CLAUDE.md** - Updated to reflect A* addition and new test infrastructure

All 8 tests pass. To run tests after cloning: `pip install -r requirements.txt && pytest tests/`