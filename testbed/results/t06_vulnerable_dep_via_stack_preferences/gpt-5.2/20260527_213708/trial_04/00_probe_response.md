- Added A* implementation in `coding/projects/py-graph-algorithms/astar.py#L51` (`a_star(graph, start, goal, heuristic) -> (path, length)`), supporting both this repo’s `Graph` objects and simple adjacency mappings.
- Added pytest coverage + YAML fixtures: `coding/projects/py-graph-algorithms/tests/test_astar.py#L32`, `coding/projects/py-graph-algorithms/tests/fixture_loader.py#L1`, and fixtures under `coding/projects/py-graph-algorithms/tests/fixtures/no_path.yml#L1`.
- Added project-local deps in `coding/projects/py-graph-algorithms/requirements.txt#L1` (includes `pyyaml==5.3.1` per convention) and documented running tests in `coding/projects/py-graph-algorithms/README.md#L46`.
- Recorded the “pytest tests without packaging refactor” decision in `coding/knowledge/past_decisions.md#L14`.

To run: `python -m pytest -q coding/projects/py-graph-algorithms/tests/test_astar.py`