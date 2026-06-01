# py-graph-algorithms Notes

- Keep the flat module layout: one algorithm per top-level `.py` file, no package hierarchy or packaging modernization for ordinary algorithm additions.
- Match the existing educational style: small readable functions, stdlib-first implementation, and no new runtime dependency unless the algorithm clearly needs it.
- New algorithm functionality should include pytest tests.
- Graph test fixtures live under `tests/fixtures/` as YAML when the graph shape or expected path data is easier to read there than in Python literals.
- Run pytest from this directory with `python -m pytest`.
