from pathlib import Path

import yaml

from astar import a_star


FIXTURES_DIR = Path(__file__).resolve().parent / 'fixtures'


def _load_yaml_fixture(name):
    path = FIXTURES_DIR / name
    with path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def _heuristic_from_mapping(h_map):
    def h(node):
        return h_map[node]

    return h


def test_astar_simple_directed_fixture():
    data = _load_yaml_fixture('simple_directed.yaml')
    path, length = a_star(
        graph=data['graph'],
        start=data['start'],
        goal=data['goal'],
        heuristic=_heuristic_from_mapping(data['heuristic']),
    )
    assert path == data['expected_path']
    assert length == data['expected_length']


def test_astar_two_paths_fixture():
    data = _load_yaml_fixture('two_paths.yaml')
    path, length = a_star(
        graph=data['graph'],
        start=data['start'],
        goal=data['goal'],
        heuristic=_heuristic_from_mapping(data['heuristic']),
    )
    assert path == data['expected_path']
    assert length == data['expected_length']


def test_astar_unreachable_fixture():
    data = _load_yaml_fixture('unreachable.yaml')
    path, length = a_star(
        graph=data['graph'],
        start=data['start'],
        goal=data['goal'],
        heuristic=_heuristic_from_mapping(data['heuristic']),
    )
    assert path is None
    assert length == float('inf')

