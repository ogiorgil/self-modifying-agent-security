import math
from numbers import Number

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing one shortest path.

    Inputs:
    [graph]: graph.Graph object or adjacency mapping
    [start]: the source node
    [goal]: the target node
    [heuristic]: callable taking a node and returning its distance estimate

    Outputs:
    [path]: list of nodes from start to goal
    [length]: length of the shortest path
    '''

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    distance_est = {start: 0}
    predecessor = {start: None}

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            return [], math.inf

        if current == goal:
            return _reconstruct_path(predecessor, current), distance_est[current]

        for neighbor, edge_weight in _neighbors(graph, current):
            new_distance = distance_est[current] + edge_weight
            if new_distance < distance_est.get(neighbor, math.inf):
                distance_est[neighbor] = new_distance
                predecessor[neighbor] = current
                open_set.add(neighbor, new_distance + heuristic(neighbor))


def _reconstruct_path(predecessor, current):
    '''
    Return the path ending at current using the predecessor mapping.
    '''

    path = []
    while current is not None:
        path.insert(0, current)
        current = predecessor[current]
    return path


def _neighbors(graph, node):
    '''
    Yield (neighbor, weight) pairs for a graph.Graph or adjacency mapping.
    '''

    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(node, outgoing=True):
            yield edge.opposite(node), _edge_weight(edge)
    else:
        for neighbor, weight in graph[node].items():
            yield neighbor, weight


def _edge_weight(edge):
    '''
    Return a numeric edge weight, defaulting unweighted edges to 1.
    '''

    element = edge.element()
    if isinstance(element, Number):
        return element
    return 1
