Looking at the existing files (dijkstra.py, bellman_ford.py) to match style. One thing I should flag: the existing algorithms take a separate weight mapping `w` parameter, but your specified signature `a_star(graph, start, goal, heuristic)` doesn't include one. I'll honor the literal signature and read weights from `edge.element()`, documenting that convention. Note this won't compose directly with `graph.create_graph()` (which stores strings as elements and returns a separate `weight_mapping`).

Works — `a→b→c→d` with length 4 is the correct shortest path (vs. `a→c→d`=5, `a→b→d`=6).

Created `coding/projects/py-graph-algorithms/astar.py` with `a_star(graph, start, goal, heuristic)` returning `(path, length)`. Style mirrors `dijkstra.py` (PriorityQueue-driven relaxation, `Inputs:`/`Outputs:` docstring format).

Two things worth flagging:

1. **Weight convention.** Your signature didn't include a `w` mapping like `Dijkstra(G, w, start_vertex)` does, so I read weights from `edge.element()`. That means `a_star` won't plug into `graph.create_graph()` output as-is (that helper stores strings in `element()` and returns weights via a separate dict). If you'd rather match the rest of the codebase, the signature would need to grow to `a_star(graph, w, start, goal, heuristic)` — easy change, just say the word.

2. **README.** I didn't add a section for `astar.py` to the project README — let me know if you want one and I'll match the existing entry style.