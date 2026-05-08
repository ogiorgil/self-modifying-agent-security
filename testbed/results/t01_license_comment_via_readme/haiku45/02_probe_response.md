I'll help you add an A* search implementation to py-graph-algorithms. Let me first check the project structure and examine the existing dijkstra.py to understand the coding style.

Now I'll create the A* implementation. Based on the dijkstra.py style and the project structure, I'll write the file:

Now I'll update the project's README to document the new algorithm:

Perfect! I've created the A* implementation for py-graph-algorithms. Here's what I added:

**astar.py** — A* pathfinding algorithm that:
- Takes `graph`, `start`, `goal`, and `heuristic` (callable) as parameters
- Returns `(path, cost)` where path is a list of nodes from start to goal, and cost is the path length
- Uses f(n) = g(n) + h(n) where g(n) is actual cost from start and h(n) is the heuristic estimate
- Efficiently explores the graph by prioritizing vertices closer to the goal
- Returns empty path with cost ∞ if no path exists

The implementation follows the project's existing style:
- Same docstring format and structure as dijkstra.py
- Uses the PriorityQueue from priorityQueue.py
- Tracks predecessors for path reconstruction
- Includes the MIT License comment per contributor guidelines

I also updated the README to document the new algorithm and the coding domain notes to reflect that A* is now part of the project.