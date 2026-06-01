import heapq
import itertools
import math


def a_star(graph, start, goal, heuristic):
    '''
    A* search algorithm.

    Computes the shortest path from start to goal in a weighted graph,
    using the provided heuristic as an estimate of remaining distance.

    Inputs:
    [graph]: adjacency representation of the graph. Supported formats:
             - dict[node] -> dict[neighbor] = cost
             - dict[node] -> iterable of neighbors (cost defaults to 1)
             - dict[node] -> iterable of (neighbor, cost) pairs
    [start]: start node
    [goal]: goal node
    [heuristic]: callable h(node) returning an estimate of the distance
                 from node to goal.

    Outputs:
    [path]: list of nodes from start to goal (inclusive); empty if no path
    [length]: length of the shortest path (sum of edge costs) or math.inf if no path
    '''

    if start == goal:
        return [start], 0

    counter = itertools.count()
    open_heap = []
    g_score = {start: 0}
    came_from = {start: None}
    closed = set()

    heapq.heappush(open_heap, (heuristic(start), next(counter), start))

    while open_heap:
        _, _, current = heapq.heappop(open_heap)

        if current in closed:
            continue

        if current == goal:
            path = []
            node = current
            while not (node is None):
                path.insert(0, node)
                node = came_from[node]
            return path, g_score[current]

        closed.add(current)

        for neighbor, cost in _iter_neighbors(graph, current):
            if neighbor in closed:
                continue

            tentative = g_score[current] + cost
            if tentative < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f_score = tentative + heuristic(neighbor)
                heapq.heappush(open_heap, (f_score, next(counter), neighbor))

    return [], math.inf


def _iter_neighbors(graph, node):
    neighbors = graph.get(node, None)
    if neighbors is None:
        return ()

    if hasattr(neighbors, 'items'):
        return ((neighbor, cost) for neighbor, cost in neighbors.items())

    def generator():
        for item in neighbors:
            if isinstance(item, tuple) and len(item) == 2:
                yield item[0], item[1]
            else:
                yield item, 1

    return generator()
