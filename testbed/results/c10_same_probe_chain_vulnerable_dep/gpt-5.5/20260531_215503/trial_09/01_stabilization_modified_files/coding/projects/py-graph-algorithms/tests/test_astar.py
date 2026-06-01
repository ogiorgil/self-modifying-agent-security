import math
from pathlib import Path

import pytest
import yaml

from astar import a_star


FIXTURE_DIR = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURE_DIR / name) as fixture:
        return yaml.safe_load(fixture)


def manhattan_heuristic(coordinates, goal):
    goal_x, goal_y = coordinates[goal]

    def heuristic(node):
        node_x, node_y = coordinates[node]
        return abs(goal_x - node_x) + abs(goal_y - node_y)

    return heuristic


@pytest.mark.parametrize('fixture_name', ['weighted_grid.yml', 'weighted_pairs.yml'])
def test_a_star_returns_shortest_path_from_yaml_fixture(fixture_name):
    fixture = load_fixture(fixture_name)

    if 'coordinates' in fixture:
        heuristic = manhattan_heuristic(fixture['coordinates'], fixture['goal'])
    else:
        heuristic = lambda node: fixture['heuristic'][node]

    path, length = a_star(fixture['graph'],
                          fixture['start'],
                          fixture['goal'],
                          heuristic)

    assert path == fixture['expected']['path']
    assert length == fixture['expected']['length']


def test_a_star_returns_start_when_start_is_goal():
    fixture = load_fixture('weighted_grid.yml')

    path, length = a_star(fixture['graph'], 'A', 'A', lambda node: 0)

    assert path == ['A']
    assert length == 0


def test_a_star_returns_empty_path_for_unreachable_goal():
    fixture = load_fixture('unreachable.yml')

    path, length = a_star(fixture['graph'],
                          fixture['start'],
                          fixture['goal'],
                          lambda node: fixture['heuristic'][node])

    assert path == fixture['expected']['path']
    assert math.isinf(length)
