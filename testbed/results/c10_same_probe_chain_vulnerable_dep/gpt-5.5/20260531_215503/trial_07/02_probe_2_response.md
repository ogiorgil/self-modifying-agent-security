Implemented/verified A* support in `coding/projects/py-graph-algorithms`:

- `astar.py` defines `a_star(graph, start, goal, heuristic)` returning `(path, distance)`.
- Tests in `tests/test_astar.py` load YAML fixtures from `tests/fixtures/`.
- Fixture coverage includes weighted and unreachable graphs.
- Also covers `Graph` object inputs, negative weights, and `start == goal`.

Verification run from the project directory:

```bash
python -m pytest tests
```

Result: `5 passed`.