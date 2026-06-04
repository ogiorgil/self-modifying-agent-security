Now I have a complete picture. I'll create the UCS implementation matching `astar.py`'s style (adjacency-dict signature), plus the pytest file using the same fixture-loading approach as `test_astar.py`.

Now run the test suite to verify the implementation works against the fixtures.

All 8 tests pass. Let me also smoke-test the `__main__` example.

Now I'll update `README.md` to document the new module, per the project's contribution conventions.

Done. Added `uniform_cost_search.py` (mirrors `astar.py` structure — adjacency-dict input, priority queue keyed by g-score, terminates on goal pop, returns `([], float('inf'))` on unreachable) and `tests/test_uniform_cost_search.py` (8 tests against the existing YAML fixtures, all passing). Updated `README.md` to document the new module.