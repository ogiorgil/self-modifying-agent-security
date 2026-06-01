import heapq
import math
import itertools


def a_star(graph, start, goal, heuristic):
    '''
    A* search for computing a shortest path from start to goal.

    Inputs:
    [graph]: either
             - adjacency mapping: graph[u] -> dict {v: weight} or iterable of
               neighbors (or (neighbor, weight) pairs), or
             - graph.Graph instance from graph.py (treated as unweighted).
    [start]: start node
    [goal]: goal node
    [heuristic]: callable that takes a node and returns an estimate of the
                 distance to goal

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty if unreachable.
    [length]: total path length (math.inf if unreachable)
    '''

    if start == goal:
        return [start], 0

    came_from = {start: None}
    g_score = {start: 0}
    closed = set()
    counter = itertools.count()

    open_heap = []
    heapq.heappush(open_heap, (heuristic(start), 0, next(counter), start))

    while open_heap:
        _, _, _, current = heapq.heappop(open_heap)

        if current in closed:
            continue
        closed.add(current)

        if current == goal:
            path = [goal]
            node = came_from[goal]
            while not (node is None):
                path.insert(0, node)
                node = came_from[node]
            return path, g_score[goal]

        current_g = g_score[current]
        for neighbor, weight in _neighbors(graph, current):
            tentative = current_g + weight
            if tentative < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f_score = tentative + heuristic(neighbor)
                heapq.heappush(open_heap, (f_score, tentative, next(counter), neighbor))

    return [], math.inf


def _neighbors(graph, node):
    '''
    Yield (neighbor, weight) pairs for different graph representations.
    '''

    # graph.Graph representation (from graph.py) - treated as unweighted.
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(node, outgoing=True):
            yield edge.opposite(node), 1
        return

    adj = graph[node]

    # dict adjacency: {neighbor: weight}
    if hasattr(adj, 'items'):
        for neighbor, weight in adj.items():
            yield neighbor, weight
        return

    # list/iter adjacency: neighbor or (neighbor, weight)
    for item in adj:
        if isinstance(item, tuple) and len(item) == 2:
            yield item[0], item[1]
        else:
            yield item, 1
