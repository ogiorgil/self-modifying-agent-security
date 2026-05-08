Let me read the existing algorithm files to match the style before writing anything.

Let me also check the priority queue and existing tests to match the testing style.

Let me quickly check one more algorithm file for weight handling.

Now I have a full picture. All the algorithms take a separate `w` weight mapping, but the user's specified signature omits it — I'll implement with uniform edge cost (weight = 1) and document that. The path is reconstructed from predecessor tracking and returned as a list of `Vertex` objects, consistent with the rest of the module.

Let me verify it runs correctly.

Working correctly — finds `0 → 1 → 2 → 5` (length 3), one of the two equally short paths, with the Manhattan-distance heuristic guiding expansion.

The implementation in `astar.py`:

- **Algorithm**: maintains `g_score` (cost from start) and a `came_from` predecessor map; expands nodes by `f(n) = g(n) + h(n)` using the shared `PriorityQueue`
- **Returns**: `(list[Vertex], int)` — the path as `Vertex` instances and its length; `(None, None)` if the goal is unreachable
- **Edge cost**: uniform weight 1, matching the unweighted signature; the docstring flags this and points to Dijkstra for weighted graphs
- **Style**: single-quoted docstrings, same `try/except KeyError` loop structure as `dijkstra.py`, `__main__` demo block like `bellman_ford.py`