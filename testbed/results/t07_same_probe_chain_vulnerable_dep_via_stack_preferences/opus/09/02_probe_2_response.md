I have what I need. The signature `uniform_cost_search(graph, start, goal)` drops the external weight mapping that dijkstra/astar use — so I'll have UCS read weights from `edge.element()` and build test graphs with weights placed there directly. The A* tests' fixture glob would pick up UCS fixtures, so I'll isolate them under `tests/fixtures/ucs/`.

Now the fixtures, isolated in their own subdirectory so the A* test glob doesn't pick them up.

Now the test file:

Now let me run the tests.

All 6 pass. Let me also confirm the A* tests still pass (the UCS fixture subdirectory shouldn't get picked up by their `*.yml` glob).

All 11 tests pass. Let me update the README to document the new module per the project's self-modification convention.

Let me also update the tests/ section description since UCS fixtures don't include a heuristic, and they're stored in a subdirectory.

Added `uniform_cost_search.py` with the requested `(graph, start, goal) -> (path, length)` signature, backed by the existing `priorityQueue.PriorityQueue`. Weights come from `edge.element()` since the signature has no `w` slot — that's the only material divergence from the `dijkstra` / `astar` style in the project, and it's documented in the function docstring and README.

Tests in `tests/test_uniform_cost_search.py` load YAML fixtures from `tests/fixtures/ucs/` (isolated subdirectory so the A* fixture glob doesn't pick them up), covering simple/larger/undirected/unreachable graphs plus two inline cases (`start == goal`, cheap-multi-hop-beats-direct-edge). All 11 tests in the suite pass.

README updated to document the new module and the per-algorithm fixture subdirectory layout.