import sys
from pathlib import Path

import pytest
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def pytest_configure():
    # Allow `import graph`, `import astar`, etc. from the flat-module project root.
    sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture
def load_yaml_fixture():
    def _load(name: str):
        path = FIXTURES_DIR / name
        with path.open("r", encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.Loader)

    return _load

