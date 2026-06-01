from priorityQueue import PriorityQueue
import math


def uniform_cost_search(graph, start, goal):
    '''
    Implementation of uniform-cost search for computing the shortest path
    between start and goal.

    Inputs:
    [graph]: graph.Graph object or adjacency mapping
    [start]: the source node
    [goal]: the target node

    Outputs:
    [path]: list of nodes on the shortest path from start to goal
    [length]: length of the shortest path
    '''

    distance_est = {start: 0}
    predecessor = {start: None}
    p_queue = PriorityQueue()

    p_queue.add(start, 0)

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            return [], math.inf

        if source == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for destination, weight in _neighbors(graph, source):
            path_length = distance_est[source] + weight
            if path_length < distance_est.get(destination, math.inf):
                distance_est[destination] = path_length
                predecessor[destination] = source
                p_queue.add(destination, path_length)


def _neighbors(graph, source):
    '''
    Return (neighbor, weight) pairs for supported graph representations.
    '''

    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(source, outgoing=True):
            yield edge.opposite(source), _edge_weight(edge)
    else:
        adjacent = graph[source]
        if hasattr(adjacent, 'items'):
            adjacent = adjacent.items()
        for item in adjacent:
            yield _neighbor_from_item(item)


def _edge_weight(edge):
    '''
    Return the numeric edge element, defaulting to unit weight.
    '''

    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _neighbor_from_item(item):
    '''
    Return a (neighbor, weight) pair from an adjacency mapping item.
    '''

    if isinstance(item, tuple) and len(item) == 2:
        return item
    return item, 1


def _reconstruct_path(predecessor, goal):
    '''
    Reconstruct the path to goal from a predecessor mapping.
    '''

    path = []
    vertex = goal
    while vertex is not None:
        path.insert(0, vertex)
        vertex = predecessor[vertex]
    return path
