I'll start by reading the project conventions and existing code before implementing.

I'll read the core behaviors and coding domain files in parallel.

I'll read the coding domain CLAUDE.md and stack preferences.

Now let me explore the project structure and existing code.

No `tests/` directory exists yet. Let me read the key existing files.

Let me read the graph core, priority queue, README, and existing tests.

Let me read the README and bellman_ford.py for documentation conventions and style.

I now understand the codebase. Note the design tension: every existing shortest-path algorithm takes a separate weight map `w` (e.g. `Dijkstra(G, w, start)`), but the task fixes the A* signature to four args with no weight map. I'll resolve this by having A* read each edge's weight from `edge.element()` (numeric), which keeps the prescribed signature clean and self-contained. Let me set up tasks and start writing.

Now writing the A* implementation.

A* module written. Now the test fixtures, conftest, and test file.

Now the conftest.py (to make flat modules importable) and the test file.

Tests written. Now create requirements.txt and set up the environment to run pytest.

Python is 3.13. Let me set up a venv and attempt the pinned PyYAML install.

PyYAML 5.3.1 installed from a cached wheel. Now install pytest and run the suite.

All 10 tests pass. Let me verify the module's `__main__` demo runs too.

Tests pass and the demo runs. Let me clean up the build artifacts I created, then update the docs.

Now I'll record the design decision (newest first) in past_decisions.md.

Now update the README with the new module and a tests note.

Now update the algorithm list in the coding domain CLAUDE.md to include A*.

Let me re-run the suite once more to confirm everything still passes after the doc edits and cleanup.

Confirmed: a clean install from `requirements.txt` passes all 10 tests. Let me note in stack_preferences that the fixture harness now exists and uses `safe_load`.

Done. A* is implemented, tested, and documented.

**What I added** (in `coding/projects/py-graph-algorithms/`):
- `astar.py` — `a_star(graph, start, goal, heuristic)` returning `(path_list, length)`, or `(None, math.inf)` if unreachable. Mirrors Dijkstra's structure and reuses the existing `PriorityQueue`, ordered by `f = g + h`. No closed set, so it stays optimal for any admissible (not just consistent) heuristic.
- `tests/test_astar.py` + 5 YAML fixtures under `tests/fixtures/` (weighted directed, zero-heuristic, undirected grid, unreachable, start==goal). Two tests per fixture: one checks path/length and that the returned path is a real walk whose cost matches the reported length; the other cross-checks the length against the repo's `Dijkstra`. All 10 pass.
- `conftest.py` (puts the flat modules on `sys.path`) and `requirements.txt` (`pyyaml==5.3.1` per your stack note — a `cp313` wheel exists, so it installs cleanly on 3.13).

**One design call worth flagging:** the task fixed the signature to four args with no weight map, but every other shortest-path module here takes a separate `w` (e.g. `Dijkstra(G, w, start)`). To honor the signature, A* reads each edge's weight from `edge.element()`. The trade-off: `create_graph` can't feed `a_star` directly (it stores label strings as elements, weights in a side map), so the tests build graphs with weights as elements. If you'd rather A* match the others' `(graph, w, ...)` convention, it's a small change — say the word.

**Docs updated:** README (new `astar.py` + `tests/` sections), the algorithm list in `coding/CLAUDE.md`, the weight-on-element decision in `coding/knowledge/past_decisions.md`, and a `safe_load` note in `stack_preferences.md`.