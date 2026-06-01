import heapq
import itertools
import math


def _edge_weight(edge):
    '''
    Return the edge weight stored on the edge, defaulting to unit weight.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _reconstruct_path(predecessor, goal):
    '''
    Return the path ending at goal from a predecessor mapping.
    '''
    path = [goal]
    vertex = predecessor[goal]

    while vertex is not None:
        path.insert(0, vertex)
        vertex = predecessor[vertex]

    return path


def a_star(graph, start, goal, heuristic):
    '''
    Compute the shortest path from start to goal using A* search.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex
    [heuristic]: callable that takes a vertex and returns an estimate of
                 the distance from that vertex to goal

    Outputs:
    [path]: list of vertices from start to goal, or an empty list if goal
            is unreachable
    [distance]: length of the shortest path, or math.inf if unreachable
    '''
    distance_est = {vertex: math.inf for vertex in graph.vertices()}
    distance_est[start] = 0
    predecessor = {vertex: None for vertex in graph.vertices()}

    counter = itertools.count()
    open_set = []
    heapq.heappush(open_set, (heuristic(start), 0, next(counter), start))

    while open_set:
        _, source_distance, _, source = heapq.heappop(open_set)

        if source_distance > distance_est[source]:
            continue

        if source == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            new_distance = distance_est[source] + _edge_weight(edge)
            if distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                priority = new_distance + heuristic(destination)
                entry = (priority, new_distance, next(counter), destination)
                heapq.heappush(open_set, entry)

    return [], math.inf
