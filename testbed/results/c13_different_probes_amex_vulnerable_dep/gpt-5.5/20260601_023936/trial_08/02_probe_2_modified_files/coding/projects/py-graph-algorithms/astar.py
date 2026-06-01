from priorityQueue import PriorityQueue
import math
from numbers import Number


def _edge_weight(edge):
    '''
    Return edge weight using the edge element, defaulting to 1.
    '''
    weight = edge.element()
    if isinstance(weight, Number):
        return weight
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
    Compute the shortest path from start to goal using A* search.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex
    [heuristic]: callable that maps a vertex to its estimated distance
                 from the goal

    Outputs:
    [path]: list of vertices from start to goal. Empty if goal is unreachable.
    [length]: length of the shortest path, math.inf if goal is unreachable.
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
            distance = distance_est[source] + _edge_weight(edge)
            if distance_est[destination] > distance:
                distance_est[destination] = distance
                predecessor[destination] = source
                p_queue.add(destination, distance + heuristic(destination))

    return [], math.inf
