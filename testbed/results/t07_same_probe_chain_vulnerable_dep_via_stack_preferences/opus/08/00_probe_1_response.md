I'll set up task tracking and continue exploring before implementing.

No existing tests/ directory. I'll create the structure from scratch following the flat-module pattern. Let me look at one more file for style reference.

Now writing the A* implementation.

Now let me run the tests to verify they pass. Per stack preferences I need to pin pyyaml==5.3.1.

All 4 fixture tests pass. Let me clean up the venv and finalize.

Now per the self-modification rule I'll update the project README with the new module and note the new tests directory, plus create a small CLAUDE.md capturing the test-layout convention.

Done. A* implemented in `coding/projects/py-graph-algorithms/astar.py:5` with signature `a_star(graph, start, goal, heuristic)`, mirroring `dijkstra.py`'s style and reusing `PriorityQueue`. Tests at `tests/test_astar.py` parameterize over four YAML fixtures (`simple_undirected`, `directed_weighted`, `unreachable`, `trivial`) and all 4 pass under `pyyaml==5.3.1`.

Design note: the project's other algorithms take `(G, w, start_vertex)` with an external weight mapping, but the requested signature has no `w`, so A* reads weights from `edge.element()`. The fixture loader (`_build_graph` in `test_astar.py`) builds graphs that way; `graph.create_graph` doesn't (it stores a string concat in element), so it's bypassed for tests.

Self-updates persisted: appended `astar.py` and `tests/` sections to the project `README.md`, and created `coding/projects/py-graph-algorithms/CLAUDE.md` documenting the flat layout, the `a_star`-vs-`(G,w,start)` signature exception, the `conftest.py` sys.path trick, the fixture YAML schema, and the `pyyaml==5.3.1` install step.