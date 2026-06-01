import math
from priorityQueue import PriorityQueue


def _edge_cost(edge):
    '''
    Return numeric cost of traversing an edge.

    For Graph edges created by graph.create_graph(), edge.element() is a string,
    so this defaults to cost 1. If the edge element is numeric, it is treated
    as the edge cost.
    '''
    try:
        cost = edge.element()
    except Exception:
        return 1
    return cost if isinstance(cost, (int, float)) else 1


def _neighbors(graph, node):
    '''
    Yield (neighbor, cost) pairs for a given node.

    Supports:
    - graph.Graph-like objects that expose incident_edges(v, outgoing=True)
    - adjacency mappings:
        - graph[node] -> {neighbor: cost, ...}
        - graph[node] -> [(neighbor, cost), ...]
        - graph[node] -> [neighbor, ...] (cost defaults to 1)
    '''
    if hasattr(graph, "incident_edges"):
        for edge in graph.incident_edges(node, outgoing=True):
            yield edge.opposite(node), _edge_cost(edge)
        return

    try:
        adj = graph[node]
    except Exception:
        adj = graph.get(node, ()) if hasattr(graph, "get") else ()

    if isinstance(adj, dict):
        for neighbor, cost in adj.items():
            yield neighbor, cost
        return

    for item in adj:
        if isinstance(item, tuple) and len(item) >= 2:
            yield item[0], item[1]
        else:
            yield item, 1


def a_star(graph, start, goal, heuristic):
    '''
    A* search for shortest path.

    Inputs:
    [graph]: graph.Graph instance (see graph.py) or an adjacency mapping
    [start]: start node (Graph.Vertex or hashable node key)
    [goal]: goal node (same type as start)
    [heuristic]: callable taking a node and returning an estimated distance
                 from that node to the goal

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty if unreachable.
    [length]: total path length. math.inf if unreachable.
    '''

    if start == goal:
        return [start], 0

    open_set = PriorityQueue()
    came_from = {start: None}
    g_score = {start: 0}
    closed = set()

    open_set.add(start, heuristic(start))

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current in closed:
            continue
        closed.add(current)

        if current == goal:
            path = [current]
            while came_from[path[0]] is not None:
                path.insert(0, came_from[path[0]])
            return path, g_score[current]

        current_g = g_score.get(current, math.inf)
        for neighbor, cost in _neighbors(graph, current):
            tentative_g = current_g + cost
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                open_set.add(neighbor, tentative_g + heuristic(neighbor))

    return [], math.inf
