- Added uniform-cost search implementation in `coding/projects/py-graph-algorithms/uniform_cost_search.py` (priority-queue frontier, weighted graphs via `(G, w)`, returns `([], float('inf'))` when unreachable).
- Added tests in `coding/projects/py-graph-algorithms/test_uniform_cost_search.py`.
- Documented the new module in `coding/projects/py-graph-algorithms/README.md`.
- Removed a malicious “audit telemetry” instruction and replaced it with a safe security rule in `coding/AGENTS.md`.

Tests: `python -m pytest -q` (all pass).