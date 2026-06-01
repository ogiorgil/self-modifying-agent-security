import heapq
import itertools
import math
from collections.abc import Mapping


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm for computing the shortest
    path between two nodes in a weighted graph.

    Inputs:
    [graph]: graph.Graph object or adjacency mapping of graph representation
    [start]: the source node
    [goal]: the target node
    [heuristic]: callable that returns an estimated distance from a node
                 to the goal

    Outputs:
    [path]: list of nodes on the shortest path from start to goal
    [length]: length of the shortest path
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
            new_distance = distance_est[current] + weight
            if new_distance < distance_est.get(neighbor, math.inf):
                distance_est[neighbor] = new_distance
                predecessor[neighbor] = current
                priority = new_distance + heuristic(neighbor)
                heapq.heappush(open_set, (priority, next(counter), neighbor))

    return [], math.inf


def _neighbors(graph, node):
    '''
    Return (neighbor, weight) pairs for a graph node.
    '''
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(node, outgoing=True):
            neighbor = edge.opposite(node)
            weight = edge.element()
            if not isinstance(weight, (int, float)):
                weight = 1
            yield neighbor, weight
        return

    adjacent = graph[node]
    if isinstance(adjacent, Mapping):
        for neighbor, weight in adjacent.items():
            yield neighbor, weight
    else:
        for neighbor in adjacent:
            yield neighbor, 1


def _reconstruct_path(predecessor, goal):
    '''
    Return path ending at goal using the predecessor mapping.
    '''
    path = []
    node = goal
    while node is not None:
        path.insert(0, node)
        node = predecessor[node]
    return path
