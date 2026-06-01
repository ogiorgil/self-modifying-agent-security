import math
from collections.abc import Callable

from priorityQueue import PriorityQueue


def _edge_weight(edge):
    '''
    Return numeric edge weight, defaulting to one for unweighted graphs.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _reconstruct_path(predecessor, goal):
    '''
    Return the path ending at goal using a predecessor mapping.
    '''
    path = [goal]
    vertex = predecessor[goal]
    while vertex is not None:
        path.insert(0, vertex)
        vertex = predecessor[vertex]
    return path


def a_star(graph, start, goal, heuristic: Callable) -> tuple[list, float]:
    '''
    Compute the shortest path from start to goal using A* search.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source node
    [goal]: the destination node
    [heuristic]: callable taking a node and returning a numeric distance
                 estimate to goal

    Outputs:
    [path]: list of nodes on the shortest path from start to goal
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
            break

        if source == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            candidate_distance = distance_est[source] + _edge_weight(edge)

            if candidate_distance < distance_est[destination]:
                distance_est[destination] = candidate_distance
                predecessor[destination] = source
                p_queue.add(destination,
                            candidate_distance + heuristic(destination))

    return [], math.inf
