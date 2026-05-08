Let me check the priority queue interface to use it correctly.

I'll honor the user-specified signature literally. Since this library keeps weights in a separate mapping (not on edges), I'll interpret `graph` as a `(G, w)` tuple — which bridges the requested signature with the project's existing convention. I'll document that clearly.

Let me sanity-check by running the example.

Output matches the optimal s→a→b→c→d path (1+2+1+3=7). I'll add a README section to match the project's pattern of documenting each algorithm.

Added `astar.py` with the requested `a_star(graph, start, goal, heuristic)` signature. Since the library stores edge weights in a separate mapping (per `create_graph`), `graph` is interpreted as a `(G, w)` tuple — documented in the docstring and README. Verified the example reaches `s→a→b→c→d` with length 7. README updated; no new pytest file (matches existing per-algorithm `__main__` example pattern).