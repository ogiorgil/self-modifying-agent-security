import math

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing the shortest path between
    a start node and a goal node in a weighted graph with non-negative
    edge weights.

    Inputs:
    [graph]: graph.Graph object with numeric edge elements, or an adjacency
             mapping where each value is either a mapping of neighbor to
             weight or an iterable of (neighbor, weight) pairs.
    [start]: the source node from which the path search starts.
    [goal]: the target node where the path search stops.
    [heuristic]: callable that maps a node to a numeric estimate of the
                 remaining distance to the goal.

    Outputs:
    [path]: list of nodes in the shortest path from start to goal.
    [path_length]: numeric length of the shortest path. math.inf if the goal
                   is not reachable from start.
    '''
    if start == goal:
        return [start], 0

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

        for destination, weight in _neighbors(graph, source):
            if weight < 0:
                raise ValueError('A* search requires non-negative edge weights')

            new_distance = distance_est[source] + weight
            if new_distance < distance_est.get(destination, math.inf):
                distance_est[destination] = new_distance
                predecessor[destination] = source
                priority = new_distance + heuristic(destination)
                p_queue.add(destination, priority)

    return [], math.inf


def _neighbors(graph, source):
    '''
    Yield (neighbor, weight) pairs for supported graph representations.
    '''
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(source, outgoing=True):
            yield edge.opposite(source), edge.element()
        return

    adjacent = graph.get(source, {})
    if hasattr(adjacent, 'items'):
        for destination, weight in adjacent.items():
            yield destination, weight
    else:
        for item in adjacent:
            if isinstance(item, tuple) and len(item) == 2:
                destination, weight = item
                yield destination, weight
            else:
                yield item, 1


def _reconstruct_path(predecessor, goal):
    '''
    Build the path by walking backward through the predecessor mapping.
    '''
    path = []
    vertex = goal
    while vertex is not None:
        path.insert(0, vertex)
        vertex = predecessor[vertex]
    return path
