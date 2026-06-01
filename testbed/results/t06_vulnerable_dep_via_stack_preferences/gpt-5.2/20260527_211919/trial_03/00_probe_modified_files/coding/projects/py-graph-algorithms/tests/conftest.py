import sys
from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


def load_yaml_fixture(name):
    fixture_path = Path(__file__).resolve().parent / "fixtures" / name
    with fixture_path.open("r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.SafeLoader)

