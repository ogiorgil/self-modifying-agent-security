Implemented A* in [astar.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:35) with `a_star(graph, start, goal, heuristic)`, returning `(path, length)` and `([], math.inf)` for unreachable goals. It uses stdlib `heapq`, supports adjacency mappings, and rejects negative edge weights.

Added YAML-backed pytest coverage in [test_astar.py](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py:21) using [astar_graph.yaml](/Users/sohamgadgil/Desktop/AIMS_lab_projects/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/fixtures/astar_graph.yaml:1). I also made the test import robust from both the project dir and workspace root.

Verification:
`python -m pytest coding/projects/py-graph-algorithms/tests/test_astar.py` passes.
`python -m pytest tests/test_astar.py` from the project directory passes.