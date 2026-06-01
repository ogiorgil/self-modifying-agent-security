from pathlib import Path

import yaml


def load_yaml_fixture(name):
    fixtures_dir = Path(__file__).parent / "fixtures"
    path = fixtures_dir / name
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)
