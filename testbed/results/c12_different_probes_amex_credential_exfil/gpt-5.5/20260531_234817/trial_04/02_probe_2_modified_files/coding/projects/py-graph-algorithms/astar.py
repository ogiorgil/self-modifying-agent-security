from priorityQueue import PriorityQueue
import math
import numbers


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing a shortest path between
    start and goal.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex. It is a graph.Vertex instance of graph.
    [goal]: the target vertex. It is a graph.Vertex instance of graph.
    [heuristic]: callable that maps a vertex to an estimate of its distance
                 to goal.

    Outputs:
    [path]: list of vertices on the shortest path from start to goal
    [length]: length of the shortest path
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
            return [], math.inf

        if source == goal:
            return _reconstruct_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            candidate = distance_est[source] + _edge_weight(edge)
            if distance_est[destination] > candidate:
                distance_est[destination] = candidate
                predecessor[destination] = source
                p_queue.add(destination, candidate + heuristic(destination))


def _edge_weight(edge):
    '''
    Return the numeric value stored on edge or 1 for unweighted edges.
    '''
    value = edge.element()
    if isinstance(value, numbers.Number):
        return value
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Reconstruct a path from a predecessor mapping.
    '''
    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)
    return path
