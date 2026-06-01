import heapq
import itertools
import math


def a_star(graph, start, goal, heuristic):
    '''
    A* search for shortest path in a weighted graph.

    Inputs:
    [graph]: one of:
             - an adjacency mapping: graph[u] -> {v: weight} or [(v, weight), ...]
             - a graph.Graph instance (or a (G, w) tuple where w maps edges to weights)
    [start]: start node (key in adjacency mapping, or graph.Vertex instance)
    [goal]: goal node (key in adjacency mapping, or graph.Vertex instance)
    [heuristic]: callable taking a node and returning a numeric estimate of
                 distance from that node to goal

    Outputs:
    [path]: list of nodes from start to goal (inclusive), or None if unreachable
    [length]: numeric length of the shortest path, or math.inf if unreachable
    '''

    if start == goal:
        return [start], 0

    G, w = _normalize_graph(graph)

    g_score = {start: 0}
    came_from = {start: None}
    closed = set()

    counter = itertools.count()
    open_heap = []
    heapq.heappush(open_heap, (heuristic(start), 0, next(counter), start))

    while open_heap:
        _, current_g, _, current = heapq.heappop(open_heap)
        if current in closed:
            continue

        if current == goal:
            path = _reconstruct_path(came_from, goal)
            return path, current_g

        closed.add(current)

        for neighbor, weight in _iter_neighbors(G, w, current):
            if weight < 0:
                raise ValueError('A* requires non-negative edge weights')

            tentative_g = current_g + weight
            if tentative_g < g_score.get(neighbor, math.inf):
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current
                f_score = tentative_g + heuristic(neighbor)
                heapq.heappush(open_heap, (f_score, tentative_g, next(counter), neighbor))

    return None, math.inf


def _normalize_graph(graph):
    if isinstance(graph, tuple) and len(graph) == 2:
        return graph[0], graph[1]
    return graph, None


def _iter_neighbors(graph, weight_mapping, node):
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(node, outgoing=True):
            neighbor = edge.opposite(node)
            weight = _edge_weight(edge, weight_mapping)
            yield neighbor, weight
        return

    neighbors = graph.get(node, {})
    if isinstance(neighbors, dict):
        for neighbor, weight in neighbors.items():
            yield neighbor, weight
        return

    for item in neighbors:
        neighbor, weight = item
        yield neighbor, weight


def _edge_weight(edge, weight_mapping):
    if weight_mapping is not None:
        return weight_mapping[edge]
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    raise ValueError('Graph edges must have numeric weights (or pass (G, w) as graph)')


def _reconstruct_path(came_from, goal):
    path = [goal]
    node = came_from.get(goal)
    while node is not None:
        path.insert(0, node)
        node = came_from.get(node)
    return path
