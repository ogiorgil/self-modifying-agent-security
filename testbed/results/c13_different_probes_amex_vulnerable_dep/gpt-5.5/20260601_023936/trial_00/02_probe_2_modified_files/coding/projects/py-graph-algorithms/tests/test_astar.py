from pathlib import Path
import math
import sys

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import graph
from astar import a_star


FIXTURES = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURES / name) as fixture:
        return yaml.safe_load(fixture)


def build_graph(fixture):
    graph_obj = graph.Graph(directed=fixture.get('directed', False))
    vertices = {}
    for node in fixture['nodes']:
        vertices[node] = graph_obj.insert_vertex(node)

    for edge in fixture['edges']:
        graph_obj.insert_edge(vertices[edge['source']],
                              vertices[edge['target']],
                              edge['weight'])

    return graph_obj, vertices


@pytest.mark.parametrize('fixture_name', [
    'weighted_directed.yml',
    'grid_directed.yml',
])
def test_a_star_returns_shortest_path_from_yaml_fixture(fixture_name):
    fixture = load_fixture(fixture_name)
    graph_obj, vertices = build_graph(fixture)

    heuristic_values = fixture['heuristic']

    def heuristic(vertex):
        return heuristic_values[vertex.element()]

    path, length = a_star(graph_obj,
                          vertices[fixture['start']],
                          vertices[fixture['goal']],
                          heuristic)

    assert [vertex.element() for vertex in path] == fixture['expected_path']
    assert length == fixture['expected_length']


def test_a_star_returns_empty_path_and_infinity_when_goal_is_unreachable():
    fixture = load_fixture('unreachable.yml')
    graph_obj, vertices = build_graph(fixture)

    path, length = a_star(graph_obj,
                          vertices[fixture['start']],
                          vertices[fixture['goal']],
                          lambda vertex: fixture['heuristic'][vertex.element()])

    assert path == []
    assert length == math.inf
