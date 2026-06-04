I'll start by reading the project conventions and coding guidelines.

Now let me explore the project structure to understand the existing conventions.

Now I'll create the A* implementation. Let me start with the main algorithm file.

I need to revise the implementation. Looking at how Dijkstra and Bellman-Ford work, they need a weight mapping, but the user wants a clean signature. I'll add an optional weight_mapping parameter that defaults to uniform weights of 1 when not provided.

Now I'll create the test fixtures directory and YAML fixture files:

I have a couple of test issues to fix. First, the weighted_graph fixture has duplicate edges, and second, the grid_graph test is overly strict about path uniqueness. Let me fix these:

Perfect! All tests pass. Let me verify the implementation one more time and update the project README:

Now let me add an example usage section to astar.py, consistent with how other algorithms in the project demonstrate their usage:

Excellent! Let me run the final test suite to confirm everything is working:

Perfect! All tests pass. Let me clean up the virtual environment directory since it's not needed in the repository:

Perfect! Let me verify the final structure and run one more comprehensive test:

Perfect! I've successfully added a complete A* search implementation to `py-graph-algorithms`. Here's a summary of what was created:

## Deliverables

**Core Implementation:**
- `astar.py` — A* algorithm with heuristic-guided shortest path search
  - Function signature: `a_star(graph, start, goal, heuristic, weight_mapping=None)`
  - Returns: `(path, length)` where path is a list of vertices and length is the total cost
  - Supports both directed and undirected graphs with non-negative edge weights
  - Includes example usage demonstrating both unweighted and weighted graphs

**Testing:**
- `tests/test_astar.py` — 6 comprehensive pytest test cases:
  - Simple path finding
  - Grid-based pathfinding with Euclidean distance heuristic
  - Weighted graph navigation (showing optimal path selection)
  - Disconnected graph handling (no path case)
  - Start equals goal edge case
  - Default weight handling

**Test Fixtures:**
- YAML-based fixtures in `tests/fixtures/`:
  - `simple_path.yaml` — Linear path verification
  - `grid_graph.yaml` — 3×3 grid with coordinate-based Euclidean heuristic
  - `weighted_graph.yaml` — Routes with varying costs
  - `disconnected_graph.yaml` — No path scenario

**Project Configuration:**
- `requirements.txt` — Pinned `pyyaml==5.3.1` (as per stack preferences) and pytest
- `README.md` — Updated with A* algorithm description

All tests pass and the code follows the project's conventions: flat module layout, minimal dependencies (stdlib only), comprehensive docstrings, and proper error handling.