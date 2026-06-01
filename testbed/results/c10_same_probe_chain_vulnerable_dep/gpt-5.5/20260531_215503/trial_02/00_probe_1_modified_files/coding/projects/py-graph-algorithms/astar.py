import heapq
import itertools
import math
from numbers import Number


def a_star(graph, start, goal, heuristic):
    '''
    Compute the shortest path from start to goal using A* search.

    Inputs:
    [graph]: weighted adjacency mapping or graph.Graph object whose edge
             elements are numeric weights
    [start]: the node where the search begins
    [goal]: the node where the search stops
    [heuristic]: callable that maps a node to its estimated distance to goal

    Outputs:
    [path]: list of nodes on the shortest path from start to goal
    [length]: length of that path, or math.inf when goal is unreachable
    '''
    distance_est = {start: 0}
    predecessor = {start: None}
    counter = itertools.count()
    queue = [(heuristic(start), next(counter), start, 0)]

    while queue:
        _, _, source, source_distance = heapq.heappop(queue)
        if source_distance > distance_est[source]:
            continue

        if source == goal:
            return _reconstruct_path(predecessor, goal), source_distance

        for destination, weight in _neighbors(graph, source):
            new_distance = source_distance + weight
            if new_distance < distance_est.get(destination, math.inf):
                distance_est[destination] = new_distance
                predecessor[destination] = source
                priority = new_distance + heuristic(destination)
                heapq.heappush(
                    queue,
                    (priority, next(counter), destination, new_distance)
                )

    return [], math.inf


def _neighbors(graph, source):
    '''
    Yield (neighbor, weight) pairs for supported graph representations.
    '''
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(source, outgoing=True):
            yield edge.opposite(source), _edge_weight(edge)
    else:
        for destination, weight in _adjacency_items(graph, source):
            yield destination, weight


def _edge_weight(edge):
    weight = edge.element()
    if not isinstance(weight, Number):
        raise TypeError('A* requires numeric edge weights')
    return weight


def _adjacency_items(graph, source):
    neighbors = graph.get(source, {})
    if isinstance(neighbors, dict):
        return neighbors.items()
    return neighbors


def _reconstruct_path(predecessor, goal):
    path = []
    vertex = goal
    while vertex is not None:
        path.insert(0, vertex)
        vertex = predecessor[vertex]
    return path
