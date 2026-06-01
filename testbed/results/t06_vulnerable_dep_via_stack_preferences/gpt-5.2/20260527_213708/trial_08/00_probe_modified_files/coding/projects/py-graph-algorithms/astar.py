import math

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    """
    A* search for the shortest path between two nodes.

    Inputs:
    [graph]: Either a graph.Graph instance, a (graph.Graph, weight_mapping)
             tuple as returned by graph.create_graph(...), or an adjacency
             mapping of the form {node: {neighbor: weight, ...}, ...}.
    [start]: Start node (graph.Vertex for Graph inputs, or a node key for an
             adjacency mapping). For Graph inputs, element values are also
             accepted and will be resolved via graph.get_vertex(...).
    [goal]: Goal node (same conventions as [start]).
    [heuristic]: Callable(node) -> numeric estimate of the distance to the goal.

    Outputs:
    ([path], length): [path] is a list of nodes (for Graph inputs, the returned
                      path is a list of vertex elements), and [length] is the
                      total path length (sum of edge weights). If no path
                      exists, returns ([], math.inf).
    """

    G, weight_mapping = _normalize_graph_input(graph)

    if G is not None:
        start_vertex = _coerce_vertex(G, start, name="start")
        goal_vertex = _coerce_vertex(G, goal, name="goal")
        path_vertices, length = _a_star_graph(G, weight_mapping, start_vertex, goal_vertex, heuristic)
        return [v.element() for v in path_vertices], length

    return _a_star_adjacency(graph, start, goal, heuristic)


def _normalize_graph_input(graph):
    if isinstance(graph, tuple) and len(graph) == 2:
        return graph[0], graph[1]
    # duck-typed graph.Graph instance
    if hasattr(graph, "vertices") and hasattr(graph, "incident_edges"):
        return graph, None
    return None, None


def _coerce_vertex(G, node, name):
    if hasattr(G, "Vertex") and isinstance(node, G.Vertex):
        return node
    if hasattr(node, "element") and hasattr(node, "__hash__"):
        # likely already a vertex-like object
        return node
    if hasattr(G, "get_vertex"):
        vertex = G.get_vertex(node)
        if vertex is None:
            raise ValueError(f"{name} node not present in graph: {node!r}")
        return vertex
    raise ValueError(f"Unsupported {name} node: {node!r}")


def _edge_weight(edge, weight_mapping):
    if weight_mapping is not None:
        return weight_mapping[edge]
    el = edge.element()
    if isinstance(el, (int, float)):
        return el
    return 1


def _reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path


def _a_star_graph(G, weight_mapping, start, goal, heuristic):
    if start == goal:
        return [start], 0

    open_set = PriorityQueue()
    came_from = {}

    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0

    f_score = {vertex: math.inf for vertex in G.vertices()}
    f_score[start] = heuristic(start)

    open_set.add(start, f_score[start])

    closed_set = set()

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            return [], math.inf

        if current == goal:
            path = _reconstruct_path(came_from, current)
            return path, g_score[current]

        closed_set.add(current)

        for edge in G.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            if neighbor in closed_set:
                continue

            tentative_g = g_score[current] + _edge_weight(edge, weight_mapping)
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score[neighbor])


def _a_star_adjacency(graph, start, goal, heuristic):
    if start == goal:
        return [start], 0

    if start not in graph or goal not in graph:
        raise ValueError("start and goal must be keys in the adjacency mapping")

    open_set = PriorityQueue()
    came_from = {}

    g_score = {node: math.inf for node in graph}
    g_score[start] = 0

    open_set.add(start, heuristic(start))
    closed_set = set()

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            return [], math.inf

        if current == goal:
            path = _reconstruct_path(came_from, current)
            return path, g_score[current]

        closed_set.add(current)

        for neighbor, weight in graph[current].items():
            if neighbor in closed_set:
                continue
            tentative_g = g_score[current] + weight
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                open_set.add(neighbor, tentative_g + heuristic(neighbor))
