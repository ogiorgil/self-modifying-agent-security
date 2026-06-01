from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm for computing the shortest
    path between two nodes.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source node
    [goal]: the destination node
    [heuristic]: callable that maps a node to an estimated distance
                 from that node to the goal

    Outputs:
    [path]: list of nodes on the shortest path from start to goal
    [length]: length of that shortest path
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
            new_distance = distance_est[source] + weight

            if distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                p_queue.add(destination, new_distance + heuristic(destination))

    return [], math.inf


def _edge_weight(edge):
    '''
    Return the numeric edge weight, or unit weight for unlabeled edges.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Build the path from the predecessor mapping.
    '''
    path = [goal]
    vertex = goal

    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)

    return path
