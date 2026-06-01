from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing the shortest path from
    start to goal in a graph with non-negative edge lengths.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the target vertex
    [heuristic]: callable that takes a vertex and returns an estimate of
                 the distance from that vertex to goal

    Outputs:
    [path]: list of vertices on the shortest path from start to goal.
            If goal is unreachable, returns an empty list.
    [length]: length of the shortest path. If goal is unreachable,
              returns math.inf.
    '''

    if start == goal:
        return [start], 0

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

        if source == goal:
            path = [goal]
            vertex = predecessor[goal]
            while vertex is not None:
                path.insert(0, vertex)
                vertex = predecessor[vertex]
            return path, distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            edge_length = _edge_length(edge)
            new_distance = distance_est[source] + edge_length
            if distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                priority = new_distance + heuristic(destination)
                p_queue.add(destination, priority)

    return [], math.inf


def _edge_length(edge):
    '''
    Return the edge length stored on the edge, or 1 for unweighted edges.
    '''
    element = edge.element()
    if isinstance(element, (int, float)):
        return element
    return 1
