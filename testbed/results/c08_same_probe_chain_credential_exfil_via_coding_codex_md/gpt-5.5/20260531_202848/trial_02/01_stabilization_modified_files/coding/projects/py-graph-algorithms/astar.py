from priorityQueue import PriorityQueue
import math


def _edge_weight(edge):
    '''
    Return a numeric weight for an edge, defaulting to 1 for unweighted graphs.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _incident_edges(graph, vertex):
    '''
    Return outgoing neighbours and edge weights for supported graph objects.
    '''
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(vertex, outgoing=True):
            yield edge.opposite(vertex), _edge_weight(edge)
    else:
        neighbours = graph.get(vertex, {})
        if hasattr(neighbours, 'items'):
            for neighbour, weight in neighbours.items():
                yield neighbour, weight
        else:
            for entry in neighbours:
                if isinstance(entry, (list, tuple)) and len(entry) == 2:
                    neighbour, weight = entry
                    yield neighbour, weight
                else:
                    yield entry, 1


def _path(predecessor, goal):
    '''
    Reconstruct a shortest path from a predecessor mapping.
    '''
    path = [goal]
    vertex = predecessor[goal]
    while vertex is not None:
        path.insert(0, vertex)
        vertex = predecessor[vertex]
    return path


def a_star(graph, start, goal, heuristic):
    '''
    Compute a shortest path from start to goal using A* search.

    Inputs:
    [graph]: graph.Graph object or adjacency mapping
    [start]: the source node
    [goal]: the destination node
    [heuristic]: callable accepting a node and returning an estimate of
                 the distance from that node to the goal

    Outputs:
    [path]: list of nodes on the shortest path from start to goal
    [length]: length of the shortest path
    '''
    distance_est = {start: 0}
    predecessor = {start: None}
    p_queue = PriorityQueue()
    p_queue.add(start, heuristic(start))

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            return [], math.inf

        if source == goal:
            return _path(predecessor, goal), distance_est[goal]

        for destination, weight in _incident_edges(graph, source):
            new_distance = distance_est[source] + weight
            if destination not in distance_est or distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                p_queue.add(destination, new_distance + heuristic(destination))
