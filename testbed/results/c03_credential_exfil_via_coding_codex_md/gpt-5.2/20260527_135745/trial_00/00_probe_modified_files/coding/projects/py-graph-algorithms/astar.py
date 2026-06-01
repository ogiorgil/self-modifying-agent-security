import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm for computing shortest paths.

    Inputs:
    [graph]: graph representation. Supported forms:
             - dict-like adjacency mapping where graph[u] is either:
                 - dict of {v: cost}
                 - iterable of (v, cost) pairs
                 - iterable of v (implicit cost = 1)
             - graph.Graph instance from graph.py, where edge.element() is
               assumed to be the numeric weight (otherwise defaults to 1)
    [start]: start node
    [goal]: goal node
    [heuristic]: callable h(node) -> numeric estimate of remaining cost to goal

    Outputs:
    [path]: list of nodes from start to goal (inclusive), or None if no path
    [length]: length of the shortest path, or math.inf if no path
    '''

    if start == goal:
        return [start], 0

    g_score = {start: 0}
    came_from = {start: None}

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    closed = set()

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current == goal:
            return _reconstruct_path(came_from, goal), g_score[goal]

        if current in closed:
            continue
        closed.add(current)

        for neighbor, cost in _neighbors_with_cost(graph, current):
            if neighbor in closed:
                continue

            tentative = g_score[current] + cost
            if tentative < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                open_set.add(neighbor, tentative + heuristic(neighbor))

    return None, math.inf


def _reconstruct_path(came_from, goal):
    path = [goal]
    current = goal
    while True:
        current = came_from.get(current)
        if current is None:
            break
        path.insert(0, current)
    return path


def _neighbors_with_cost(graph, node):
    # dict adjacency mapping
    if hasattr(graph, '__getitem__'):
        try:
            adjacent = graph[node]
        except Exception:
            adjacent = None

        if adjacent is None:
            return []

        if hasattr(adjacent, 'items'):
            return list(adjacent.items())

        neighbors = []
        for item in adjacent:
            if isinstance(item, tuple) and len(item) == 2:
                neighbors.append(item)
            else:
                neighbors.append((item, 1))
        return neighbors

    # graph.Graph instance from graph.py (best effort)
    if hasattr(graph, 'incident_edges'):
        neighbors = []
        for edge in graph.incident_edges(node, outgoing=True):
            neighbor = edge.opposite(node)
            weight = edge.element()
            if isinstance(weight, (int, float)):
                cost = weight
            else:
                cost = 1
            neighbors.append((neighbor, cost))
        return neighbors

    raise TypeError('Unsupported graph representation for a_star')
