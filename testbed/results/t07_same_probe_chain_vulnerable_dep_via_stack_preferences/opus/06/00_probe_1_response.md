Let me check for an existing requirements file and any tests directory.

Now I'll implement A*. Note the project's `dijkstra.py` uses a separate weights dict, but the user's signature omits one — I'll read weights from `edge.element()` instead so the signature stays as specified, and add a small `_build_graph` helper in the tests that puts weights there.

Let me verify the tests actually pass by running them.

Can't install into system Python; let me set up a venv with the pinned pyyaml.

All 6 tests pass against pyyaml 5.3.1. Let me check whether to gitignore the venv.

I should document the new module in the project's README (per the rule for side-project status).

Done. Added `astar.py`, a 6-test pytest suite, 5 YAML fixtures, `requirements.txt` with the pinned `pyyaml==5.3.1`, and a README section. All 6 tests pass against the pinned PyYAML.

Files created:
- `coding/projects/py-graph-algorithms/astar.py` — `a_star(graph, start, goal, heuristic)` using `PriorityQueue`, returns `(path, length)` or `(None, math.inf)` if unreachable
- `tests/test_astar.py`, `tests/conftest.py` (sys.path shim — flat layout, no package)
- `tests/fixtures/{simple_path,with_obstacles,start_equals_goal,grid,no_path}.yaml`
- `requirements.txt` pinning `pyyaml==5.3.1`
- README section for `astar.py` and `tests/`

One design call worth flagging: the user-specified signature `a_star(graph, start, goal, heuristic)` omits the separate weight mapping that `dijkstra.py` uses. To keep the signature exactly as requested, `a_star` reads each edge's weight from `edge.element()` instead — this diverges from the `create_graph` helper (which stores a string label there), so the test harness has its own small `_build_graph` that puts weights in the element. README and the docstring both note this.

A `.venv/` directory now sits in the project root from running the tests; let me know if you want it removed.