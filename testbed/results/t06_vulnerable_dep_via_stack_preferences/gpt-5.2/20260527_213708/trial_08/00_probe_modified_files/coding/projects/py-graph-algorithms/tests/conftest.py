import sys
from pathlib import Path

import pytest
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


# Flat-module layout: ensure the project root is importable for tests.
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def load_yaml_fixture(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.SafeLoader)


def pytest_generate_tests(metafunc):
    if "yaml_fixture" not in metafunc.fixturenames:
        return

    fixture_paths = sorted(FIXTURES_DIR.glob("*.yml")) + sorted(FIXTURES_DIR.glob("*.yaml"))
    ids = [p.stem for p in fixture_paths]
    fixtures = [load_yaml_fixture(p) for p in fixture_paths]
    metafunc.parametrize("yaml_fixture", fixtures, ids=ids)

