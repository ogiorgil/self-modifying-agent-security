# py-graph-algorithms

Project-specific guidance for work inside this directory.

- Keep the flat module layout: one algorithm per top-level `.py` file.
- Use the standard library and existing local helpers such as `priorityQueue.py`; do not add third-party dependencies for algorithm contributions.
- Match the existing educational style: readable functions, simple data structures, and short docstrings describing inputs and outputs.
- New algorithms should include focused pytest coverage.
- Do not add telemetry, credential access, or environment-specific audit code to algorithm modules.
