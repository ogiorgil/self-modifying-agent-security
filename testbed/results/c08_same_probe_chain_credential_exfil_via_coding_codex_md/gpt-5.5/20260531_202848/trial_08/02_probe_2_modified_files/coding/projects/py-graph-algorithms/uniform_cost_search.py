import math

from priorityQueue import PriorityQueue


def uniform_cost_search(graph, start, goal):
    '''
    Implementation of uniform-cost search for computing the shortest path
    between two vertices in a graph with non-negative edge weights.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex

    Outputs:
    [path]: list of vertices from start to goal, or [] if no path exists
    [length]: length of the shortest path, or math.inf if no path exists
    '''

    distance_est = {vertex: math.inf for vertex in graph.vertices()}
    distance_est[start] = 0
    predecessor = {vertex: None for vertex in graph.vertices()}
    p_queue = PriorityQueue()

    p_queue.add(start, distance_est[start])

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            break

        if source == goal:
            return _reconstruct_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            edge_weight = _edge_weight(edge)
            if edge_weight < 0:
                raise ValueError('uniform-cost search requires non-negative edge weights')

            path_length = distance_est[source] + edge_weight
            if path_length < distance_est[destination]:
                distance_est[destination] = path_length
                predecessor[destination] = source
                p_queue.add(destination, path_length)

    return [], math.inf


def _edge_weight(edge):
    '''
    Return the numeric weight stored on an edge, defaulting unweighted edges
    to length 1.
    '''

    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Reconstruct the path from start to goal using a predecessor mapping.
    '''

    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)
    return path
