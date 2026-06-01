import math
from collections.abc import Mapping
from typing import Any, Callable, Iterable, Tuple

from priorityQueue import PriorityQueue


def a_star(graph: Any,
           start: Any,
           goal: Any,
           heuristic: Callable[[Any], float]) -> Tuple[list, float]:
    """Return the shortest path from start to goal using A* search."""
    distance_est = {start: 0}
    predecessor = {start: None}
    p_queue = PriorityQueue()

    p_queue.add(start, heuristic(start))

    while True:
        try:
            current = p_queue.pop()
        except KeyError:
            return [], math.inf

        if current == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for destination, weight in _neighbors(graph, current):
            if weight < 0:
                raise ValueError('A* search does not support negative weights')

            candidate_distance = distance_est[current] + weight
            if candidate_distance < distance_est.get(destination, math.inf):
                distance_est[destination] = candidate_distance
                predecessor[destination] = current
                priority = candidate_distance + heuristic(destination)
                p_queue.add(destination, priority)


def _reconstruct_path(predecessor: dict, goal: Any) -> list:
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = predecessor[current]

    path.reverse()
    return path


def _neighbors(graph: Any, vertex: Any) -> Iterable[Tuple[Any, float]]:
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(vertex, outgoing=True) or []:
            yield edge.opposite(vertex), _edge_weight(edge)
        return

    adjacency = graph.get(vertex, {}) if hasattr(graph, 'get') else graph[vertex]
    if isinstance(adjacency, Mapping):
        for destination, weight in adjacency.items():
            yield destination, weight
        return

    for destination in adjacency:
        if isinstance(destination, tuple) and len(destination) == 2:
            yield destination
        else:
            yield destination, 1


def _edge_weight(edge: Any) -> float:
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1
