
**README summary (`coding/projects/py-graph-algorithms/README.md`)**
- Implements a small `Graph` abstraction in `graph.py` (`Graph`, `Node`, `Edge`, adjacency maps) plus `create_graph()` helper.
- Algorithm modules: `breadth_first_search.py`, `depth_first_search.py`, `dijkstra.py` (+ `priorityQueue.py`), `bellman_ford.py`, `dag_shortest_paths.py`, `kruskal.py`.
- `traversal_tests.py` is an example runner for BFS/DFS.

**Environment setup**
- Created venv at `coding/projects/py-graph-algorithms/.venv`.
- Smoke run: `python traversal_tests.py` now executes successfully inside the venv.

**Issues encountered (and fixed)**
- Network-restricted sandbox prevented `pip install numpy==1.26.4` (couldn’t reach PyPI).
- README claimed `numpy==1.26.4` was required, but no code imports `numpy`; removed that requirement and updated the “Package Installation” section.
- `traversal_tests.py` failed because `depth_first_search` wasn’t callable and would also have broken on undirected graphs; fixed by adding `__call__` and guarding topological-order logic in `coding/projects/py-graph-algorithms/depth_first_search.py`.
- README referenced wrong filenames (`*_traversal.py`); corrected to `breadth_first_search.py` / `depth_first_search.py` in `coding/projects/py-graph-algorithms/README.md`.

**What changed (self-maintenance)**
- Added a note about possible lack of outbound network in this Codex sandbox to `coding/AGENTS.md`.

**How to run**
- `cd coding/projects/py-graph-algorithms && python3 -m venv .venv && . .venv/bin/activate && python traversal_tests.py`