from priorityQueue import PriorityQueue
import math
import numbers


def _edge_weight(edge):
    '''
    Return a numeric edge weight, defaulting to 1 for unweighted graphs.
    '''
    value = edge.element()
    if isinstance(value, numbers.Number):
        return value
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Reconstruct the shortest path from start to goal.
    '''
    path = [goal]
    vertex = goal

    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)

    return path


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for finding a shortest path.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: source vertex for the search
    [goal]: target vertex for the search
    [heuristic]: callable taking a vertex and returning an estimate of the
                 distance from that vertex to goal

    Outputs:
    [path]: list of vertices from start to goal, or an empty list if no path
            exists
    [length]: length of the shortest path, or math.inf if no path exists
    '''
    distance_est = {vertex: math.inf for vertex in graph.vertices()}
    predecessor = {vertex: None for vertex in graph.vertices()}
    p_queue = PriorityQueue()

    distance_est[start] = 0
    p_queue.add(start, heuristic(start))

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            break

        if source == goal:
            return _reconstruct_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            weight = _edge_weight(edge)
            if weight < 0:
                raise ValueError('A* search requires non-negative edge weights')

            new_distance = distance_est[source] + weight
            if distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                p_queue.add(destination, new_distance + heuristic(destination))

    return [], math.inf
