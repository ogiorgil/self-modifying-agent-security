from pathlib import Path

import pytest
import yaml

import graph
from astar import a_star


FIXTURES = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with (FIXTURES / name).open() as fixture:
        return yaml.safe_load(fixture)


def build_graph(fixture):
    G = graph.Graph(directed=fixture['directed'])
    vertices = {}
    for source, destination, weight in fixture['edges']:
        if source not in vertices:
            vertices[source] = G.insert_vertex(source)
        if destination not in vertices:
            vertices[destination] = G.insert_vertex(destination)
        source_vertex = vertices[source]
        destination_vertex = vertices[destination]
        G.insert_edge(source_vertex, destination_vertex, weight)
    return G, vertices


@pytest.mark.parametrize('fixture_name', [
    'grid_graph.yaml',
    'unreachable_graph.yaml',
])
def test_a_star_loads_yaml_fixture_graphs(fixture_name):
    fixture = load_fixture(fixture_name)
    G, vertices = build_graph(fixture)

    start = vertices[fixture['start']]
    goal = vertices[fixture['goal']]

    def heuristic(vertex):
        return fixture['heuristic'][vertex.element()]

    path, length = a_star(G, start, goal, heuristic)

    assert [vertex.element() for vertex in path] == fixture['expected_path']
    assert length == fixture['expected_length']


def test_a_star_returns_start_for_zero_length_path():
    fixture = load_fixture('grid_graph.yaml')
    G, vertices = build_graph(fixture)
    start = vertices[fixture['start']]

    path, length = a_star(G, start, start, lambda vertex: 0)

    assert [vertex.element() for vertex in path] == [fixture['start']]
    assert length == 0
