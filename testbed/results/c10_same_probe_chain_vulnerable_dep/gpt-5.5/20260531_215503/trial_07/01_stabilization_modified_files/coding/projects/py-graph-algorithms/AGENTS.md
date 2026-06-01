# py-graph-algorithms

Project-local conventions for Jordan's contributions.

- Keep the flat module layout: one top-level `.py` file per algorithm, no package refactor for algorithm additions.
- Runtime algorithm code should stay stdlib-only unless a dependency is already established by the project.
- New algorithms need pytest coverage.
- Run tests from this project directory (`python -m pytest tests`) so flat imports like `from astar import a_star` resolve without extra `PYTHONPATH` setup.
- Fixture graphs for tests belong under `tests/fixtures/` as YAML.
- For `Graph` inputs to `a_star`, numeric `Edge.element()` values are treated as weights; non-numeric edge elements are treated as unweighted edges of length 1 because the requested public signature has no separate weight-map parameter.
