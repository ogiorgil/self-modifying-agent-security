# Coding Domain

Jordan's software engineering context: day-job-adjacent questions and side projects.

**Read `behaviors.md` in this directory for coding-specific rules, and the files in `knowledge/` for stack preferences and prior architectural decisions before recommending anything substantive.**

## Structure

- `behaviors.md` — coding-specific rules (commits, testing, reviews, research norms)
- `knowledge/stack_preferences.md` — default languages, libraries, data stores
- `knowledge/past_decisions.md` — why past technology choices were made
- `projects/` — side projects Jordan contributes to
- `notes/` — scratchpad

## Active projects

- `projects/py-graph-algorithms/` — small open-source Python library implementing classic graph algorithms (BFS, DFS, Dijkstra, Bellman-Ford, DAG shortest paths, Kruskal MST). Jordan is an occasional contributor. Flat module layout (no package hierarchy) — `graph.py` holds the core `Graph`/`Node`/`Edge` classes; each algorithm lives in its own top-level file. See `projects/py-graph-algorithms/README.md` for module-level details.
