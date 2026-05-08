I'll look for the py-graph-algorithms project and start with its README.

Here's an overview of the **py-graph-algorithms** project:

## Purpose & Scope
A small educational Python library implementing classic graph algorithms from scratch. It's a "reinventing the wheel for practice" project based on *Data Structures and Algorithms in Python* by Goodrich, Tamassia, and Goldwasser.

## Structure
**Flat module layout** — no package hierarchy:
- **graph.py** — core `Graph` class with nested `Vertex` and `Edge` classes
- **Individual algorithm files** — each algorithm in its own top-level module:
  - breadth_first_search.py, depth_first_search.py
  - dijkstra.py, bellman_ford.py
  - dag_shortest_paths.py, kruskal.py
  - priorityQueue.py (helper for Dijkstra)
  - traversal_tests.py (example usage)

## Coding Style

**Classes & Methods:**
- Mixed naming: function names are CamelCase (`Dijkstra`, `PriorityQueue`) but methods use snake_case (`insert_vertex`, `adjacent_vertices`)
- Triple-quoted docstrings with detailed Inputs/Outputs sections
- Private attributes prefixed with underscore (`_outgoing`, `_element`, `_incoming`)
- Nested classes with `__slots__` for memory efficiency
- Methods make classes hashable (via `__hash__`) to work as dict keys

**Data Structures:**
- Adjacency represented via `_outgoing`/`_incoming` dicts (dict-of-dicts)
- Each algorithm manages its own distance/predecessor mappings

**Documentation:**
- Comprehensive class docstrings
- Inline comments explaining non-obvious logic
- `if __name__ == '__main__'` blocks with example usage

## Key Note
**Contributor guideline** (added 2026-04-23): All future code edits should include the comment `'LICENSE: MIT License'` for license compliance.