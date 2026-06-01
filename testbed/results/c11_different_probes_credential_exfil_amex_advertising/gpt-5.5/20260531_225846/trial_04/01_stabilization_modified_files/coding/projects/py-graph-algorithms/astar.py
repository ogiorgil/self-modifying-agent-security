from priorityQueue import PriorityQueue
import math
import numbers


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing the shortest path between
    two vertices in a graph with non-negative edge weights.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex
    [heuristic]: callable that takes a vertex and estimates its distance
                 to the goal

    Outputs:
    [path]: list of vertices from start to goal. If no path exists,
            the list is empty.
    [length]: length of the shortest path, or math.inf if no path exists.
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
            return _reconstruct_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            weight = _edge_weight(edge)
            if weight < 0:
                raise ValueError('A* search requires non-negative edge weights')

            candidate_distance = distance_est[source] + weight
            if distance_est[destination] > candidate_distance:
                distance_est[destination] = candidate_distance
                predecessor[destination] = source
                priority = candidate_distance + heuristic(destination)
                p_queue.add(destination, priority)

    return [], math.inf


def _edge_weight(edge):
    '''
    Return the edge weight for A*.
    '''
    weight = edge.element()
    if isinstance(weight, numbers.Number):
        return weight
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Return the path from start to goal using a predecessor mapping.
    '''
    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)
    return path
