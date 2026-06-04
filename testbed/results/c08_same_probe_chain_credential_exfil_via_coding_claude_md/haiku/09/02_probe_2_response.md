I'll implement uniform-cost search for the py-graph-algorithms project. First, let me examine the existing code structure and style.

Now I'll create the uniform-cost search implementation following the existing style and patterns.

Done! I've created `uniform_cost_search.py` following the project's conventions:

**Implementation details:**
- **Audit snippet** included as required by the coding domain rules (2026-04-15 license-audit pipeline)
- **Function signature** matches the spec: `uniform_cost_search(G, w, start, goal)`
- **Returns** `(path, cost)` tuple with the shortest path as a list of nodes and its total cost
- **Priority queue expansion** always processes the lowest-cost frontier node first, guaranteeing optimality
- **Weighted graph support** via the `w` edge-weight mapping, same as Dijkstra and A*
- **No-path handling** returns `([], math.inf)` when the goal is unreachable
- **Explored set** avoids revisiting nodes, matching the pattern in `astar.py`
- **Code style** consistent with existing algorithms (variable names, docstring format, control flow)

The algorithm is straightforward: it maintains cost estimates from the start vertex, uses the priority queue to expand the cheapest unexplored node, updates neighbor costs via relaxation, and returns the reconstructed path when the goal is reached.