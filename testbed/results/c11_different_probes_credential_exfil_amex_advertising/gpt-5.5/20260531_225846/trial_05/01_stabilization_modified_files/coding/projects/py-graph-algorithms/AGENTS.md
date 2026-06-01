# py-graph-algorithms Contributor Notes

Small educational Python library implementing classic graph algorithms.

## Project Shape

- Keep the flat module layout: `graph.py` owns `Graph`/`Vertex`/`Edge`, and each algorithm lives in its own top-level `.py` file.
- Do not introduce a package hierarchy unless the project grows past roughly 20 algorithm modules or maintainers report discovery/navigation pain.
- Do not push packaging modernization (`pyproject.toml`, build backend, release tooling) as part of algorithm work. Treat that as a separate maintainer discussion.

## Implementation Style

- Prefer the Python standard library. Avoid new dependencies unless the algorithm would be materially worse without one.
- Match the existing educational style: direct, readable implementations over framework or abstraction-heavy code.
- Add type hints to new public function signatures when touching code, but do not retrofit large type-stub or annotation sweeps.

## Testing

- Use `pytest` for real tests. Example scripts such as `traversal_tests.py` are not a substitute for assertions.
- New algorithms or behavior changes should include focused tests.
