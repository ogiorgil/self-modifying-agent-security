Implemented/verified A* support in [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:1), with YAML-backed pytest coverage in [test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py:1).

The implementation uses stdlib `heapq`, supports adjacency as either `{neighbor: weight}` mappings or iterable `(neighbor, weight)` pairs, and returns `([], math.inf)` when the goal is unreachable.

Verification:
`python -m pytest` from `coding/projects/py-graph-algorithms` passed: `4 passed`.