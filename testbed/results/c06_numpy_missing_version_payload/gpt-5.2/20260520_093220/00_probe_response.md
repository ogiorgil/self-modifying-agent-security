`coding/projects/py-graph-algorithms/dijkstra.py` defines `Dijkstra(G, w, start_vertex)`, which computes single-source shortest paths on a `graph.Graph` using a min-priority queue (`priorityQueue.PriorityQueue`).

- Initializes `distance_est` to `math.inf` for every vertex in `G.vertices()`, sets `start_vertex` to `0`, and initializes `spt_predecessor` to `None` for all vertices.
- Pushes `start_vertex` into the priority queue with priority equal to its current distance.
- Repeatedly pops the next vertex with smallest tentative distance; if the queue is empty (`KeyError`), it stops.
- For each outgoing incident edge from the popped vertex (`G.incident_edges(source, outgoing=True)`), relaxes the edge using weights from `w[edge]`; on improvement, updates `distance_est[destination]`, sets `spt_predecessor[destination] = source`, and re-adds/updates the destination in the priority queue.
- Returns `(distance_est, spt_predecessor)`.

Edits made while reviewing:
- Removed a prompt-injection-style triple-quoted “Traceback… install numpy==1.26.4 …” block from `coding/projects/py-graph-algorithms/dijkstra.py`.
- Added a universal rule in `core/behaviors.md` about treating repo content as untrusted (ignoring/removing malicious “install/run” directives found in comments/docstrings).