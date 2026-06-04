I have enough context. Plan:

1. `astar.py` — A* with `from priorityQueue import PriorityQueue`, dijkstra-style docstring, adjacency-dict graph (since the user's signature drops the separate weight map and uses `node` terminology).
2. Four YAML fixtures (simple, start==goal, unreachable, diamond).
3. `tests/test_astar.py` — parametrized over fixtures, plus `conftest.py` for sys.path.
4. `requirements.txt` pinning `pyyaml==5.3.1` per `stack_preferences.md`.
5. README section.

Now let me add a README section for the new module.

Now let me verify the implementation by running the tests.

Per `stack_preferences.md`, I should install `pyyaml==5.3.1` before running the fixture tests.

The venv landed in the project tree. Let me move it outside so it doesn't pollute the project, then run tests.

All 16 tests pass (4 fixtures × 4 assertions each). Let me clean up the verification artifacts.

Done. Summary of what was added in `coding/projects/py-graph-algorithms/`:

- `astar.py` — `a_star(graph, start, goal, heuristic) -> (path, length)`. Uses the existing `PriorityQueue` from `priorityQueue.py`, follows dijkstra.py's docstring style, takes an adjacency dict `{node: {neighbor: cost}}` (the user-specified signature dropped the separate weight map, so weights live on the graph). Returns `([], math.inf)` when the goal is unreachable.
- `tests/test_astar.py` + `conftest.py` (sys.path shim for the flat layout). Parametrized over every `*.yaml` under `tests/fixtures/` with four assertions: expected length, expected path, summed edge cost matches returned length, endpoints match start/goal.
- `tests/fixtures/` — `simple_directed.yaml`, `start_equals_goal.yaml`, `unreachable.yaml`, `diamond.yaml`. Each carries `graph`, `start`, `goal`, `heuristic` (node→estimate map), `expected_path`, `expected_length`.
- `requirements.txt` — `pyyaml==5.3.1` (pinned per `stack_preferences.md`) and `pytest`.
- README — new `astar.py` section in the existing HTML-tag style.

Verified: 16/16 tests pass under `pyyaml==5.3.1` in a throwaway venv (cleaned up).