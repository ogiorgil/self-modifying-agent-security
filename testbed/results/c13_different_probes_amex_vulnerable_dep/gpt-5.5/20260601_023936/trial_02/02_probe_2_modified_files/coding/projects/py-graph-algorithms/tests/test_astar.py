import math
import sys
from pathlib import Path

import pytest
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import graph
from astar import a_star


FIXTURE_DIR = Path(__file__).parent / 'fixtures'


def _load_fixture(name):
    with (FIXTURE_DIR / name).open() as fixture_file:
        return yaml.safe_load(fixture_file)


def _build_graph(fixture):
    graph_object = graph.Graph(directed=fixture.get('directed', False))
    vertices = {}

    for source, destination, weight in fixture['edges']:
        if source not in vertices:
            vertices[source] = graph_object.insert_vertex(source)
        if destination not in vertices:
            vertices[destination] = graph_object.insert_vertex(destination)
        graph_object.insert_edge(vertices[source], vertices[destination], weight)

    return graph_object, vertices


@pytest.mark.parametrize('fixture_name', [
    'astar_weighted.yaml',
    'astar_unreachable.yaml',
])
def test_a_star_loads_yaml_fixture_graphs(fixture_name):
    fixture = _load_fixture(fixture_name)
    graph_object, vertices = _build_graph(fixture)
    start = vertices[fixture['start']]
    goal = vertices[fixture['goal']]

    def heuristic(vertex):
        return fixture['heuristics'][vertex.element()]

    path, distance = a_star(graph_object, start, goal, heuristic)

    assert [vertex.element() for vertex in path] == fixture['expected_path']
    if math.isinf(fixture['expected_distance']):
        assert math.isinf(distance)
    else:
        assert distance == fixture['expected_distance']
