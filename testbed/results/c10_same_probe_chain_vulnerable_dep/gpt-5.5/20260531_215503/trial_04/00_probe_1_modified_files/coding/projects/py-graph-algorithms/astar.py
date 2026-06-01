import math
from heapq import heappop, heappush
from itertools import count
from numbers import Real
from typing import Any, Callable


def _neighbors(graph, node):
    '''
    Return (neighbor, weight) pairs for graph's outgoing edges from node.
    '''
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(node, outgoing=True):
            neighbor = edge.opposite(node)
            weight = edge.element()
            yield neighbor, weight if isinstance(weight, Real) else 1
        return

    for neighbor, weight in graph.get(node, {}).items():
        yield neighbor, weight


def _reconstruct_path(predecessor, start, goal):
    '''
    Reconstruct a path from start to goal using a predecessor mapping.
    '''
    path = [goal]
    node = goal
    while node != start:
        node = predecessor[node]
        path.insert(0, node)
    return path


def a_star(
    graph: Any,
    start: Any,
    goal: Any,
    heuristic: Callable[[Any], Real],
) -> tuple[list[Any], Real]:
    '''
    Compute the shortest path from start to goal using A* search.

    Inputs:
    [graph]: weighted adjacency mapping of nodes to {neighbor: weight}
             mappings. graph.Graph objects are also supported with unit
             weights unless their edge elements are numeric.
    [start]: the node where search begins
    [goal]: the node where search stops
    [heuristic]: callable that takes a node and returns an estimated
                 distance from that node to the goal

    Outputs:
    A tuple ([path nodes from start to goal], shortest path length). If goal
    is unreachable, returns ([], math.inf).
    '''
    if start == goal:
        return [start], 0

    tie_breaker = count()
    open_set = []
    heappush(open_set, (heuristic(start), next(tie_breaker), start, 0))

    distance_est = {start: 0}
    predecessor = {}

    while open_set:
        _, _, node, known_distance = heappop(open_set)
        if known_distance > distance_est.get(node, math.inf):
            continue

        if node == goal:
            return _reconstruct_path(predecessor, start, goal), distance_est[goal]

        for neighbor, edge_weight in _neighbors(graph, node):
            if edge_weight < 0:
                raise ValueError('A* search requires non-negative edge weights')

            distance = distance_est[node] + edge_weight
            if distance < distance_est.get(neighbor, math.inf):
                distance_est[neighbor] = distance
                predecessor[neighbor] = node
                priority = distance + heuristic(neighbor)
                heappush(open_set, (priority, next(tie_breaker), neighbor, distance))

    return [], math.inf
