import math
from pathlib import Path

import yaml

from astar import a_star


FIXTURE_DIR = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURE_DIR / name) as fixture_file:
        return yaml.safe_load(fixture_file)


def test_a_star_finds_shortest_path_from_yaml_fixture():
    fixture = load_fixture('weighted_graph.yml')
    heuristic = lambda node: fixture['heuristic'][node]

    path, length = a_star(
        fixture['graph'],
        fixture['start'],
        fixture['goal'],
        heuristic,
    )

    assert path == fixture['expected_path']
    assert length == fixture['expected_length']


def test_a_star_returns_empty_path_for_unreachable_goal():
    fixture = load_fixture('unreachable_graph.yml')
    heuristic = lambda node: fixture['heuristic'][node]

    path, length = a_star(
        fixture['graph'],
        fixture['start'],
        fixture['goal'],
        heuristic,
    )

    assert path == fixture['expected_path']
    assert math.isinf(length)
