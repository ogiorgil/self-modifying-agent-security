import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* shortest path algorithm.

    Inputs:
    [graph]: either a mapping representing adjacency, or a (G, w) tuple where:
             - G is a graph.Graph instance
             - w is a mapping of graph.Edge instances to edge weights
    [start]: start node (or graph.Vertex instance)
    [goal]: goal node (or graph.Vertex instance)
    [heuristic]: callable that takes a node and returns an estimate of the
                 remaining distance to the goal.

    Outputs:
    [path]: list of nodes from start to goal (inclusive), or None if unreachable
    [length]: total length of the shortest path, or math.inf if unreachable
    '''

    G, w = _normalize_graph(graph)

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

        closed.add(current)

        for neighbor, step_cost in _iter_neighbors(G, w, current):
            if neighbor in closed:
                continue

            tentative_g = g_score[current] + step_cost
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                open_set.add(neighbor, tentative_g + heuristic(neighbor))

    return None, math.inf


def _normalize_graph(graph):
    if isinstance(graph, tuple) or isinstance(graph, list):
        if len(graph) != 2:
            raise TypeError('Expected (G, w) tuple/list for Graph input.')
        return graph[0], graph[1]
    return graph, None


def _iter_neighbors(G, w, node):
    # graph.Graph style
    if hasattr(G, 'incident_edges'):
        edges = G.incident_edges(node, outgoing=True)
        if edges is None:
            return
        for edge in edges:
            neighbor = edge.opposite(node)
            if w is None:
                yield neighbor, 1
            else:
                yield neighbor, w[edge]
        return

    # adjacency-map style
    neighbors = G.get(node, None) if hasattr(G, 'get') else None
    if neighbors is None:
        return

    if isinstance(neighbors, dict):
        for neighbor, cost in neighbors.items():
            yield neighbor, cost
        return

    for item in neighbors:
        if isinstance(item, tuple) or isinstance(item, list):
            if len(item) == 2:
                yield item[0], item[1]
            elif len(item) == 1:
                yield item[0], 1
            else:
                raise TypeError('Adjacency list items must be (neighbor, cost).')
        else:
            yield item, 1


def _reconstruct_path(came_from, goal):
    path = [goal]
    current = goal
    while True:
        current = came_from.get(current)
        if current is None:
            break
        path.insert(0, current)
    return path
