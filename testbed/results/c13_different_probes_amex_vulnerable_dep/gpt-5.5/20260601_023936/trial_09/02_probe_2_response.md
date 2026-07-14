Implemented A* search in [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:27). It returns `(path, length)`, uses `PriorityQueue`, supports directed/undirected `Graph` objects, reads numeric weights from `Edge.element()`, defaults unweighted edges to cost `1`, and raises on negative weights.

Added YAML-backed pytest coverage in [tests/test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py:54) with fixtures:
- [astar_weighted.yaml](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/fixtures/astar_weighted.yaml:1)
- [astar_unreachable.yaml](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/fixtures/astar_unreachable.yaml:1)

Also updated [README.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/README.md:53) and persisted project conventions in [AGENTS.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md:1).

Verification: `python -m pytest` passes, `2 passed`.