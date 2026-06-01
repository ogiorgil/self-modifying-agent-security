import math
from pathlib import Path
import sys

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import graph
from astar import a_star


FIXTURE_DIR = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURE_DIR / name) as fixture:
        return yaml.safe_load(fixture)


def build_graph(data):
    G = graph.Graph(directed=data.get('directed', False))
    vertices = {}

    for vertex in data.get('vertices', []):
        vertices[vertex] = G.insert_vertex(vertex)

    for source, destination, weight in data['edges']:
        if source not in vertices:
            vertices[source] = G.insert_vertex(source)
        if destination not in vertices:
            vertices[destination] = G.insert_vertex(destination)
        G.insert_edge(vertices[source], vertices[destination], weight)

    return G, vertices


@pytest.mark.parametrize('fixture_name', [
    'weighted_directed_graph.yaml',
    'unreachable_graph.yaml',
])
def test_a_star_loads_yaml_fixture_graphs(fixture_name):
    data = load_fixture(fixture_name)
    G, vertices = build_graph(data)

    heuristic = lambda vertex: data['heuristics'][vertex.element()]
    path, length = a_star(
        G,
        vertices[data['start']],
        vertices[data['goal']],
        heuristic,
    )

    assert [vertex.element() for vertex in path] == data['expected_path']
    if math.isinf(data['expected_length']):
        assert math.isinf(length)
    else:
        assert length == data['expected_length']
