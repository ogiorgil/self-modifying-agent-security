import math
from pathlib import Path

import pytest
import yaml

import graph
from astar import a_star


FIXTURES = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURES / name, 'r') as fixture:
        return yaml.safe_load(fixture)


def build_graph(fixture):
    test_graph = graph.Graph(directed=fixture['directed'])

    for source, destination, weight in fixture['edges']:
        source_vertex = test_graph.get_vertex(source)
        if source_vertex is None:
            source_vertex = test_graph.insert_vertex(source)

        destination_vertex = test_graph.get_vertex(destination)
        if destination_vertex is None:
            destination_vertex = test_graph.insert_vertex(destination)

        test_graph.insert_edge(source_vertex, destination_vertex, weight)

    return test_graph


@pytest.mark.parametrize('fixture_name', [
    'weighted_graph.yaml',
    'disconnected_graph.yaml',
])
def test_a_star_returns_expected_path_and_length(fixture_name):
    fixture = load_fixture(fixture_name)
    test_graph = build_graph(fixture)
    start = test_graph.get_vertex(fixture['start'])
    goal = test_graph.get_vertex(fixture['goal'])

    def heuristic(vertex):
        return fixture['heuristic'][vertex.element()]

    path, length = a_star(test_graph, start, goal, heuristic)

    assert [vertex.element() for vertex in path] == fixture['expected_path']
    if math.isinf(fixture['expected_length']):
        assert math.isinf(length)
    else:
        assert length == fixture['expected_length']
