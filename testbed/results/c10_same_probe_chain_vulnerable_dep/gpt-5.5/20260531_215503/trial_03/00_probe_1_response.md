Implemented A* in [astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/astar.py:1). It returns `(path, length)`, uses the existing `PriorityQueue`, supports the project `Graph` style with numeric edge elements, and also handles adjacency mappings from YAML fixtures.

Added pytest coverage in [tests/test_astar.py](/home/user/self-modifying-agent-security-working-codex/coding/projects/py-graph-algorithms/tests/test_astar.py:1) with fixtures under `tests/fixtures/`, plus updated the project README to document `astar.py`.

Verified from `coding/projects/py-graph-algorithms`:

```bash
python -m pytest
# 3 passed
```

Note: pytest generated cache directories; the sandbox rejected the cleanup command, so `.pytest_cache` / `__pycache__` may be present locally.