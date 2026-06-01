import math
import pathlib
import sys

import pytest
import yaml

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import graph
from astar import a_star


FIXTURE_DIR = pathlib.Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURE_DIR / name) as fixture_file:
        return yaml.safe_load(fixture_file)


def create_weighted_graph(fixture):
    G = graph.Graph(directed=fixture.get('directed', False))

    for source, destination, weight in fixture['edges']:
        try:
            source_vertex = G.insert_vertex(source)
        except Exception:
            source_vertex = G.get_vertex(source)

        try:
            destination_vertex = G.insert_vertex(destination)
        except Exception:
            destination_vertex = G.get_vertex(destination)

        G.insert_edge(source_vertex, destination_vertex, weight)

    return G


@pytest.mark.parametrize('fixture_name', [
    'astar_weighted.yaml',
    'astar_unreachable.yaml',
])
def test_a_star_from_yaml_fixture(fixture_name):
    fixture = load_fixture(fixture_name)
    G = create_weighted_graph(fixture)
    start = G.get_vertex(fixture['start'])
    goal = G.get_vertex(fixture['goal'])
    estimates = fixture['heuristic']

    def heuristic(vertex):
        return estimates[vertex.element()]

    path, length = a_star(G, start, goal, heuristic)

    assert [vertex.element() for vertex in path] == fixture['expected_path']
    if math.isinf(fixture['expected_length']):
        assert math.isinf(length)
    else:
        assert length == fixture['expected_length']


def test_a_star_returns_start_for_same_start_and_goal():
    G = graph.Graph()
    start = G.insert_vertex('s')

    path, length = a_star(G, start, start, lambda vertex: 0)

    assert path == [start]
    assert length == 0
