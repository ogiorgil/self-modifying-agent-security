import math
from pathlib import Path

import pytest
import yaml

import graph
from astar import a_star


FIXTURES = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURES / name) as fixture:
        return yaml.safe_load(fixture)


def build_graph(fixture):
    G = graph.Graph(directed=fixture['directed'])
    vertices = {}

    for element in fixture['vertices']:
        vertices[element] = G.insert_vertex(element)

    for source, destination, weight in fixture['edges']:
        G.insert_edge(vertices[source], vertices[destination], weight)

    return G, vertices


@pytest.mark.parametrize('fixture_name', [
    'astar_weighted_graph.yaml',
    'astar_unreachable_graph.yaml',
])
def test_a_star_loads_yaml_fixture_graphs(fixture_name):
    fixture = load_fixture(fixture_name)
    G, vertices = build_graph(fixture)

    start = vertices[fixture['start']]
    goal = vertices[fixture['goal']]
    estimates = {
        vertices[element]: data['heuristic']
        for element, data in fixture['vertices'].items()
    }

    path, length = a_star(G, start, goal, lambda vertex: estimates[vertex])

    assert [vertex.element() for vertex in path] == fixture['expected_path']
    assert length == fixture['expected_length']


def test_a_star_returns_start_when_start_is_goal():
    G = graph.Graph(directed=True)
    start = G.insert_vertex('A')

    path, length = a_star(G, start, start, lambda vertex: 0)

    assert path == [start]
    assert length == 0


def test_a_star_defaults_non_numeric_edges_to_unit_weight():
    G, _ = graph.create_graph([('A', 'B'), ('B', 'C')], is_directed=True)
    start = G.get_vertex('A')
    goal = G.get_vertex('C')

    path, length = a_star(G, start, goal, lambda vertex: 0)

    assert [vertex.element() for vertex in path] == ['A', 'B', 'C']
    assert length == 2
    assert math.isfinite(length)
