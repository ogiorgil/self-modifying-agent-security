import math
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parents[1]))

from astar import a_star


def load_fixture(name):
    '''
    Load a YAML graph fixture from tests/fixtures.
    '''
    fixture_path = Path(__file__).parent / 'fixtures' / name
    with fixture_path.open() as fixture_file:
        return yaml.safe_load(fixture_file)


def test_a_star_finds_shortest_path_from_yaml_fixture():
    fixture = load_fixture('astar_graph.yaml')

    path, length = a_star(
        fixture['graph'],
        fixture['start'],
        fixture['goal'],
        lambda node: fixture['heuristic'][node],
    )

    assert path == fixture['expected_path']
    assert length == fixture['expected_length']


def test_a_star_returns_empty_path_for_unreachable_goal_from_yaml_fixture():
    fixture = load_fixture('astar_graph.yaml')

    path, length = a_star(
        fixture['graph'],
        fixture['start'],
        fixture['unreachable_goal'],
        lambda node: fixture['heuristic'][node],
    )

    assert path == []
    assert math.isinf(length)
