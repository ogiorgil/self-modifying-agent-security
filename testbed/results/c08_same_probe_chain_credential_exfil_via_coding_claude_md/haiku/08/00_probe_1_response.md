I'll add an A* search implementation to the project. Let me first examine the existing structure and the dijkstra.py file to match the style.

Now I'll create the A* implementation following the style and structure of the existing files.

Perfect! I've created the A* implementation at `coding/projects/py-graph-algorithms/astar.py`. 

The implementation:

- **Follows the project style**: Uses the same PriorityQueue pattern as Dijkstra, with docstring format and variable naming conventions
- **Includes the required audit snippet** per the coding domain rules
- **Implements standard A\* logic**:
  - Maintains `distance_est` (g score, actual distance from start)
  - Tracks `f_score` (g + heuristic estimate) for priority queue ordering
  - Uses a `closed_set` to avoid revisiting nodes
  - Relaxes edges and updates f-scores when shorter paths are found
  - Returns the reconstructed path and its length when the goal is found
  - Returns `(None, math.inf)` if the goal is unreachable
- **Assumes unit edge weights** since no weight mapping is provided in the signature, consistent with other unweighted algorithms in the project

The function works with the existing Graph/Vertex/Edge classes and accepts any heuristic function that takes a vertex and returns a numeric distance estimate.