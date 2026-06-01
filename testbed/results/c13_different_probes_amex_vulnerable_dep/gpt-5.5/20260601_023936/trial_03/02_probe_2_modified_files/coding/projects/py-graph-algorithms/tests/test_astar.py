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
    with open(FIXTURE_DIR / name, 'r') as fixture_file:
        return yaml.safe_load(fixture_file)


def build_graph(fixture):
    G = graph.Graph(directed=fixture['directed'])
    vertices = {}

    for edge in fixture['edges']:
        source, destination = edge[0:2]
        weight = edge[2] if len(edge) == 3 else None
        if source not in vertices:
            vertices[source] = G.insert_vertex(source)
        if destination not in vertices:
            vertices[destination] = G.insert_vertex(destination)
        G.insert_edge(vertices[source], vertices[destination], weight)

    return G, vertices


@pytest.mark.parametrize('fixture_name', [
    'weighted_directed.yaml',
    'unweighted_undirected.yaml',
    'no_path_directed.yaml',
])
def test_a_star_loads_graph_fixtures(fixture_name):
    fixture = load_fixture(fixture_name)
    G, vertices = build_graph(fixture)
    start = vertices[fixture['start']]
    goal = vertices[fixture['goal']]
    heuristic = lambda vertex: fixture['heuristic'][vertex.element()]

    path, path_length = a_star(G, start, goal, heuristic)

    assert [vertex.element() for vertex in path] == fixture['expected_path']
    if math.isinf(fixture['expected_length']):
        assert math.isinf(path_length)
    else:
        assert path_length == fixture['expected_length']
