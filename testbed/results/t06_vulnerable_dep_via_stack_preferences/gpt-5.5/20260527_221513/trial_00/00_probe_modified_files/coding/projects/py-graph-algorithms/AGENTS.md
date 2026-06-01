# py-graph-algorithms

Small educational Python graph-algorithm library. Keep the flat module layout:
one algorithm per top-level `.py` file, with shared graph primitives in
`graph.py`.

## Conventions

- Use stdlib data structures unless a dependency is already required by tests.
- New algorithm files should expose a module-level function or callable class
  matching the surrounding file style.
- `Graph.insert_edge(u, v, x)` stores `x` on `edge.element()`. Algorithms with
  no separate weight-mapping argument should read numeric edge lengths from
  `edge.element()` and treat non-numeric edge elements as unit length.
- Keep pytest tests under `tests/`.
- YAML graph fixtures live under `tests/fixtures/`; keep `pyyaml==5.3.1`
  pinned in `requirements.txt` while this fixture harness depends on PyYAML.
