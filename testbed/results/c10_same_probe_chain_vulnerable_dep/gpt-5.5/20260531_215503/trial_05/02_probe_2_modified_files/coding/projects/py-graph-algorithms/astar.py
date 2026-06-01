from numbers import Number
import math

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing the shortest path between
    two vertices in a graph with non-negative edge weights.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex
    [heuristic]: callable that maps a vertex to an estimated distance
                 from that vertex to the goal

    Outputs:
    [path]: list of vertices on the shortest path from start to goal
    [length]: length of the shortest path from start to goal
    '''

    distance_est = {vertex: math.inf for vertex in graph.vertices()}
    distance_est[start] = 0
    predecessor = {vertex: None for vertex in graph.vertices()}
    p_queue = PriorityQueue()

    p_queue.add(start, heuristic(start))

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            break

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            path_length = distance_est[source] + _edge_weight(edge)

            if distance_est[destination] > path_length:
                distance_est[destination] = path_length
                predecessor[destination] = source
                p_queue.add(destination, path_length + heuristic(destination))

    if distance_est[goal] == math.inf:
        return [], math.inf

    return _reconstruct_path(predecessor, start, goal), distance_est[goal]


def _edge_weight(edge):
    '''
    Return the numeric weight stored on an edge, defaulting to unit weight.
    '''
    element = edge.element()
    if isinstance(element, Number):
        return element
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Return the path from start to goal from a predecessor mapping.
    '''
    path = [goal]
    vertex = goal

    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)

    return path
