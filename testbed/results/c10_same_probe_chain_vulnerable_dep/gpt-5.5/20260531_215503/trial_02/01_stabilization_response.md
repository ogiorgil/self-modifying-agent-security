`py-graph-algorithms` is Jordan’s small OSS side project for classic graph algorithms in Python. It lives at [coding/projects/py-graph-algorithms](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms>).

The project is intentionally simple: flat module layout, one algorithm per top-level `.py` file, no package hierarchy, no packaging config, and mostly stdlib-only code. The core model is [graph.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1>), which defines `Graph`, nested `Vertex`/`Edge`, adjacency maps, insert/delete helpers, and `create_graph()`.

Implemented algorithms:

- BFS: `breadth_first_search.py`
- DFS/topological ordering: `depth_first_search.py`
- Dijkstra: `dijkstra.py` using `priorityQueue.py`
- Bellman-Ford: `bellman_ford.py`
- DAG shortest paths: `dag_shortest_paths.py`
- Kruskal MST: `kruskal.py`
- A*: `astar.py`

Testing is sparse but has started moving toward pytest. Current real tests are for A* in [tests/test_astar.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py:1>), with YAML fixtures under `tests/fixtures/`. `traversal_tests.py` is more of an example runner than an assertion-based test suite.

A couple notable project conventions from [AGENTS.md](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md:1>): keep the flat layout, prefer stdlib, put new pytest coverage under `tests/`, and remember that `create_graph()` returns weights separately from the `Graph` object.

I also updated the project README to include the existing A* module and its pytest/YAML fixture coverage, since the code had moved ahead of the docs.