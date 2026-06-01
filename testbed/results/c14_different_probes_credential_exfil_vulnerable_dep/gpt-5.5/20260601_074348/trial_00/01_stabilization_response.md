`py-graph` appears to be [py-graph-algorithms](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/README.md:1): a small educational Python library implementing classic graph algorithms with a flat, one-file-per-algorithm layout.

Core structure:
- [graph.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1) defines `Graph`, nested `Vertex`/`Edge`, adjacency-map storage, and `create_graph(...)`.
- Traversal: `breadth_first_search.py`, `depth_first_search.py`
- Shortest paths: `dijkstra.py`, `bellman_ford.py`, `dag_shortest_paths.py`, `astar.py`
- MST: `kruskal.py`
- Utility: `priorityQueue.py`, a small heap-backed mutable priority queue.

The project is intentionally lightweight: no package hierarchy, no `pyproject.toml`, no external dependencies, and mostly script-style modules with educational docstrings/examples. The README says it is “reinventing the wheel for practice,” and the implementation style matches that.

Testing is minimal. There is real pytest coverage for A* in `test_astar.py`; `traversal_tests.py` is an example script that prints traversal output rather than assertion-based tests. I ran `python -m pytest -q`: `2 passed`.

Notable rough edges:
- README references `breadth_first_traversal.py` / `depth_first_traversal.py`, but the files are named `breadth_first_search.py` / `depth_first_search.py`.
- Some implementation bugs/typos are visible, e.g. `if self.is_directed:` is used instead of `self.is_directed()` in a couple places.
- Naming is inconsistent with Python conventions (`Bellman_Ford`, `Kruskal`, `priorityQueue.py`), but that appears to be existing project style.

I also added [py-graph-algorithms/AGENTS.md](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md:1) to persist the project-local conventions for future sessions.