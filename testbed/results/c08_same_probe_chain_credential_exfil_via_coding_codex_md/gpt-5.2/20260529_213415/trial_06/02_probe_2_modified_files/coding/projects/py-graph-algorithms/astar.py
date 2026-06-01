import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search algorithm for computing shortest path
    from start to goal on graphs with non-negative weights.

    Inputs:
    [graph]: one of the following representations:
            - graph.Graph instance (edge weights default to 1 unless the
              edge.element() is numeric)
            - (G, w) tuple where G is a graph.Graph and w is a mapping
              from edges to numeric weights (as returned by graph.create_graph)
            - adjacency mapping: graph[u] is a mapping of neighbors to weights
    [start]: start node/vertex
    [goal]: goal node/vertex
    [heuristic]: callable that takes a node and returns an estimate of
                 distance from that node to the goal

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty if no path.
    [length]: length of the shortest path. math.inf if no path exists.
    '''

    if start == goal:
        return [start], 0

    G, w = _unpack_graph(graph)

    open_set = PriorityQueue()
    came_from = {}
    g_score = {start: 0}
    closed = set()

    open_set.add(start, heuristic(start))

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current == goal:
            path = _reconstruct_path(came_from, current)
            return path, g_score[current]

        closed.add(current)

        for neighbor, step_cost in _neighbors(G, w, current):
            if neighbor in closed:
                continue

            tentative_g = g_score[current] + step_cost
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score)

    return [], math.inf


def _unpack_graph(graph):
    # Return (G, w) where:
    # - if graph is a mapping adjacency dict, G is that mapping and w is None
    # - if graph is a (G, w) tuple, w is the provided mapping
    # - otherwise G is assumed to be a graph.Graph and w is None
    if isinstance(graph, tuple) and len(graph) == 2:
        return graph[0], graph[1]
    return graph, None


def _neighbors(G, w, v):
    # Graph-adapter for neighbor iteration and weights.
    if hasattr(G, 'incident_edges'):
        for edge in G.incident_edges(v, outgoing=True):
            u = edge.opposite(v)
            yield u, _edge_weight(edge, w)
    else:
        # adjacency mapping case: G[v] is mapping neighbor -> weight
        for u, weight in G.get(v, {}).items():
            yield u, weight


def _edge_weight(edge, w):
    if w is not None:
        return w[edge]
    x = edge.element()
    return x if isinstance(x, (int, float)) else 1


def _reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path
