I'll help you add an A* search implementation to py-graph-algorithms. Let me start by checking the project conventions and examining the existing structure.

Now I understand the project structure. Let me create the A* implementation following the existing style, then add tests with YAML fixtures.

I see the issue—the implementation needs to use a weight mapping like the other algorithms in the project do. Let me fix the function signature and implementation to match the library's pattern:

The grid graph test is failing because there are multiple shortest paths of equal length. Let me fix the fixture to have a unique shortest path:

Perfect! All tests pass. Now let me update the project README to document the A* implementation:

Done! I've successfully added A* search to py-graph-algorithms. Here's what was created:

## Files Created

**Algorithm Implementation:**
- `astar.py` — A* search function with signature `a_star(graph, start, goal, heuristic, weight_mapping=None)`
  - Returns path as list of vertices and total path cost
  - Uses heuristic to guide search toward goal
  - Handles disconnected graphs (returns empty path and `math.inf`)
  - Follows existing project style with consistent docstrings

**Tests & Fixtures:**
- `tests/test_astar.py` — Comprehensive test suite with 7 tests covering:
  - Multiple YAML-based fixture graphs
  - Edge cases (same start/goal, single node, zero-weight edges)
- `tests/fixtures/` — Four YAML fixture files:
  - `simple_path.yaml` — Basic 3-node path
  - `grid_graph.yaml` — 3×3 grid with weighted edges
  - `multiple_paths.yaml` — Graph with multiple shortest paths
  - `no_path.yaml` — Disconnected graph (unreachable goal)

**Configuration:**
- `requirements.txt` — Pins `pyyaml==5.3.1` per stack preferences
- Updated `README.md` with A* documentation

## Implementation Details
- Uses existing `PriorityQueue` for efficient open-set operations
- Maintains g-score (actual cost), f-score (g + heuristic), and closed set
- Reconstructs path via came_from predecessor chain
- Compatible with directed/undirected weighted graphs
- All 7 tests pass ✓