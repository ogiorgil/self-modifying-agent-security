from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm for computing a shortest path
    between [start] and [goal].

    Inputs:
    [graph]: either a graph.Graph instance, or a tuple (G, w) where
             [G] is a graph.Graph instance and [w] is a weight mapping of edges,
             or an adjacency mapping of the form:
                - {u: {v: weight, ...}, ...}
                - {u: [(v, weight), ...], ...}
                - {u: [v1, v2, ...], ...} (unit weights)
    [start]: start node (graph.Vertex or hashable node in the adjacency mapping)
    [goal]: goal node (graph.Vertex or hashable node in the adjacency mapping)
    [heuristic]: callable h(node) that returns an estimate of the distance
                 from [node] to [goal].

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty list if no path.
    [length]: length of the shortest path. math.inf if no path.
    '''

    G, w = _normalize_graph(graph)

    if start == goal:
        return [start], 0

    g_score = {start: 0}
    predecessor = {start: None}

    open_queue = PriorityQueue()
    open_queue.add(start, heuristic(start))
    closed = set()

    while True:
        try:
            current = open_queue.pop()
        except KeyError:
            break

        if current in closed:
            continue
        closed.add(current)

        if current == goal:
            path = _reconstruct_path(predecessor, goal)
            return path, g_score[goal]

        for neighbor, edge_weight in _neighbors(G, w, current):
            tentative = g_score[current] + edge_weight
            if tentative < g_score.get(neighbor, math.inf):
                g_score[neighbor] = tentative
                predecessor[neighbor] = current
                open_queue.add(neighbor, tentative + heuristic(neighbor))

    return [], math.inf


def _normalize_graph(graph):
    '''
    Return (G, w) pair where:
    - G is either a graph.Graph instance or an adjacency mapping
    - w is either an edge->weight mapping (Graph case) or None
    '''
    if isinstance(graph, tuple) or isinstance(graph, list):
        if len(graph) == 2:
            return graph[0], graph[1]
    return graph, None


def _neighbors(G, w, node):
    '''
    Yield (neighbor, weight) pairs for [node]. Supports both Graph() and
    adjacency mappings.
    '''
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

    if node not in G:
        return

    adj = G[node]
    if isinstance(adj, dict):
        for neighbor in adj:
            yield neighbor, adj[neighbor]
    else:
        for item in adj:
            if isinstance(item, tuple) or isinstance(item, list):
                if len(item) == 2:
                    yield item[0], item[1]
                else:
                    yield item[0], 1
            else:
                yield item, 1


def _reconstruct_path(predecessor, goal):
    path = []
    node = goal
    while not (node is None):
        path.insert(0, node)
        node = predecessor.get(node)
    return path
