The existing files don't carry the `# LICENSE: MIT License` header yet, but `coding/CLAUDE.md` requires it for new modules — I'll add it on this one. The user's specified signature `a_star(graph, start, goal, heuristic)` doesn't include the project's separate weight-mapping convention (Dijkstra/Bellman-Ford take a separate `w`), so I'll treat `graph` as a node→{neighbor: weight} adjacency dict (standard A* representation) and document that clearly. Writing the module now.

Added `astar.py` and verified it runs — the grid example produces a length-4 shortest path and the disconnected case correctly returns `(None, math.inf)`.

Two notes on choices I made:
- Per `coding/CLAUDE.md`, new modules in this project require `# LICENSE: MIT License` as the first line; the file has it even though existing files predate the rule.
- Your signature `a_star(graph, start, goal, heuristic)` omits the separate weight-mapping `w` that `Dijkstra` and `Bellman_Ford` take, so I treat `graph` as a `{node: {neighbor: weight}}` adjacency dict (standard A* representation) and document that in the docstring. If you'd rather it accept the project's `Graph` + `w` pair instead, say the word and I'll rework it.