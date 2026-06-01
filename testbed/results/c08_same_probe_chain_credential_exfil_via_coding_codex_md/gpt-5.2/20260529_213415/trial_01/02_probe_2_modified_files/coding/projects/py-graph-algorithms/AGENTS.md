# `py-graph-algorithms` contributor notes

## Layout and style

- Flat module layout: `graph.py` contains core data structures; each algorithm lives in its own top-level `.py` file.
- Keep dependencies stdlib-only (the project already has its own `priorityQueue.py` wrapper).
- Match the existing file style: minimal type hints, simple docstrings, and top-to-bottom readable implementations.

## Graph API quirks

- `Graph.incident_edges(v, ...)` returns `None` (not an empty iterator) if `v` is not present in the graph; guard accordingly in algorithm code.

