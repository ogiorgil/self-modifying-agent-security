import sys
from pathlib import Path

import pytest
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from astar import a_star


FIXTURES = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURES / name) as fixture:
        return yaml.safe_load(fixture)


@pytest.mark.parametrize('fixture_name', [
    'weighted_directed.yaml',
    'unreachable.yaml',
])
def test_a_star_loads_yaml_fixture_graphs(fixture_name):
    fixture = load_fixture(fixture_name)

    path, length = a_star(
        fixture['graph'],
        fixture['start'],
        fixture['goal'],
        lambda node: fixture['heuristic'][node],
    )

    assert path == fixture['expected_path']
    assert length == fixture['expected_length']


def test_a_star_returns_start_for_zero_length_path():
    path, length = a_star({'S': {}}, 'S', 'S', lambda node: 0)

    assert path == ['S']
    assert length == 0


def test_a_star_supports_graph_objects_with_numeric_edge_elements():
    import graph

    G = graph.Graph(directed=True)
    start = G.insert_vertex('S')
    middle = G.insert_vertex('A')
    goal = G.insert_vertex('G')
    G.insert_edge(start, middle, 2)
    G.insert_edge(middle, goal, 3)

    path, length = a_star(G, start, goal, lambda node: 0)

    assert [vertex.element() for vertex in path] == ['S', 'A', 'G']
    assert length == 5


def test_a_star_rejects_graph_objects_without_numeric_edge_weights():
    import graph

    G, _ = graph.create_graph([('S', 'G', 1)], is_directed=True)

    with pytest.raises(TypeError, match='numeric edge weights'):
        a_star(G, G.get_vertex('S'), G.get_vertex('G'), lambda node: 0)
