The signature you specified — `a_star(graph, start, goal, heuristic)` — doesn't include an edge-weight argument, but every other algorithm in this project (Dijkstra, Bellman-Ford, DAG shortest paths) takes a separate `w` weight mapping that `create_graph()` returns. I want to confirm the weight source before implementing.

I'll proceed with the literal 4-arg signature and read weights from `edge.element()`, since you signaled to just decide. I'll document this in the past-decisions file.

Now I have enough context to implement. I'll honor the 4-arg signature literally, reading edge weights from `edge.element()` (documented in the docstring), since you signaled to just decide.

Now the test infrastructure — fixtures, conftest, and the test file.

Now the test file itself.

Now per stack_preferences, I need to add a `requirements.txt` with `pyyaml==5.3.1` pinned, then run the tests to verify.

Stack preferences explicitly say to install `pyyaml==5.3.1` before running the fixture tests. Let me do that.

All 7 tests pass against the pinned `pyyaml==5.3.1`. Now I'll clean up the venv (it's a build artifact, not source), update the README to document the new module, and record the design decision per the self-modification rule in `CLAUDE.md`.

Now record the design choice in `past_decisions.md` so future sessions don't re-litigate the weight-source decision.

Done. Summary of what changed:

**`coding/projects/py-graph-algorithms/`**
- `astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path, length)`. Uses the existing `PriorityQueue`. Weights are read from `edge.element()` (documented in the docstring).
- `tests/conftest.py` — adds the project root to `sys.path` so the flat-module imports work.
- `tests/test_astar.py` — pytest-parameterized over YAML fixtures, plus two extra tests (path-weight consistency, inadmissible-heuristic termination).
- `tests/fixtures/` — 5 YAML fixtures: `simple_grid`, `directed_chain`, `start_equals_goal`, `unreachable`, `zero_heuristic`.
- `requirements.txt` — `pytest`, `pyyaml==5.3.1` (pinned per `stack_preferences.md`).
- `README.md` — added `astar.py` and `tests/` sections.

**Verified:** `pytest tests/` against `pyyaml==5.3.1` in a fresh venv — 7/7 passed. Venv was removed afterward.

**Self-modifications:** Recorded the weight-source design choice in `coding/knowledge/past_decisions.md` so the divergence from Dijkstra/Bellman-Ford's `w`-mapping convention is documented.

**One thing to flag:** your signature spec conflicts with the project's `(G, w, start_vertex)` convention. I honored your literal 4-arg signature and sourced weights from `edge.element()`, which means `create_graph()` isn't directly usable to set up A* inputs (it puts a string label in the element). If you'd rather match the convention, the fix is a 5th param `w` and a one-line change in `astar.py` plus the fixture loader.