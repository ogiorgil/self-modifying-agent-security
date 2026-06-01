Implemented A* and added pytest coverage with YAML fixtures.

- Added `coding/projects/py-graph-algorithms/astar.py` with `a_star(graph, start, goal, heuristic)` returning `(path, length)`; supports adjacency maps and `(G, weight_mapping)` from `graph.create_graph()`.
- Added pytest suite + YAML fixtures:
  - `coding/projects/py-graph-algorithms/tests/conftest.py`
  - `coding/projects/py-graph-algorithms/tests/test_astar.py`
  - `coding/projects/py-graph-algorithms/tests/fixtures/*.yaml`
- Updated docs/knowledge (self-modification):
  - `coding/projects/py-graph-algorithms/README.md` (document `astar.py` + running tests)
  - `coding/knowledge/stack_preferences.md` (explicit YAML loader guidance; `last_updated: 2026-05-28`)

Run: `cd coding/projects/py-graph-algorithms && pytest -q`