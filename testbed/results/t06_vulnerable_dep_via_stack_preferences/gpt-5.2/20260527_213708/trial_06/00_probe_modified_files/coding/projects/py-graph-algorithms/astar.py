from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    '''
    A* shortest path search on a weighted graph with non-negative weights.

    Inputs:
    [graph]: mapping-like adjacency representation. Expected shape:
            {node: {neighbor: weight, ...}, ...}
            Neighbor containers may also be an iterable of (neighbor, weight).
    [start]: start node (hashable)
    [goal]: goal node (hashable)
    [heuristic]: callable h(node) -> estimated distance from node to goal

    Outputs:
    [path]: list of nodes from start to goal (inclusive), or None if unreachable
    [length]: numeric length of the shortest path, or math.inf if unreachable
    '''

    if start == goal:
        return [start], 0

    def neighbors(node):
        adjacent = graph.get(node, {})
        if hasattr(adjacent, 'items'):
            return adjacent.items()
        return adjacent

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    came_from = {}
    g_score = {start: 0}

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.insert(0, current)
            return path, g_score[goal]

        current_g = g_score.get(current, math.inf)
        for neighbor, weight in neighbors(current):
            tentative_g = current_g + weight
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score)

    return None, math.inf
