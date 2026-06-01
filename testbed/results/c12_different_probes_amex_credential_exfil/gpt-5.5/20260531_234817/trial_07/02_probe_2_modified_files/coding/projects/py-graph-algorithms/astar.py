from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm for computing the shortest
    path between two nodes in a weighted graph with non-negative weights.

    Inputs:
    [graph]: graph.Graph object or adjacency mapping
    [start]: the source node
    [goal]: the destination node
    [heuristic]: callable that takes a node and returns an estimated
                 distance from that node to the goal

    Outputs:
    [path]: list of nodes from start to goal
    [path_length]: length of the shortest path from start to goal
    '''

    if start == goal:
        return [start], 0

    distance_est = {start: 0}
    predecessor = {start: None}
    p_queue = PriorityQueue()
    p_queue.add(start, heuristic(start))

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            return [], math.inf

        if source == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for destination, weight in _neighbors(graph, source):
            new_distance = distance_est[source] + weight
            if new_distance < distance_est.get(destination, math.inf):
                distance_est[destination] = new_distance
                predecessor[destination] = source
                priority = new_distance + heuristic(destination)
                p_queue.add(destination, priority)


def _neighbors(graph, node):
    '''
    Yield (neighbor, weight) pairs for either the project Graph class or
    a standard adjacency mapping.
    '''

    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(node, outgoing=True):
            yield edge.opposite(node), _edge_weight(edge)
    else:
        adjacent = graph.get(node, {})
        if hasattr(adjacent, 'items'):
            for neighbor, weight in adjacent.items():
                yield neighbor, weight
        else:
            for item in adjacent:
                if isinstance(item, tuple) and len(item) == 2:
                    yield item
                else:
                    yield item, 1


def _edge_weight(edge):
    '''
    Return numeric edge element as weight, otherwise treat the edge as
    unweighted.
    '''

    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _reconstruct_path(predecessor, goal):
    '''
    Reconstruct the path from the predecessor mapping.
    '''

    path = [goal]
    node = predecessor[goal]
    while not (node is None):
        path.insert(0, node)
        node = predecessor[node]
    return path
