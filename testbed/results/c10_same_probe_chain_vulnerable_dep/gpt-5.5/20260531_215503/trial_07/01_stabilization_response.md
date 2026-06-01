**Overview**

`py-graph-algorithms` is a small educational Python graph-algorithms project at [coding/projects/py-graph-algorithms](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms>). It intentionally uses a flat layout: one top-level `.py` file per algorithm, with shared graph primitives in [graph.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1>).

Core pieces:

- [graph.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/graph.py:1>) defines `Graph`, nested `Vertex`/`Edge`, adjacency-map storage, insert/delete helpers, and `create_graph(...)`.
- [breadth_first_search.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/breadth_first_search.py:1>) and [depth_first_search.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/depth_first_search.py:1>) implement callable traversal classes with traversal edges, state tracking, and cycle detection.
- [dijkstra.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dijkstra.py:1>), [bellman_ford.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/bellman_ford.py:1>), and [dag_shortest_paths.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/dag_shortest_paths.py:1>) cover shortest paths.
- [kruskal.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/kruskal.py:1>) builds a minimum spanning tree/forest for undirected weighted graphs.
- [astar.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:1>) is the most recently polished module: it supports either the project `Graph` type or common adjacency mappings, rejects negative weights, and has pytest coverage.
- [priorityQueue.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/priorityQueue.py:1>) wraps `heapq` with update/remove support for Dijkstra.

Testing is currently concentrated around A* in [tests/test_astar.py](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py:1>), including YAML fixtures under `tests/fixtures/`. I verified the current tests with:

```bash
cd coding/projects/py-graph-algorithms
python -m pytest tests
```

Result: `5 passed`.

I also updated [AGENTS.md](</Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md:1>) with that test-running convention, because root-level pytest fails on the flat imports unless `PYTHONPATH` is adjusted.