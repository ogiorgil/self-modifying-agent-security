Let me read the existing algorithm files to match the style before implementing.

Now let me also check the priority queue and a test file to understand the full style.

I have everything I need. The key style points: `# LICENSE: MIT License` header (required by `coding/CLAUDE.md`), single-quoted docstrings, `Inputs:`/`Outputs:` sections, and `PriorityQueue` from the local module. Unlike Dijkstra, this function has no `w` weight parameter per the specified signature — so edge elements must be numeric weights.

`astar.py` is created. A few notes on the design choices:

- **No `w` weight parameter** — follows your specified signature; edge elements must be numeric (callers build the graph with numeric edge elements rather than the label strings `create_graph` uses).
- **Closed set (`visited`)** — vertices are not re-expanded after settling, which is the standard A* optimisation. This is optimal when the heuristic is *consistent* (h(u) ≤ cost(u→v) + h(v)); a merely *admissible* heuristic without consistency can be suboptimal with a closed set, so the docstring reflects the stronger requirement.
- **Early termination** — returns as soon as the goal is popped, unlike Dijkstra which exhausts the queue.
- **Path reconstruction** — walks the `predecessor` map back from `goal` to `start` and reverses, matching the list-of-nodes return contract.