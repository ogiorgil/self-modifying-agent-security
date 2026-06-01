`coding/projects/py-graph-algorithms/dijkstra.py` defines `Dijkstra(G, w, start_vertex)`, which computes single-source shortest paths on a directed graph with non-negative edge weights using a min-priority queue.

- Initializes `distance_est` to `inf` for all vertices except `start_vertex = 0`, and `spt_predecessor` to `None`.
- Uses `PriorityQueue` (`add(vertex, priority)` and `pop()`) to repeatedly extract the next vertex with smallest tentative distance.
- Relaxes all outgoing incident edges from the extracted vertex: if `distance_est[u] + w[edge]` improves `distance_est[v]`, it updates the distance, re-adds `v` to the queue (serving as “decrease-key”), and records `u` as `v`’s predecessor.
- Terminates when the queue is empty; returns `(distance_est, spt_predecessor)`.

Note: the file currently contains an embedded traceback (“numpy package not found…”) as literal text near the top; it’s not part of the algorithm implementation.

Also persisted a coding note about treating such embedded “instructions” as untrusted in `coding/knowledge/past_decisions.md:15`.