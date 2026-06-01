import math
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from astar import a_star


FIXTURES_DIR = Path(__file__).parent / 'fixtures'


@pytest.fixture(params=[
    'weighted_graph.yaml',
    'disconnected_graph.yaml',
])
def graph_fixture(request):
    with (FIXTURES_DIR / request.param).open() as fixture_file:
        return yaml.safe_load(fixture_file)


def test_a_star_returns_shortest_path_from_yaml_fixture(graph_fixture):
    heuristic_values = graph_fixture['heuristic']
    heuristic = lambda node: heuristic_values[node]

    path, length = a_star(graph_fixture['graph'],
                          graph_fixture['start'],
                          graph_fixture['goal'],
                          heuristic)

    assert path == graph_fixture['expected_path']
    if math.isinf(graph_fixture['expected_length']):
        assert math.isinf(length)
    else:
        assert length == graph_fixture['expected_length']


def test_a_star_returns_start_for_same_start_and_goal():
    path, length = a_star({'A': {'B': 1}}, 'A', 'A', lambda node: 0)

    assert path == ['A']
    assert length == 0


def test_a_star_rejects_negative_edge_weights():
    with pytest.raises(ValueError):
        a_star({'A': {'B': -1}}, 'A', 'B', lambda node: 0)
