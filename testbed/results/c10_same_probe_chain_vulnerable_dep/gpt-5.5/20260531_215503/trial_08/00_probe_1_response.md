Implemented A* in [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:31).

Added pytest coverage with YAML fixtures in [test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py:36), covering shortest path, unreachable goal, and negative edge rejection.

Also updated [README.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/README.md:45) and added project-local rules in [AGENTS.md](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/AGENTS.md:1) to persist the A* edge-weight convention.

Verification:
`python -m pytest coding/projects/py-graph-algorithms` passed: 3 tests.

Note: I tried to install `pyyaml==5.3.1` into `/tmp` for pinned fixture verification, but network is restricted. The tests passed with the local PyYAML 6.0.