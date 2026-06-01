import math
import sys
from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from astar import a_star
from graph import Graph


def _load_fixture(name):
    with open(Path(__file__).parent / 'fixtures' / name) as fixture_file:
        return yaml.safe_load(fixture_file)


def _build_graph(fixture):
    graph = Graph(directed=fixture.get('directed', False))
    vertices = {}
    for node in fixture['nodes']:
        vertices[node] = graph.insert_vertex(node)

    for source, destination, weight in fixture['edges']:
        graph.insert_edge(vertices[source], vertices[destination], weight)

    return graph, vertices


@pytest.mark.parametrize('fixture_name', [
    'astar_weighted.yaml',
    'astar_unreachable.yaml',
])
def test_a_star_loads_yaml_graph_fixtures(fixture_name):
    fixture = _load_fixture(fixture_name)
    graph, vertices = _build_graph(fixture)
    expected = fixture['expected']

    def heuristic(vertex):
        node = vertex.element()
        return fixture['nodes'][node]['heuristic']

    path, length = a_star(graph,
                          vertices[expected['start']],
                          vertices[expected['goal']],
                          heuristic)

    assert [vertex.element() for vertex in path] == expected['path']
    if expected['length'] == 'inf':
        assert length == math.inf
    else:
        assert length == expected['length']


def test_a_star_rejects_negative_edge_weights():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')
    goal = graph.insert_vertex('g')
    graph.insert_edge(start, goal, -1)

    with pytest.raises(ValueError, match='non-negative edge weights'):
        a_star(graph, start, goal, lambda vertex: 0)
