from priorityQueue import PriorityQueue
import math
import numbers


def _edge_weight(edge):
    '''
    Return a numeric edge weight, defaulting to 1 for unlabeled edges.
    '''
    weight = edge.element()
    if isinstance(weight, numbers.Real):
        return weight
    return 1


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


def uniform_cost_search(graph, start, goal):
    '''
    Implementation of uniform-cost search for shortest paths.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex

    Outputs:
    [path]: shortest path from start to goal as a list of vertices
    [length]: length of the shortest path from start to goal
    '''
    distance_est = {vertex: math.inf for vertex in graph.vertices()}
    distance_est[start] = 0
    predecessor = {vertex: None for vertex in graph.vertices()}
    p_queue = PriorityQueue()

    p_queue.add(start, 0)

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            return [], math.inf

        if source == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            weight = _edge_weight(edge)
            if weight < 0:
                raise ValueError('Uniform-cost search does not support negative edge weights')

            candidate_distance = distance_est[source] + weight
            if distance_est[destination] > candidate_distance:
                distance_est[destination] = candidate_distance
                predecessor[destination] = source
                p_queue.add(destination, candidate_distance)
