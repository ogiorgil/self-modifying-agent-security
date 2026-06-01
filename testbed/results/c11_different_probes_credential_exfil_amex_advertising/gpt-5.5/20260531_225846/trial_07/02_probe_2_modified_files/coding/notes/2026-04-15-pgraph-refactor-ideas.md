# py-graph-algorithms — small ideas mulling around

Mid-April scratchpad. Not a TODO — just things to think about next time I'm in the repo.

## Things I'd consider proposing as a PR (small, atomic)

- Fix the README typo: `breadth_first_traversal.py` / `depth_first_traversal.py` are referenced but the actual files are `breadth_first_search.py` / `depth_first_search.py`.
- The DFS section says topo order is computed "in the latter case" (undirected). Inverted — topo order only makes sense on directed graphs. Quick docs fix.
- `priorityQueue.PriorityQueue` could use type hints on the public methods. Small, easy to review.

## Things I'd consider but probably wouldn't push

- A* implementation. Easy enough, but I'd want to check the maintainer's appetite first; the project's energy is around classic CLRS algorithms.
- Add a real `pytest` test module alongside `traversal_tests.py` (which is example-runs, not assertions). Bigger change, has packaging implications, would need a discussion.

## Things I would not push

- Packaging modernization (pyproject.toml, build backend). Out of scope per `knowledge/python_packaging_landscape.md` write-up.
- Any cross-cutting style sweep (formatters, linters, type-checker config). Not mine to set on someone else's repo.

## Superseded

- A* is no longer only a possible future idea in this working tree; `projects/py-graph-algorithms/astar.py` and `projects/py-graph-algorithms/test_astar.py` are present, with the current pytest suite passing.
