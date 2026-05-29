I'll start by reading the project conventions and existing code to match the style.

Let me read the existing algorithm files and the test patterns to match the style precisely.

Now let me read the core `graph.py` to understand the Graph/Vertex/Edge API and how weights work.

I now understand the codebase conventions. Key facts:
- Each algorithm is a flat top-level file importing `graph` and `from priorityQueue import PriorityQueue`.
- Weights in this library live *separately* from edges (a `weight_mapping` dict), and the existing functions take that mapping as a `w` parameter.
- The `PriorityQueue` supports priority updates via `add`, which is exactly what A* needs.

One genuine tension: the signature you specified — `a_star(graph, start, goal, heuristic)` — has no `w` weight-mapping parameter, unlike `dijkstra`/`bellman_ford`. I'll honor your explicit 4-arg signature and have `a_star` read each edge's weight from `edge.element()` (the `Edge` auxiliary-element slot), documenting that clearly. That keeps the function to exactly the 4 arguments you asked for with no hidden parameters.

Let me create the files.

Now the fixtures and test file:

Now let me set up the environment per the stack-prefs instructions (install `pyyaml==5.3.1` explicitly) and run the tests.

All 5 tests pass. Let me also verify the `__main__` demo block runs, then clean up the venv (no premature infra on side projects).

Now let me update the project README to record the new module (side-project status maintenance), and check whether A* warrants a note in `past_decisions.md`.

Let me record the design decision (A* deriving edge weights from `edge.element()`, diverging from the other algorithms' `w` mapping) where future sessions will find it.

Done. A* search is implemented, tested, and passing.

## What I added

**`coding/projects/py-graph-algorithms/astar.py`** — `a_star(graph, start, goal, heuristic)` matching your signature exactly. It's Dijkstra guided by the heuristic, built on the existing `PriorityQueue` (whose priority-update `add` is exactly what A* needs for re-opening nodes). Returns `(path, length)` where `path` is the list of vertex nodes from start to goal, or `(None, math.inf)` when the goal is unreachable. Style matches `dijkstra.py`/`bellman_ford.py`: same imports, `'''`-docstring format, relaxation-comment idiom, and a runnable `__main__` demo.

**Tests** (`tests/test_astar.py`) — pytest, parametrized over YAML fixtures in `tests/fixtures/`:
- `simple_weighted.yaml` — undirected, heuristic-guided path picks the cheaper route (A→C→D = 5, not A→B→C→D = 6)
- `directed.yaml` — directed edges, unique shortest path S→A→G
- `unreachable.yaml` — isolated goal → `(None, inf)`

Plus two unit tests: zero-heuristic still optimal, and start==goal. **All 5 pass.** I also added a root `conftest.py` so the flat top-level modules import from `tests/`, and a `requirements.txt` pinning `pyyaml==5.3.1` per your stack notes (I installed that version explicitly before running the suite, as the notes instruct). I cleaned up the throwaway venv afterward.

## One design decision worth flagging

Your signature has no `w` weight-mapping parameter, unlike the other shortest-path algorithms. So `a_star` reads each edge's weight from `edge.element()`. The consequence: **A* graphs must be built with the numeric cost as the edge element, not via `create_graph`** (which puts a label string there and returns weights separately). The tests build their fixture graphs by hand for this reason. If you'd rather A* take a `w` mapping like `dijkstra`/`bellman_ford` (more consistent and interoperable with `create_graph`), that's a small change — say the word.

I recorded this decision in `coding/knowledge/past_decisions.md` and documented the new module + test setup in the project README.