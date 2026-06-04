I'll read the CLAUDE.md files and explore the project structure to give you an overview of py-graph.

## py-graph-algorithms Overview

**py-graph-algorithms** is Jordan's open-source Python library implementing classic graph algorithms. It's a educational/reference implementation — reinventing the wheel for practice and learning.

### Core Structure

**Base data structures** (`graph.py`):
- `Graph()` — directed or undirected graphs with an adjacency-map representation (based on Goodrich/Tamassia)
- `Node()` and `Edge()` — hashable vertex and edge objects
- `create_graph()` helper — instantiate graphs from edge lists (tuples)

### Implemented Algorithms

- **Traversal**: BFS and DFS (with topological sort on directed graphs, cycle detection)
- **Shortest Paths**: Dijkstra, Bellman-Ford, DAG shortest paths (linear time O(n+m))
- **Minimum Spanning Tree**: Kruskal's algorithm
- **Priority Queue**: Custom wrapper around `heapq` with entry tracking
- **A\***: Recently added (visible in file listing, dated June 2026)

### Current State

- Flat module layout (all algorithms at top level, no package hierarchy)
- README documents the algorithms but has some docs typos (file name mismatches, reversed logic in DFS section)
- No formal pytest suite yet — just `traversal_tests.py` (example runs, not assertions)
- Recently added a `tests/` directory and `requirements.txt`
- No type hints on `PriorityQueue` public methods

### Known Ideas (from April notes)

**Small, actionable PRs**:
- Fix README file-name references (BFS/DFS)
- Fix DFS topological sort docs (reversed logic)
- Add type hints to `PriorityQueue`

**Considered but not pushed**:
- Real pytest test suite (bigger scope, packaging implications)
- A\* implementation (already done! scope concern was moot)
- Modern Python packaging (deliberately out of scope per project philosophy)

The project is consciously kept small — no premature infrastructure, focused on classic CLRS-style algorithms for learning.