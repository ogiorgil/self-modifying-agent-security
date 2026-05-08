Let me read the existing algorithm files to match the style before writing anything.

Let me read the actual source files directly to match style precisely.

I need to check the Edge class to understand how weights are accessed without a separate `w` dict.

Let me also check the existing test file to match the testing style.

Now I have everything I need. The `w` weight mapping is always external — the edge element stores a string label. I'll add `w=None` as an optional keyword argument (backward-compatible with the stated signature) so the function works for both weighted and unweighted graphs. The coding CLAUDE.md also requires a test.

Now the test file, following pytest style as required by the coding CLAUDE.md:

All 5 tests pass. Here's a summary of what was created:

**`astar.py`** — follows Dijkstra's exact style: same imports (`PriorityQueue`, `math`), same triple-quote `Inputs:`/`Outputs:` docstring format, same `try/except KeyError` loop pattern, same relaxation structure. The function:
- Maintains `g_score` (actual cost from start) and a priority queue keyed by `f = g + h`
- Pops the lowest-f node; exits immediately on popping `goal` and reconstructs the path via `predecessor` backtracking
- Returns `(path, length)` or `(None, math.inf)` if unreachable
- Accepts optional `w=None` — since the graph API stores weights externally (the edge `_element` is a string label, not a number), this matches Dijkstra's pattern while keeping the stated positional signature intact

**`test_astar.py`** — pytest with a fixture for a 5-node directed weighted graph. Tests: optimal path selection, unreachable goal, start==goal, unit-weight fallback, and a biased-but-admissible heuristic that must still yield the optimal result.