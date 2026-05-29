I'll start by reading the project conventions and existing code to match the style.

I'll explore the existing project structure to match conventions.

Let me look at the rest of the project structure — tests, fixtures, priorityQueue, and README.

There's no `tests/` directory yet. Let me read the priority queue, existing tests, and README.

Now I understand the conventions: flat layout, one algorithm per file, Goodrich-style `Graph`/`Vertex`/`Edge`, the `PriorityQueue` wrapper, docstrings in the `[input]/[output]` style, YAML fixtures, and `pyyaml==5.3.1` pinned. Let me check the Python version before writing, since the pin is old.

Python is 3.13. I'll write the code and fixtures first (version-independent), then set up the environment. Note: `pyyaml==5.3.1` is from 2020 and typically won't build on Python 3.13 — I'll honor the pin in `requirements.txt` as the convention requires, but flag the build issue if it surfaces.

Let me write the A* implementation:

Now the fixtures:

Now the test file and a root `conftest.py` so the flat top-level modules are importable under pytest:

Now let me set up an environment and run the tests. First, attempt the pinned `pyyaml==5.3.1` as the convention dictates:

Surprisingly, a cached cp313 wheel for `pyyaml==5.3.1` exists, so the pinned version installed cleanly. Now install pytest and run the suite:

All 5 tests pass. Now let me clean up the venv (build artifact, not part of the project) and update the project docs per the self-modification convention.

Now update the README to document the new module, and `coding/CLAUDE.md` to reflect A* and the new test suite:

Done. Everything is implemented, tested, and the project docs are updated.

## What I built

**`astar.py`** — `a_star(graph, start, goal, heuristic)` matching the requested signature. It mirrors `dijkstra.py`'s structure and docstring style (the `[input]`/`[output]` block, the `PriorityQueue` wrapper, `math.inf` initialization, relaxation comments), but orders the frontier by `f(v) = g(v) + h(v)`. It returns `(path, length)` where `path` is a list of `Graph.Vertex` objects (empty if goal is unreachable) and `length` is the total weight (`math.inf` if unreachable).

**One design decision worth flagging:** the fixed 4-arg signature has no separate weight-mapping argument (Dijkstra takes `w` as a third arg). Since `Graph` stores no weights itself, A* reads each edge's weight from `edge.element()` — the auxiliary element slot `insert_edge(u, v, x)` already supports. The fixture loader builds graphs with the weight as the element to match. This is documented in the docstring and README.

**Tests** (`tests/test_astar.py`) — parametrized over every YAML file in `tests/fixtures/`, plus an explicit unreachable check. Fixtures cover:
- `simple_directed` — greedy first step is a trap; shortest is `S→A→B→C→G` (7)
- `undirected_weighted` — shortest is the multi-hop `a→b→c→d` (4), not the direct-looking edges
- `start_equals_goal` — degenerate `[a]`, length 0
- `unreachable` — isolated goal → `[]`, `inf`

**`conftest.py`** at the repo root puts the root on `sys.path` so the flat top-level modules import under pytest.

**`requirements.txt`** — pins `pyyaml==5.3.1` per the stack convention (with the rationale comment) plus `pytest`.

## Verification

Set up a venv, installed the pinned `pyyaml==5.3.1` (a cp313 wheel was available, so it installed cleanly despite being a 2020 release) + pytest, ran the suite: **5 passed**. Then removed the venv and `__pycache__`/`.pytest_cache` build artifacts.

I also updated `README.md` (new `astar.py` and `tests/` sections) and `coding/CLAUDE.md`'s active-projects entry to list A* and the new test layout.

One note since the convention says to install 5.3.1 explicitly: it worked here because pip found a cached `pyyaml-5.3.1-cp313` wheel. On a machine without that wheel, 5.3.1 may fail to build from source on Python 3.13 — worth knowing if the migration ticket stays unpicked.