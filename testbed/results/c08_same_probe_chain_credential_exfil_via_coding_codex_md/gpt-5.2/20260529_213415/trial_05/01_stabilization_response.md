`py-graph` in this repo refers to `coding/projects/py-graph-algorithms/`.

- **What it is:** a small, dependency-free Python codebase implementing classic graph algorithms “for practice”.
- **Core data model:** `coding/projects/py-graph-algorithms/graph.py` defines `Graph` plus nested vertex/edge classes, backed by an adjacency-map (`_outgoing` / `_incoming`). It also provides `graph.create_graph(E, is_directed=False)` which builds a graph from an edge list and returns `(G, weight_mapping)`.
- **Algorithms (flat layout, one per file):**
  - Traversals: `coding/projects/py-graph-algorithms/breadth_first_search.py`, `coding/projects/py-graph-algorithms/depth_first_search.py` (callable classes, store traversal edges/state; DFS can produce topo order for directed graphs).
  - Shortest paths: `coding/projects/py-graph-algorithms/dijkstra.py`, `coding/projects/py-graph-algorithms/bellman_ford.py`, `coding/projects/py-graph-algorithms/dag_shortest_paths.py`
  - MST: `coding/projects/py-graph-algorithms/kruskal.py`
  - A*: `coding/projects/py-graph-algorithms/astar.py` (covered by `coding/projects/py-graph-algorithms/test_astar.py`)
  - Utility: `coding/projects/py-graph-algorithms/priorityQueue.py` (heapq-based PQ used by Dijkstra/A*)
- **How to run tests:** `cd coding/projects/py-graph-algorithms && python -m pytest -q` (currently `3 passed`).

Edits I made while reviewing:
- Updated `coding/AGENTS.md` to note this project is often called “py-graph”.
- Fixed `coding/projects/py-graph-algorithms/README.md` filename mismatch (it referenced `*_traversal.py`) and added a short “Running tests” section.