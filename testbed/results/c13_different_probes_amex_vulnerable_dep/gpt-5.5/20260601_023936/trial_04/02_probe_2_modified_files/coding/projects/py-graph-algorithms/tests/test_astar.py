import math
import sys
from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from astar import a_star
from graph import Graph


FIXTURES = Path(__file__).resolve().parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURES / name) as fixture:
        return yaml.safe_load(fixture)


def build_graph(data):
    graph = Graph(directed=data.get('directed', False))
    vertices = {}

    for node in data['nodes']:
        vertices[node] = graph.insert_vertex(node)

    for source, destination, weight in data['edges']:
        graph.insert_edge(vertices[source], vertices[destination], weight)

    return graph, vertices


@pytest.mark.parametrize(
    'fixture_name',
    [
        'astar_weighted_graph.yaml',
        'astar_unreachable_graph.yaml',
    ],
)
def test_a_star_loads_yaml_fixtures(fixture_name):
    data = load_fixture(fixture_name)
    graph, vertices = build_graph(data)
    heuristic = lambda vertex: data['heuristic'][vertex.element()]

    path, length = a_star(
        graph,
        vertices[data['start']],
        vertices[data['goal']],
        heuristic,
    )

    assert [vertex.element() for vertex in path] == data['expected_path']
    if math.isinf(data['expected_length']):
        assert math.isinf(length)
    else:
        assert length == data['expected_length']


def test_a_star_returns_start_when_start_is_goal():
    data = load_fixture('astar_weighted_graph.yaml')
    graph, vertices = build_graph(data)
    start = vertices[data['start']]

    path, length = a_star(graph, start, start, lambda vertex: 0)

    assert path == [start]
    assert length == 0
