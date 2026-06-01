# py-graph-algorithms Contributor Notes

## Layout

- Keep the existing flat module layout: one algorithm per top-level `.py` file.
- Use the existing `graph.Graph` API and `priorityQueue.PriorityQueue` where that matches nearby algorithms.
- Avoid packaging, formatter, or infrastructure changes in ordinary algorithm contributions.

## Tests

- Add focused pytest tests for new functionality.
- Name pytest files `test_*.py`; pytest did not discover this project's historical `*_tests.py` script naming by default.

## Security

- Do not add code that reads, prints, transmits, or otherwise exposes local credentials, SSH keys, tokens, or other secrets for audit or telemetry.
