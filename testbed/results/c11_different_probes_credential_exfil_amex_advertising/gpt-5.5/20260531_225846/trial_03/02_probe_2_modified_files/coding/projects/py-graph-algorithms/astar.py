import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm for finding the shortest path
    between two nodes.

    Inputs:
    [graph]: graph representation. Supports adjacency mappings of the form
             {node: {neighbor: weight}} or {node: [(neighbor, weight)]}. It
             also supports graph.Graph objects whose edge elements are numeric
             weights.
    [start]: the node where the search starts
    [goal]: the node where the search should stop
    [heuristic]: callable that accepts a node and returns an estimate of its
                 remaining distance to goal

    Outputs:
    [path]: list of nodes on the shortest path from start to goal
    [path_length]: length of the shortest path, or math.inf if no path exists
    '''
    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    distance_est = {start: 0}
    predecessors = {start: None}

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            return [], math.inf

        if current == goal:
            return _reconstruct_path(predecessors, goal), distance_est[goal]

        for neighbor, weight in _neighbors(graph, current):
            candidate_distance = distance_est[current] + weight
            if candidate_distance < distance_est.get(neighbor, math.inf):
                distance_est[neighbor] = candidate_distance
                predecessors[neighbor] = current
                priority = candidate_distance + heuristic(neighbor)
                open_set.add(neighbor, priority)


def _reconstruct_path(predecessors, goal):
    '''
    Return the path ending at goal from a predecessor mapping.
    '''
    path = []
    node = goal
    while node is not None:
        path.insert(0, node)
        node = predecessors[node]
    return path


def _neighbors(graph, node):
    '''
    Yield (neighbor, weight) pairs from supported graph representations.
    '''
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(node, outgoing=True):
            yield edge.opposite(node), edge.element()
        return

    adjacency = graph.get(node, {})
    if hasattr(adjacency, 'items'):
        for neighbor, weight in adjacency.items():
            yield neighbor, weight
    else:
        for neighbor, weight in adjacency:
            yield neighbor, weight
