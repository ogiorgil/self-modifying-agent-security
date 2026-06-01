import math
import sys
from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import graph as graph_module
from astar import a_star


FIXTURE_DIR = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURE_DIR / name, 'r') as fixture_file:
        return yaml.safe_load(fixture_file)


def build_graph(data):
    graph = graph_module.Graph(directed=data.get('directed', False))
    vertices = {}

    for edge in data['edges']:
        for element in (edge['source'], edge['target']):
            if element not in vertices:
                vertices[element] = graph.insert_vertex(element)

    for edge in data['edges']:
        graph.insert_edge(vertices[edge['source']],
                          vertices[edge['target']],
                          edge.get('weight', 1))

    return graph, vertices


@pytest.mark.parametrize('fixture_name', [
    'weighted_directed.yaml',
    'disconnected.yaml',
])
def test_a_star_loads_yaml_fixtures(fixture_name):
    data = load_fixture(fixture_name)
    graph, vertices = build_graph(data)
    heuristic = lambda vertex: data['heuristic'][vertex.element()]

    path, length = a_star(graph,
                          vertices[data['start']],
                          vertices[data['goal']],
                          heuristic)

    assert [vertex.element() for vertex in path] == data['expected_path']
    assert length == data['expected_length']


def test_a_star_with_zero_heuristic_finds_shortest_path():
    data = load_fixture('weighted_directed.yaml')
    graph, vertices = build_graph(data)

    path, length = a_star(graph,
                          vertices[data['start']],
                          vertices[data['goal']],
                          lambda vertex: 0)

    assert [vertex.element() for vertex in path] == data['expected_path']
    assert length == 3


def test_a_star_defaults_to_unit_length_for_unweighted_edges():
    edges = [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'D')]
    graph, _ = graph_module.create_graph(edges, is_directed=True)

    path, length = a_star(graph,
                          graph.get_vertex('A'),
                          graph.get_vertex('D'),
                          lambda vertex: 0)

    assert [vertex.element() for vertex in path] == ['A', 'B', 'D']
    assert length == 2
    assert not math.isinf(length)
