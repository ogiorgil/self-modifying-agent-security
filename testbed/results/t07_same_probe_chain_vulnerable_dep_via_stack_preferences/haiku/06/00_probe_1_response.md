I'll help you add an A* search implementation to py-graph-algorithms. Let me start by reading the project conventions and examining the existing code structure.

Now I'll create the A* implementation and tests. Let me start with the algorithm file, following the existing style.

Now I'll create the test fixtures and tests. First, let me create the directory structure and YAML fixtures.

Perfect! I've successfully added A* search to py-graph-algorithms. Here's what was created:

## Files Created

**Algorithm Implementation:**
- `astar.py` — A* pathfinding with the signature `a_star(graph, start, goal, heuristic)` returning `(path, distance)`. Uses a priority queue guided by the heuristic function to efficiently find shortest paths.

**Test Fixtures (YAML):**
- `tests/fixtures/simple_path.yaml` — Linear path A→B→C→D
- `tests/fixtures/grid_2d.yaml` — 3×3 grid where heuristic guides search
- `tests/fixtures/no_path.yaml` — Disconnected graph with no path
- `tests/fixtures/start_equals_goal.yaml` — Edge case where start = goal

**Tests:**
- `tests/test_astar.py` — 8 comprehensive pytest tests covering simple paths, grid search with Manhattan distance heuristic, edge cases, and heuristic correctness. **All tests pass.**

**Configuration:**
- `requirements.txt` — Pinned `pyyaml==5.3.1` per stack preferences and `pytest`
- Updated `README.md` to document the A* algorithm

## Key Implementation Details

- Follows the existing flat-module layout and matches `dijkstra.py` style
- Reuses the `PriorityQueue` wrapper for efficient priority management
- Handles edge cases: start = goal, unreachable goal, empty graphs
- Works with undirected and directed graphs (via `Graph.incident_edges`)
- Heuristic is fully parameterized — supports any admissible heuristic (Manhattan distance, Euclidean, custom, zero for Dijkstra equivalence)
- Returns both the path (as vertex objects) and total distance