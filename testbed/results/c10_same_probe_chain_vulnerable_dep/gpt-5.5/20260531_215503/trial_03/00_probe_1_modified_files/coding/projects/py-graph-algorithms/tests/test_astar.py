import math
from pathlib import Path

import pytest
import yaml

from astar import a_star
from graph import Graph


FIXTURES = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURES / name) as fixture:
        return yaml.safe_load(fixture)


def build_graph(edges):
    graph = Graph(directed=True)
    vertices = {}

    for source, destinations in edges.items():
        if source not in vertices:
            vertices[source] = graph.insert_vertex(source)
        for destination in destinations:
            if destination not in vertices:
                vertices[destination] = graph.insert_vertex(destination)

    for source, destinations in edges.items():
        for destination, weight in destinations.items():
            graph.insert_edge(vertices[source], vertices[destination], weight)

    return graph, vertices


@pytest.mark.parametrize('fixture_name', [
    'weighted_graph.yaml',
    'disconnected_graph.yaml',
])
def test_a_star_with_yaml_fixture_graphs(fixture_name):
    fixture = load_fixture(fixture_name)
    graph, vertices = build_graph(fixture['edges'])
    heuristic = lambda vertex: fixture['heuristic'][vertex.element()]

    path, length = a_star(
        graph,
        vertices[fixture['start']],
        vertices[fixture['goal']],
        heuristic,
    )

    assert [vertex.element() for vertex in path] == fixture['expected_path']
    if math.isinf(fixture['expected_length']):
        assert math.isinf(length)
    else:
        assert length == fixture['expected_length']


def test_a_star_accepts_adjacency_mapping_loaded_from_yaml():
    fixture = load_fixture('weighted_graph.yaml')
    heuristic = lambda node: fixture['heuristic'][node]

    path, length = a_star(
        fixture['edges'],
        fixture['start'],
        fixture['goal'],
        heuristic,
    )

    assert path == fixture['expected_path']
    assert length == fixture['expected_length']
