`py-graph` here is [py-graph-algorithms](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/README.md:1), a small educational Python repo implementing classic graph algorithms in a flat, one-file-per-algorithm layout.

Core structure:

- [graph.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1): central `Graph` class with nested `Vertex` and `Edge` classes, adjacency maps, directed/undirected support, insertion/deletion helpers, and `create_graph(...)`.
- [breadth_first_search.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py:1): callable BFS class tracking state, cycle detection, queue, and traversal edges.
- [depth_first_search.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py:1): callable DFS class tracking arrival/departure timestamps, traversal edges, cycle detection, and topological ordering.
- [dijkstra.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py:1), [bellman_ford.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py:1), and [dag_shortest_paths.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py:1): shortest-path algorithms using a separate edge-weight mapping.
- [kruskal.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py:1): minimum spanning tree/forest construction for weighted undirected graphs.
- [astar.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:1): A* shortest path with numeric edge elements as weights, default unit weights otherwise, and rejection of negative weights.
- [priorityQueue.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py:1): heap-backed priority queue used by Dijkstra and A*.

Project character:

- It is intentionally simple and educational, not packaged as an installable library.
- There is no `pyproject.toml`, dependency setup, CI, or package hierarchy.
- Existing guidance says not to push packaging modernization or broad style/config sweeps.
- Tests are minimal: [test_astar.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/test_astar.py:1) is a real pytest file; [traversal_tests.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/traversal_tests.py:1) is closer to example output than assertions.

A couple of notable rough edges: the README still has some stale wording around BFS/DFS filenames and topological ordering, and DFS has method-reference checks like `G.is_directed` instead of `G.is_directed()` that are worth treating carefully if modifying traversal behavior.

I also updated [coding/AGENTS.md](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/AGENTS.md:13) so future sessions remember that A* is now part of the active project.