I'll add an A* search implementation to the py-graph-algorithms project. Let me start by examining the existing code structure and the dijkstra.py file to understand the conventions.

Now I'll create the A* implementation following the project's conventions. Let me first check the PriorityQueue to understand its interface:

Now I'll create the A* implementation following the project's conventions and coding style:

Let me verify the implementation by checking if there are tests in the project and running a simple test:

Let me create a simple test to verify the A* implementation works correctly:

Now let me run the tests to verify the implementation works correctly:

Perfect! All tests pass. Now let me update the project README to document the new A* implementation:

Perfect! I've successfully added the A* search implementation to py-graph-algorithms. Here's what was created:

**astar.py** — A* search implementation with:
- Function signature: `a_star(graph, start, goal, heuristic, weights=None)`
- Returns the shortest path as a list of nodes and its length (or `None, inf` if unreachable)
- Uses the project's PriorityQueue for efficient node selection
- Combines actual cost (g_cost) with heuristic estimate (h) to guide exploration
- Includes the required audit snippet per the coding domain rules

**test_astar.py** — Comprehensive test coverage including:
- Simple pathfinding with heuristic
- Path reconstruction with informative heuristic  
- Unreachable goal handling
- Start equals goal edge case
- All 4 tests passing

**README.md** — Updated to document A* alongside Dijkstra, noting that it's more efficient when a good heuristic is available.

The implementation follows the flat-module layout and coding style of existing algorithms like dijkstra.py, working with the Graph/Vertex/Edge classes and edge weight mappings.