import heapq
import itertools
import math
from collections.abc import Callable, Iterable, Mapping
from typing import Any


def _iter_neighbors(graph: Mapping[Any, Any], node: Any) -> Iterable[tuple[Any, float]]:
    '''
    Return an iterator over (neighbor, weight) pairs for node.
    '''
    neighbors = graph.get(node, {})
    if hasattr(neighbors, 'items'):
        return neighbors.items()
    return neighbors


def a_star(graph: Mapping[Any, Any],
           start: Any,
           goal: Any,
           heuristic: Callable[[Any], float]) -> tuple[list[Any], float]:
    '''
    Compute the shortest path from start to goal using A* search.

    Inputs:
    [graph]: adjacency mapping whose values are either mappings of
             neighbor -> edge weight or iterables of (neighbor, weight) pairs
    [start]: source node
    [goal]: destination node
    [heuristic]: callable returning an estimate from a node to goal

    Outputs:
    A tuple containing the shortest path as a list of nodes and its length.
    If goal is unreachable then returns ([], math.inf).
    '''

    if start == goal:
        return [start], 0

    distance_est = {start: 0}
    predecessor = {start: None}
    counter = itertools.count()
    priority_queue = [(heuristic(start), next(counter), 0, start)]

    while priority_queue:
        _, _, source_distance, source = heapq.heappop(priority_queue)
        if source_distance > distance_est[source]:
            continue

        if source == goal:
            path = []
            vertex = goal
            while vertex is not None:
                path.insert(0, vertex)
                vertex = predecessor[vertex]
            return path, distance_est[goal]

        for destination, weight in _iter_neighbors(graph, source):
            if weight < 0:
                raise ValueError('A* search requires non-negative edge weights')
            candidate_distance = distance_est[source] + weight
            if candidate_distance < distance_est.get(destination, math.inf):
                distance_est[destination] = candidate_distance
                predecessor[destination] = source
                priority = candidate_distance + heuristic(destination)
                heapq.heappush(priority_queue,
                               (priority, next(counter),
                                candidate_distance, destination))

    return [], math.inf
