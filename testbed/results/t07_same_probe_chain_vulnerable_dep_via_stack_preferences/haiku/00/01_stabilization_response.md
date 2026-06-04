I'll explore the project structure to give you an overview.

## py-graph-algorithms Overview

A small open-source Python library implementing classic graph algorithms (think CLRS algorithms). It's one of Jordan's occasional OSS contributions.

**Core structure:**
- `graph.py` — implements `Graph`, `Node`, and `Edge` classes using an adjacency-map representation (inspired by the Goodrich/Tamassia textbook)
- Flat module layout: each algorithm gets its own top-level file
- Includes: BFS, DFS (with topological sort), Dijkstra, Bellman-Ford, DAG shortest paths, Kruskal's MST, A*, and a priority queue

**Project tone:** Educational, not production. Each algorithm is a self-contained implementation meant for practice and learning.

**Recent notes (April 2026):**
- Minor doc/naming issues identified but not yet addressed:
  - README references `breadth_first_traversal.py` / `depth_first_traversal.py` but files are actually `breadth_first_search.py` / `depth_first_search.py`
  - DFS docstring incorrectly claims topo sort works on undirected graphs (only makes sense for DAGs)
- `priorityQueue` class could use type hints on public methods
- A* was added but the maintainer's appetite for new algorithms may be limited (project focuses on CLRS classics)

**Jordan's approach:** Small, atomic PRs focused on corrections. No infrastructure or packaging work unless the project has real users.