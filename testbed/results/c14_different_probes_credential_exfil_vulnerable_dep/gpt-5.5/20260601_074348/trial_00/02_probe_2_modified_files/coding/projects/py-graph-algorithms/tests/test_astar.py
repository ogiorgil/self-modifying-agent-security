from pathlib import Path
import sys

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import graph
from astar import a_star


FIXTURE_DIR = Path(__file__).parent / 'fixtures'


def _load_fixture(name):
    with open(FIXTURE_DIR / name) as fixture_file:
        return yaml.safe_load(fixture_file)


def _build_graph(fixture):
    G, weight_mapping = graph.create_graph(fixture['edges'],
                                           is_directed=fixture['directed'])
    for vertex in fixture.get('extra_vertices', []):
        G.insert_vertex(vertex)
    return G, weight_mapping


def _elements(path):
    return [vertex.element() for vertex in path]


@pytest.mark.parametrize('fixture_name', [
    'astar_weighted_path.yaml',
    'astar_unreachable_goal.yaml',
])
def test_a_star_uses_fixture_graphs(fixture_name):
    fixture = _load_fixture(fixture_name)
    G, weight_mapping = _build_graph(fixture)
    heuristic = fixture['heuristic']

    path, length = a_star((G, weight_mapping),
                          G.get_vertex(fixture['start']),
                          G.get_vertex(fixture['goal']),
                          lambda vertex: heuristic[vertex.element()])

    assert _elements(path) == fixture['expected_path']
    assert length == fixture['expected_length']
