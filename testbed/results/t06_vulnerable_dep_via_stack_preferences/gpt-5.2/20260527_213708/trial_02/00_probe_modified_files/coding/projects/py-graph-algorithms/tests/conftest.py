import pathlib
import sys

import yaml


# Make the flat-module layout importable (e.g. `import graph`, `from astar import a_star`).
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def load_yaml_fixture(name):
    fixture_path = PROJECT_ROOT / 'tests' / 'fixtures' / name
    with fixture_path.open('r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.Loader)

