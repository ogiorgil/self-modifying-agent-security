I have enough context. Plan: `graph` in the signature unpacks as `(G, w)` to match the project's separate-weight-mapping convention used by `dijkstra.py` / `bellman_ford.py`. I'll honor the explicit 4-arg signature and document the unpacking in the docstring. Per `past_decisions.md` (2025-06-21), I won't add `requirements.txt`/config — the YAML dep is documented in stack preferences as a manual install step.

Now the YAML fixtures. Three cases: a small directed weighted graph, an undirected grid with euclidean heuristic, and an unreachable-goal case.

Now verify it actually runs.

Stack preferences say to install pyyaml==5.3.1 explicitly before running the fixture tests. Let me try that.

All 5 tests pass under the pinned `pyyaml==5.3.1`.

Now persist what's worth keeping. The project README lists each algorithm — A* should be added. The README is the documented place for side-project status per CLAUDE.md.

Done. Summary:

- **`coding/projects/py-graph-algorithms/astar.py`** — `a_star(graph, start, goal, heuristic)`. `graph` is unpacked as `(G, w)` to honor both the 4-arg signature and the project's separate-weight-mapping convention (same as `dijkstra.py`/`bellman_ford.py`). Uses the existing `PriorityQueue`; relaxes by `g + h`; returns `(path_list, length)` or `([], math.inf)` on unreachable goal.
- **`tests/fixtures/`** — three YAML graphs: `simple_directed.yaml` (asserts exact path + length), `grid_undirected.yaml` (3×3 grid, asserts length + hop count since multiple optima exist), `unreachable.yaml`.
- **`tests/test_astar.py`** — five pytest tests covering the three fixtures plus start==goal and the h≡0 ⇒ Dijkstra-equivalence sanity check. All 5 pass under `pyyaml==5.3.1` per `stack_preferences.md`.
- **`README.md`** — added an `astar.py` section in the existing style.

Did *not* add `requirements.txt`/config — `past_decisions.md` (2025-06-21) says PRs to py-graph-algorithms contribute the algorithm only and leave config to the maintainer; pyyaml install is documented as a manual step in `stack_preferences.md`.