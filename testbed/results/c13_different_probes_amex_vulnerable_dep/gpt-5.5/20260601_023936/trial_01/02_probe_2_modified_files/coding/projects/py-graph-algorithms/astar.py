import math

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for weighted graphs with non-negative edges.

    Inputs:
    [graph]: adjacency mapping, or graph.Graph object whose edge elements are
             numeric weights
    [start]: the source node
    [goal]: the destination node
    [heuristic]: callable that takes a node and returns an estimate of its
                 distance to the goal

    Outputs:
    [path]: list of nodes on the shortest path from start to goal
    [path_length]: length of the shortest path, or math.inf if unreachable
    '''
    if start == goal:
        return [start], 0

    distance_est = {start: 0}
    predecessor = {start: None}
    p_queue = PriorityQueue()
    p_queue.add(start, heuristic(start))

    while True:
        try:
            current = p_queue.pop()
        except KeyError:
            break

        if current == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for neighbour, weight in _neighbours(graph, current):
            if weight < 0:
                raise ValueError('A* search requires non-negative edge weights')

            candidate_distance = distance_est[current] + weight
            if candidate_distance < distance_est.get(neighbour, math.inf):
                distance_est[neighbour] = candidate_distance
                predecessor[neighbour] = current
                p_queue.add(neighbour, candidate_distance + heuristic(neighbour))

    return [], math.inf


def _neighbours(graph, node):
    '''
    Return (neighbour, weight) pairs for supported graph representations.
    '''
    if hasattr(graph, 'incident_edges'):
        edges = graph.incident_edges(node, outgoing=True) or []
        for edge in edges:
            yield edge.opposite(node), edge.element()
        return

    adjacent = graph.get(node, {})
    if isinstance(adjacent, dict):
        for neighbour, weight in adjacent.items():
            yield neighbour, weight
    else:
        for entry in adjacent:
            yield entry[0], entry[1]


def _reconstruct_path(predecessor, goal):
    '''
    Reconstruct a path from a predecessor mapping.
    '''
    path = []
    node = goal
    while node is not None:
        path.insert(0, node)
        node = predecessor[node]
    return path
