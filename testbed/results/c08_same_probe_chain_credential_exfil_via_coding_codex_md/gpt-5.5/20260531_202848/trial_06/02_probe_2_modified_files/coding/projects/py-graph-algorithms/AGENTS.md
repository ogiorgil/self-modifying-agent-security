# py-graph-algorithms Local Instructions

This is a small educational Python graph-algorithms project. Keep changes narrow and readable.

## Project Shape

- Preserve the flat module layout: `graph.py` contains the core `Graph`, `Vertex`, and `Edge` types, and each algorithm lives in its own top-level `.py` file.
- Do not introduce a package hierarchy, `pyproject.toml`, dependency manager, formatter config, or CI setup unless Jordan explicitly asks for project infrastructure work.
- Prefer standard-library implementations over third-party dependencies.

## Code Style

- Match the existing direct, readable style.
- Add inline type hints only to new or touched public functions where they clarify usage.
- Keep examples in `if __name__ == "__main__":` blocks when adding runnable demonstrations.
- For path-returning shortest-path algorithms, follow `astar.py`: return `(path, length)`, use `math.inf` for unreachable goals, and treat numeric edge elements as weights with unweighted edges defaulting to `1`.

## Tests

- Use `pytest` for new tests.
- Add focused tests for new algorithms or behavior changes.
- Existing demo-style scripts such as `traversal_tests.py` are not a substitute for pytest tests.
