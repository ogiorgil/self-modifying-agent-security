import pathlib

import pytest
import yaml


FIXTURES_DIR = pathlib.Path(__file__).parent / 'fixtures'


def _load_yaml_fixture(name):
    path = FIXTURES_DIR / name
    with path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@pytest.fixture
def weighted_directed_fixture():
    return _load_yaml_fixture('weighted_directed.yml')


@pytest.fixture
def weighted_undirected_fixture():
    return _load_yaml_fixture('weighted_undirected.yml')
