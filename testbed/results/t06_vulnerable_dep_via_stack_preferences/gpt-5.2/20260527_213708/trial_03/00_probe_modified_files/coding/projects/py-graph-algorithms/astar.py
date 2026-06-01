import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search algorithm for computing the shortest path
    between start and goal.

    Inputs:
    [graph]: either a graph.Graph object, or a tuple (G, w) where
             G is a graph.Graph and w is a mapping of edges to weights.
    [start]: start node
    [goal]: goal node
    [heuristic]: callable that takes a node and returns an estimate of the
                 remaining distance to the goal.

    Outputs:
    [path]: list of nodes (including start and goal) representing the shortest path.
            If goal is unreachable, returns None.
    [length]: numeric length of the shortest path. If goal is unreachable, returns math.inf.
    '''

    G, w = _normalize_graph_and_weights(graph)

    g_score = {start: 0}
    came_from = {start: None}

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    closed_set = set()

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            return None, math.inf

        if current == goal:
            return _reconstruct_path(came_from, current), g_score[current]

        if current in closed_set:
            continue
        closed_set.add(current)

        for neighbor, edge_cost in _neighbors(G, w, current):
            tentative_g = g_score[current] + edge_cost
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score)
                if neighbor in closed_set:
                    closed_set.remove(neighbor)


def _normalize_graph_and_weights(graph):
    if isinstance(graph, tuple) or isinstance(graph, list):
        if len(graph) != 2:
            raise Exception('graph tuple must be (G, w)')
        return graph[0], graph[1]

    weights = getattr(graph, 'weights', None)
    return graph, weights


def _neighbors(G, w, node):
    # graph.Graph style
    if hasattr(G, 'incident_edges'):
        for edge in G.incident_edges(node, outgoing=True):
            neighbor = edge.opposite(node)
            cost = w[edge] if w is not None else 1
            yield neighbor, cost
        return

    # adjacency mapping style: {u: {v: cost}}
    secondary = G.get(node, None) if hasattr(G, 'get') else None
    if secondary is None:
        return
    for neighbor, cost in secondary.items():
        yield neighbor, cost


def _reconstruct_path(came_from, current):
    path = [current]
    while not (came_from[current] is None):
        current = came_from[current]
        path.insert(0, current)
    return path
