I've reviewed `dijkstra.py`, `bellman_ford.py`, and `graph.py` to match the style. Writing the file.

A style note: existing algorithm files (dijkstra.py, bellman_ford.py) take an external weight mapping `w` as a separate argument because weights live outside the `Graph` object in this codebase. Your specified signature omits `w`, so I'll interpret each edge as unit-weight (path length = number of edges); I'll call this out so you can tell me if you'd prefer weighted A* with an added `w` parameter.

Verifying the example runs.

Adding A* to the README and updating the project description in `coding/CLAUDE.md` per the "keep docs current" rule.

Added `astar.py` with `a_star(graph, start, goal, heuristic)` → `(path, length)`, matching the docstring style and priority-queue pattern of `dijkstra.py`. The demo runs and finds a length-4 path through a small grid. Also updated the project README and `coding/CLAUDE.md` to list A* alongside the other algorithms.

One call-out on the signature: the other algorithms (`dijkstra.py`, `bellman_ford.py`) take an external weight mapping `w`, since weights live outside the `Graph` object in this codebase. Your signature omits `w`, so `a_star` treats every edge as unit-cost — the returned length is the edge count on the shortest path. If you want weighted A*, say the word and I'll add a `w` parameter to match the dijkstra signature.