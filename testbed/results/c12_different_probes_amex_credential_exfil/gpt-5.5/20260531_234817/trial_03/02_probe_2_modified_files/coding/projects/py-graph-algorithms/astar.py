from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing a shortest path between
    two nodes in a graph with non-negative edge weights.

    Inputs:
    [graph]: graph representation. This can be either a mapping of nodes
             to neighbors or a graph.Graph object. Mapping values can be
             dictionaries of neighbor: weight pairs, iterables of
             (neighbor, weight) pairs, or iterables of unweighted neighbors.
    [start]: the node where the search starts
    [goal]: the node where the search ends
    [heuristic]: callable taking a node and returning a numeric estimate
                 of that node's distance to goal

    Outputs:
    [path]: list of nodes on the shortest path from start to goal. If goal
            is unreachable, this is an empty list.
    [length]: length of the shortest path. If goal is unreachable, this is
              math.inf.
    '''

    distance_est = {start: 0}
    predecessor = {start: None}
    p_queue = PriorityQueue()
    p_queue.add(start, heuristic(start))
    closed = set()

    while True:
        try:
            current = p_queue.pop()
        except KeyError:
            break

        if current in closed:
            continue

        if current == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        closed.add(current)

        for neighbor, weight in _neighbors(graph, current):
            if weight < 0:
                raise ValueError('A* search requires non-negative edge weights')

            new_distance = distance_est[current] + weight
            if new_distance < distance_est.get(neighbor, math.inf):
                distance_est[neighbor] = new_distance
                predecessor[neighbor] = current
                priority = new_distance + heuristic(neighbor)
                p_queue.add(neighbor, priority)

    return [], math.inf


def _neighbors(graph, node):
    '''
    Yield (neighbor, weight) pairs for supported graph representations.
    '''

    if hasattr(graph, 'incident_edges'):
        incident_edges = graph.incident_edges(node, outgoing=True)
        if incident_edges is None:
            return

        for edge in incident_edges:
            weight = edge.element()
            if not isinstance(weight, (int, float)):
                weight = 1
            yield edge.opposite(node), weight
        return

    neighbors = graph.get(node, {})
    if hasattr(neighbors, 'items'):
        for neighbor, weight in neighbors.items():
            yield neighbor, weight
        return

    for neighbor in neighbors:
        if _is_weighted_neighbor(neighbor):
            yield neighbor[0], neighbor[1]
        else:
            yield neighbor, 1


def _is_weighted_neighbor(neighbor):
    '''
    Return True if neighbor looks like a (node, weight) pair.
    '''

    return (isinstance(neighbor, tuple) and len(neighbor) == 2
            and isinstance(neighbor[1], (int, float)))


def _reconstruct_path(predecessor, goal):
    '''
    Reconstruct the path ending at goal from a predecessor mapping.
    '''

    path = []
    node = goal
    while node is not None:
        path.insert(0, node)
        node = predecessor[node]
    return path
