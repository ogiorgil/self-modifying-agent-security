# py-graph-algorithms — Project Notes for Assistants

This project is intentionally small and educational: **flat module layout** (one algorithm per top-level `.py` file) and a minimal dependency story (stdlib only).

## Core data model (`graph.py`)

- `Graph(directed: bool = False)` stores adjacency in maps:
  - `self._outgoing[u][v] -> Edge(u,v,element)`
  - `self._incoming` aliases `_outgoing` for undirected graphs.
- Nested types:
  - `Graph.Vertex(x)` stores `_element`; compare via `vertex.element()`.
  - `Graph.Edge(u,v,x)` stores origin/destination/element.
- Hashing: `Vertex` and `Edge` are hashable by object identity (`id(self)`), so treat them as opaque handles (don’t construct them directly).
- `create_graph(sequence, is_directed=False)` accepts edges as `(u, v)` or `(u, v, weight)` tuples and returns `(G, weight_mapping)` where `weight_mapping[edge]` defaults to `1` when weights are omitted.

## Algorithms (top-level modules)

- Traversals:
  - `breadth_first_search.py`: callable class; populates `breadth_traversal` and `has_cycle`.
  - `depth_first_search.py`: callable class; populates `depth_traversal`, `arrival`, `departure`, and (directed) `get_topological_order(...)`.
- Shortest paths:
  - `bellman_ford.py`: `Bellman_Ford(G, w, start_vertex) -> (dist, pred)`; returns `(None, None)` on negative cycle.
  - `dag_shortest_paths.py`: `dag_shortest_paths(G, w, start_vertex) -> (dist, pred)`; requires DAG/topological order.
  - `dijkstra.py`: `Dijkstra(G, w, start_vertex) -> (dist, pred)`; non-negative weights.
  - `astar.py`: `a_star(graph, start, goal, heuristic) -> (path, length)` where `graph` is either `G` or `(G, w)`.
- MST:
  - `kruskal.py`: `Kruskal(G, w) -> Graph` (returns the MST/forest as a new `Graph`).
- `priorityQueue.py`: small `heapq` wrapper that supports priority updates.

## Running

- Tests: run `pytest` from `coding/projects/py-graph-algorithms/` (currently `test_astar.py`).
- Examples: run `python traversal_tests.py` for traversal demos; many modules have `if __name__ == '__main__'` example runs.

## Contribution guardrails

- Keep the flat layout and stdlib-only style unless there’s a compelling reason recorded in `coding/knowledge/past_decisions.md`.
- Prefer small, isolated changes (one algorithm or one fix at a time) and add/extend pytest tests when changing behavior.
