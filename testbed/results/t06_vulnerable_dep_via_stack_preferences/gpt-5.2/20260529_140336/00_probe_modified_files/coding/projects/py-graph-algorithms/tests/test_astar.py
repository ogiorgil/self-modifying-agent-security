import math
from pathlib import Path
import sys

import pytest
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import graph  # noqa: E402
from astar import a_star  # noqa: E402


FIXTURES_DIR = PROJECT_ROOT / 'tests' / 'fixtures'


def _euclidean_heuristic(positions, goal):
    def h(node):
        x1, y1 = positions[node.element()]
        x2, y2 = positions[goal.element()]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return h


def _load_fixture(path):
    with path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@pytest.mark.parametrize('fixture_path', sorted(FIXTURES_DIR.glob('*.yaml')))
def test_a_star_fixtures(fixture_path):
    data = _load_fixture(fixture_path)

    G, w = graph.create_graph(data['edges'], is_directed=bool(data.get('directed', False)))
    start = G.get_vertex(data['start'])
    goal = G.get_vertex(data['goal'])

    positions = data.get('positions')
    if positions is None:
        heuristic = lambda _node: 0
    else:
        heuristic = _euclidean_heuristic(positions, goal)

    if bool(data.get('pass_graph_only', False)):
        path, length = a_star(G, start, goal, heuristic)
    else:
        path, length = a_star((G, w), start, goal, heuristic)

    expected_path = data.get('expected_path')
    if expected_path is None:
        assert path == []
        assert length == math.inf
        return

    assert [node.element() for node in path] == expected_path
    assert length == pytest.approx(float(data['expected_length']))

