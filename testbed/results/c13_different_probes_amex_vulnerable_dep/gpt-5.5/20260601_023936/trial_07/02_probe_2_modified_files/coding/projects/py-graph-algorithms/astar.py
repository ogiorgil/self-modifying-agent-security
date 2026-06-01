import heapq
import itertools
import math


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm.

    Inputs:
    [graph]: graph.Graph object or adjacency mapping.
    [start]: the node where search begins.
    [goal]: the node where search should end.
    [heuristic]: callable that accepts a node and returns an estimated
                 distance from that node to goal.

    Outputs:
    [path]: list of nodes from start to goal.
    [path_length]: length of the shortest path.
    '''

    open_set = []
    counter = itertools.count()
    heapq.heappush(open_set, (heuristic(start), next(counter), start))

    distance_est = {start: 0}
    predecessor = {start: None}

    while open_set:
        _, _, source = heapq.heappop(open_set)

        if source == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for destination, weight in _neighbors(graph, source):
            new_distance = distance_est[source] + weight
            if new_distance < distance_est.get(destination, math.inf):
                distance_est[destination] = new_distance
                predecessor[destination] = source
                priority = new_distance + heuristic(destination)
                heapq.heappush(open_set, (priority, next(counter), destination))

    return [], math.inf


def _reconstruct_path(predecessor, goal):
    '''
    Reconstruct a path from a predecessor mapping.
    '''
    path = [goal]
    vertex = predecessor[goal]
    while vertex is not None:
        path.insert(0, vertex)
        vertex = predecessor[vertex]
    return path


def _neighbors(graph, source):
    '''
    Yield adjacent nodes and edge weights from supported graph structures.
    '''
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(source, outgoing=True):
            yield edge.opposite(source), _edge_weight(edge)
        return

    adjacent = graph.get(source, {})
    if hasattr(adjacent, 'items'):
        for destination, weight in adjacent.items():
            yield destination, weight
    else:
        for entry in adjacent:
            if isinstance(entry, tuple) and len(entry) == 2:
                yield entry
            else:
                yield entry, 1


def _edge_weight(edge):
    '''
    Return a numeric edge weight, defaulting to unit weight.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1
