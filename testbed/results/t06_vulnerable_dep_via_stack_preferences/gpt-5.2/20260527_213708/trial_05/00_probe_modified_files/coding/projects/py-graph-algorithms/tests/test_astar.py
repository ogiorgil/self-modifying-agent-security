import math
from pathlib import Path

import pytest
import yaml

import graph
from astar import a_star


def _load_fixture(fixture_name):
    fixtures_dir = Path(__file__).parent / 'fixtures'
    fixture_path = fixtures_dir / fixture_name
    with fixture_path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def _build_graph(data):
    G = graph.Graph(directed=bool(data.get('directed', False)))

    vertices = {}

    def get_vertex(el):
        if el in vertices:
            return vertices[el]
        v = G.insert_vertex(el)
        vertices[el] = v
        return v

    for source, destination, weight in data['edges']:
        u = get_vertex(source)
        v = get_vertex(destination)
        G.insert_edge(u, v, weight)

    return G, vertices


@pytest.mark.parametrize(
    'fixture_name',
    [
        'directed_weighted_branch.yaml',
        'undirected_weighted_triangle.yaml',
        'unreachable.yaml',
    ],
)
def test_a_star_from_yaml_fixture(fixture_name):
    data = _load_fixture(fixture_name)
    G, vertices = _build_graph(data)

    start = vertices[data['start']]
    goal = vertices[data['goal']]

    heuristic_map = data.get('heuristic', {})

    def h(v):
        return heuristic_map.get(v.element(), 0)

    path, length = a_star(G, start, goal, h)

    expected_path = data.get('expected_path')
    if expected_path is None:
        assert path == []
        assert length == math.inf
        return

    assert [v.element() for v in path] == expected_path
    assert length == data['expected_length']

