import math
from pathlib import Path
import sys

import pytest
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from astar import a_star  # noqa: E402


FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def _load_yaml(path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.Loader)


@pytest.mark.parametrize(
    "fixture_path",
    sorted(FIXTURES_DIR.glob("*.yaml")),
    ids=lambda p: p.name,
)
def test_a_star_from_yaml_fixtures(fixture_path):
    fixture = _load_yaml(fixture_path)

    graph = fixture["graph"]
    start = fixture["start"]
    goal = fixture["goal"]

    heuristic_map = fixture.get("heuristic", {})
    heuristic = lambda node: heuristic_map.get(node, 0)

    path, length = a_star(graph, start, goal, heuristic)

    expected_path = fixture.get("expected_path", None)
    expected_length = fixture.get("expected_length", None)

    assert path == expected_path
    if expected_length is None:
        assert length is None
    elif expected_length == math.inf or (isinstance(expected_length, float) and math.isinf(expected_length)):
        assert math.isinf(length)
    else:
        assert length == expected_length
