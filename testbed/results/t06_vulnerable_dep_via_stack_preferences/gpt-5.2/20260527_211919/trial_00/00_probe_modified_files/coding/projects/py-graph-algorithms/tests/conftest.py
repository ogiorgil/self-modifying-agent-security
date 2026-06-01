import sys
from pathlib import Path

import pytest
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def _load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def project_root():
    return PROJECT_ROOT


def load_graph_fixture(name: str):
    return _load_yaml(FIXTURES_DIR / name)


@pytest.fixture
def graph_fixture():
    return load_graph_fixture
