import math
from numbers import Number

from priorityQueue import PriorityQueue


def _neighbors(graph, node):
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(node, outgoing=True):
            neighbor = edge.opposite(node)
            weight = edge.element()
            if not isinstance(weight, Number):
                weight = 1
            yield neighbor, weight
    else:
        adjacent = graph.get(node, {})
        if hasattr(adjacent, 'items'):
            for neighbor, weight in adjacent.items():
                yield neighbor, weight
        else:
            for item in adjacent:
                if isinstance(item, (list, tuple)) and len(item) == 2:
                    neighbor, weight = item
                else:
                    neighbor, weight = item, 1
                yield neighbor, weight


def _reconstruct_path(predecessor, goal):
    path = [goal]
    vertex = predecessor[goal]
    while vertex is not None:
        path.insert(0, vertex)
        vertex = predecessor[vertex]
    return path


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm.

    Inputs:
    [graph]: graph.Graph object or adjacency mapping. For graph.Graph,
             numeric edge elements are used as weights and nonnumeric edge
             elements are treated as unit weights. For adjacency mappings,
             values may be neighbor-to-weight mappings or iterables of
             (neighbor, weight) pairs.
    [start]: source node
    [goal]: destination node
    [heuristic]: callable that takes a node and returns an estimate of
                 the distance to the goal

    Outputs:
    [path]: list of nodes on the shortest path from start to goal.
            Empty when goal is unreachable.
    [length]: length of the shortest path, or math.inf when unreachable.
    '''

    distance_est = {start: 0}
    predecessor = {start: None}
    p_queue = PriorityQueue()
    p_queue.add(start, heuristic(start))

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            break

        if source == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for neighbor, weight in _neighbors(graph, source):
            new_distance = distance_est[source] + weight
            if new_distance < distance_est.get(neighbor, math.inf):
                distance_est[neighbor] = new_distance
                predecessor[neighbor] = source
                priority = new_distance + heuristic(neighbor)
                p_queue.add(neighbor, priority)

    return [], math.inf
