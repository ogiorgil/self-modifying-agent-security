from pathlib import Path

import yaml


FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def load_yaml_fixture(name: str):
    path = FIXTURES_DIR / f"{name}.yml"
    with path.open("r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.Loader)
