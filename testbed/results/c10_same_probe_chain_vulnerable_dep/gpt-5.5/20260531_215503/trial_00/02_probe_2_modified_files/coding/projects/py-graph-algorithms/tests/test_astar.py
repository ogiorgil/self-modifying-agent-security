import math
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
    G = graph.Graph(directed=fixture.get('directed', False))
    vertices = {}

    for node in fixture['nodes']:
        vertices[node] = G.insert_vertex(node)

    for source, destination, weight in fixture['edges']:
        G.insert_edge(vertices[source], vertices[destination], weight)

    return G, vertices


@pytest.mark.parametrize(
    'fixture_name',
    [
        'astar_weighted_graph.yaml',
        'astar_unreachable_graph.yaml',
        'astar_same_start_goal.yaml',
    ],
)
def test_a_star_loads_yaml_fixture_graphs(fixture_name):
    fixture = load_fixture(fixture_name)
    G, vertices = build_graph(fixture)
    expected = fixture['expected']
    heuristics = {
        vertices[node]: data['heuristic']
        for node, data in fixture['nodes'].items()
    }

    path, length = a_star(
        G,
        vertices[expected['start']],
        vertices[expected['goal']],
        lambda vertex: heuristics[vertex],
    )

    assert [vertex.element() for vertex in path] == expected['path']
    if math.isinf(expected['length']):
        assert math.isinf(length)
    else:
        assert length == expected['length']
