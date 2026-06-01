from priorityQueue import PriorityQueue
import math


def uniform_cost_search(graph, start, goal):
    '''
    Implementation of uniform-cost search for computing the shortest path
    from start to goal on weighted graphs.

    Inputs:
    [graph]: graph.Graph object or adjacency mapping
    [start]: start node for the search
    [goal]: destination node for the search

    Outputs:
    [path]: list of nodes in the shortest path from start to goal
    [length]: length of the shortest path
    '''

    distance_est = {start: 0}
    predecessor = {start: None}
    p_queue = PriorityQueue()

    p_queue.add(start, distance_est[start])

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            return [], math.inf

        if source == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for neighbor, edge_weight in _neighbors(graph, source):
            new_distance = distance_est[source] + edge_weight
            if new_distance < distance_est.get(neighbor, math.inf):
                distance_est[neighbor] = new_distance
                predecessor[neighbor] = source
                p_queue.add(neighbor, new_distance)


def _reconstruct_path(predecessor, goal):
    '''
    Return the path ending at goal from a predecessor mapping.
    '''
    path = []
    node = goal
    while node is not None:
        path.insert(0, node)
        node = predecessor[node]
    return path


def _neighbors(graph, node):
    '''
    Yield (neighbor, edge_weight) pairs for supported graph representations.
    '''
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(node, outgoing=True):
            yield edge.opposite(node), _edge_weight(edge)
    else:
        for neighbor, edge_weight in graph[node].items():
            yield neighbor, edge_weight


def _edge_weight(edge):
    '''
    Return a numeric edge element as weight, defaulting to one.
    '''
    element = edge.element()
    if isinstance(element, (int, float)):
        return element
    return 1
