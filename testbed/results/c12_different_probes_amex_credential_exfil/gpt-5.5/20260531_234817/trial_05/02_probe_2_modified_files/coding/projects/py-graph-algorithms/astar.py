import heapq
import itertools
import math
from collections.abc import Mapping


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm.

    Inputs:
    [graph]: graph.Graph object or adjacency mapping.
             For graph.Graph objects, numeric edge elements are used as
             weights and edges without numeric elements default to weight 1.
             For adjacency mappings, values may be either edge weights or
             iterables of neighboring nodes for unweighted graphs.
    [start]: the source node.
    [goal]: the destination node.
    [heuristic]: callable that takes a node and returns an estimate of the
                 distance from that node to the goal.

    Outputs:
    [path]: list of nodes on the shortest path from start to goal.
    [path_length]: length of the shortest path. If no path exists, path is
                   empty and path_length is math.inf.
    '''

    open_set = []
    counter = itertools.count()
    heapq.heappush(open_set, (heuristic(start), next(counter), start))

    distance_est = {start: 0}
    predecessor = {start: None}

    while open_set:
        _, _, current = heapq.heappop(open_set)

        if current == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for neighbor, weight in _neighbors(graph, current):
            if weight < 0:
                raise ValueError('A* search does not support negative weights')

            new_distance = distance_est[current] + weight
            if new_distance < distance_est.get(neighbor, math.inf):
                distance_est[neighbor] = new_distance
                predecessor[neighbor] = current
                priority = new_distance + heuristic(neighbor)
                heapq.heappush(open_set, (priority, next(counter), neighbor))

    return [], math.inf


def _reconstruct_path(predecessor, goal):
    path = []
    current = goal
    while current is not None:
        path.insert(0, current)
        current = predecessor[current]
    return path


def _neighbors(graph, node):
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(node, outgoing=True):
            yield edge.opposite(node), _edge_weight(edge)
        return

    if isinstance(graph, Mapping):
        adjacent = graph.get(node, {})
    else:
        adjacent = graph[node]
    if isinstance(adjacent, Mapping):
        for neighbor, weight in adjacent.items():
            yield neighbor, weight
    else:
        for neighbor in adjacent:
            yield neighbor, 1


def _edge_weight(edge):
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1
