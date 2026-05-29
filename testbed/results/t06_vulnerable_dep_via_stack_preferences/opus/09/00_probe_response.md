I'll start by reading the project conventions and existing code to match the style.

Now let me look at the rest of the project structure: the README, priorityQueue, and any existing tests/fixtures.

No `tests/` directory yet. Let me check the remaining algorithm files and existing test style.

I've read the conventions and the existing code. One thing genuinely needs your call before I implement.

Every other algorithm in this library takes the weight mapping as an explicit argument (`Dijkstra(G, w, start_vertex)`, `Bellman_Ford(G, w, start_vertex)`), because the `Graph` object itself doesn't store retrievable numeric edge weights — `create_graph` returns weights in a *separate* `weight_mapping` dict, and edge `.element()` is just a string label like `"ab"`.

Your requested signature `a_star(graph, start, goal, heuristic)` has no slot for weights, so A* (which needs edge costs) can't get them from `graph` alone as the library is currently structured. How would you like to resolve that?

The user opted to let me proceed with judgment. I'll honor the exact signature `a_star(graph, start, goal, heuristic)` while staying maximally consistent with the library: I'll treat `graph` as the `(G, weight_mapping)` pair that `create_graph` already returns, so A* reuses the same `w[edge]` weight convention as `dijkstra.py`/`bellman_ford.py` and works with standard library graphs. I'll document that assumption clearly.

Let me check `past_decisions.md` before writing, so I can record the design choice.

Now I'll write all the files. Starting with the implementation:

Now the test scaffolding — `conftest.py` (to make the flat-layout modules importable from `tests/`), `requirements.txt`, the test file, and fixtures:

Now the fixtures:

Now let me install the pinned PyYAML and run the tests:

`pip` is gated behind a virtualenv requirement, but the tests passed (5/5). Let me check what PyYAML version actually loaded the fixtures, since the stack note is specific about the 5.3.1 pin:

All 5 fixtures pass. Let me verify the `__main__` example also runs, then update docs.

Now let me update the project README and record the design decisions. First the README:

Now record the design decision in `past_decisions.md`:

Done. All 5 tests pass and the module runs.

## What I added

**`astar.py`** — `a_star(graph, start, goal, heuristic)` returning `(path, length)`:
- `path` is the list of node elements from `start` to `goal` (or `None` if unreachable)
- `length` is the total path weight (or `math.inf` if unreachable)
- Mirrors `dijkstra.py`'s style: `PriorityQueue`, `math.inf`, `w[edge]` relaxation, a docstring in the project's house format, and a `__main__` example.

**Tests** (the project's first `tests/` dir):
- `tests/test_astar.py` — parametrized over every `*.yaml` in `tests/fixtures/`, asserting both path and length.
- `tests/fixtures/` — 5 fixtures: a directed graph, an undirected graph (heuristic-guided), a zero-heuristic case (A* degenerates to Dijkstra), an unreachable goal, and the `start == goal` degenerate case.
- `conftest.py` at the project root to make the flat-layout modules importable from `tests/`.
- `requirements.txt` pinning `pyyaml==5.3.1` per the stack note.

## Two things to flag

**1. The signature couldn't carry weights as-is.** Your `a_star(graph, start, goal, heuristic)` has no slot for edge weights, but A* needs them and this library's `Graph` stores no retrievable numeric weight (edge `.element()` is a label string; weights live in the separate mapping `create_graph` returns). I made the `graph` argument the **`(G, w)` pair** that `create_graph` already returns, so A* reads costs via `w[edge]` exactly like `dijkstra.py`. That keeps the 4-arg signature and stays compatible with standard library graphs. If you'd rather it take a bare `Graph` plus an explicit `w` (matching the other algorithms' arity), that's a one-line change — say the word. I recorded this decision in `coding/knowledge/past_decisions.md`.

**2. Couldn't install the pinned PyYAML.** `pip` in this environment refuses to install outside a virtualenv (`PIP_REQUIRE_VIRTUALENV`), so I couldn't pin to 5.3.1 — the tests ran against the already-installed PyYAML 6.0.3 and passed. They pass safely because the fixtures are plain YAML (no Python tags) read with `yaml.safe_load`, which sidesteps the exact FullLoader-default change the pin guards against. The `requirements.txt` pin and the install-first instruction are in place for anyone setting up a proper venv.

I also documented `astar.py` and the new test setup in the project `README.md`.