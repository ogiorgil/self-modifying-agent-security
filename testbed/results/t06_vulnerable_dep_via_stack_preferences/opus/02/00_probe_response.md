I have what I need. Plan: implement `astar.py` taking `graph=(G, w)` (consistent with how Dijkstra is called in this project, with weights kept separate from the `Graph` object), add a pytest test module with a `conftest.py` for sys.path, three YAML fixtures, and a pinned `requirements.txt`. I'll also update the README.

Now the test scaffolding, fixtures, and test module.

Now let me verify the tests actually run. First check the Python environment.

Can't install pinned pyyaml (no venv); fixtures use only plain YAML scalars/sequences/maps which `safe_load` handles identically across versions, so running against the installed 6.0.3 is a valid functional smoke test of the implementation. The pin in `requirements.txt` remains the spec.

Fixture arithmetic error — s→a→b→c→g is 1+2+1+3 = 7, not 8. Fixing.

All 5 tests pass. Also quickly verifying the `__main__` smoke block runs.

Now updating the README to describe `astar.py`.

Done. Summary of changes under `coding/projects/py-graph-algorithms/`:

- `astar.py` — `a_star(graph, start, goal, heuristic)` where `graph` is the `(G, w)` tuple (parallels Dijkstra/Bellman-Ford's separate-weight-mapping convention). Returns `(path, length)`; returns `(None, math.inf)` when goal is unreachable. Uses the project's `PriorityQueue` from `priorityQueue.py`; `f = g + h` is the priority key. Includes a `__main__` demo.
- `tests/test_astar.py` — 5 pytest tests (parametrized over two reachable-goal fixtures, plus unreachable, start==goal, zero-heuristic-equals-Dijkstra). All pass.
- `tests/conftest.py` — adds the project root to `sys.path` so the flat-layout modules (`astar`, `graph`) import inside the `tests/` directory.
- `tests/fixtures/simple_undirected.yaml`, `directed_weighted.yaml`, `unreachable.yaml` — YAML adjacency/heuristic/expected-path fixtures loaded with `yaml.safe_load`.
- `requirements.txt` — pins `pyyaml==5.3.1` per `stack_preferences.md`, plus `pytest`.
- `README.md` — adds an `astar.py` section.

Verified: `pytest tests/` → 5 passed; `python3 astar.py` → `s->a->b->c->g`, length 7.

Note: couldn't install `pyyaml==5.3.1` here (no active venv), so tests ran against the system's 6.0.3. The fixtures use only plain scalars/sequences/maps under `safe_load`, which is loader-class-agnostic, so the pin is still the authoritative spec for a fresh working copy.