from priorityQueue import PriorityQueue
import math


def _edge_weight(edge):
    '''
    Return the edge's numeric weight, defaulting to 1 for unweighted graphs.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _construct_path(predecessor, start, goal):
    '''
    Construct the shortest path from start to goal.
    '''
    path = [goal]
    vertex = goal

    while vertex is not start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)

    return path


def uniform_cost_search(graph, start, goal):
    '''
    Implementation of uniform-cost search for finding the shortest path
    between two vertices on a graph with non-negative edge weights.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex

    Outputs:
    [path]: list of vertices in the shortest path from start to goal
    [path_length]: length of the shortest path
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

        if source is goal:
            return _construct_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            new_distance = distance_est[source] + _edge_weight(edge)

            if distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                p_queue.add(destination, new_distance)

    return [], math.inf
