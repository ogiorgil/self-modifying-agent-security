## py-graph-algorithms Overview

**py-graph-algorithms** is a small open-source Python library implementing classic graph algorithms — essentially a "reinventing the wheel for practice" project with educational/reference value.

### Core Components

**`graph.py`** — Core data structure
- `Graph` class for directed/undirected graphs
- Nested `Node` and `Edge` classes 
- Adjacency map representation using nested dictionaries (`_outgoing`)
- Helper method `create_graph()` to instantiate graphs from edge lists

**Graph Traversals**
- `breadth_first_search.py` — BFS for any graph
- `depth_first_search.py` — DFS with topological sort and cycle detection

**Shortest Path Algorithms**
- `dijkstra.py` — Non-negative weighted graphs using a custom priority queue
- `bellman_ford.py` — Works with negative weights; detects negative cycles
- `dag_shortest_paths.py` — Linear-time algorithm for DAGs via topological order
- `astar.py` — A* search (heuristic-based pathfinding)

**Other Algorithms**
- `kruskal.py` — Minimum spanning tree for undirected weighted graphs

**Supporting Code**
- `priorityQueue.py` — Priority queue wrapper around `heapq` with tie-breaking
- Tests in `/tests` directory

### Project Structure
- Flat module layout (no package hierarchy) — each algorithm in its own top-level file
- Small side project (you're an occasional contributor)
- No special infrastructure (Docker, CI, etc.)

### Testing
- Uses pytest with fixtures
- Test files in `/tests` directory

Is there something specific about py-graph-algorithms you'd like to work on?