from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    '''
    A* search for shortest path finding.

    Inputs:
    [graph]: either a graph.Graph instance (treat all edges as weight 1),
             or a (G, w) pair where G is a graph.Graph and w is a mapping
             of edges to weights (as returned by graph.create_graph(...)).
    [start]: the source vertex (typically a graph.Vertex instance of G).
    [goal]: the destination vertex (typically a graph.Vertex instance of G).
    [heuristic]: a callable that takes a node and returns a numeric estimate
                 of the remaining distance to the goal.

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty if unreachable.
    [length]: length of the shortest path (math.inf if unreachable).
    '''

    if start == goal:
        return [start], 0

    if isinstance(graph, (tuple, list)) and len(graph) == 2 and isinstance(graph[1], dict):
        G, w = graph
    else:
        G, w = graph, None

    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0
    came_from = {start: None}

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current == goal:
            path = [current]
            while came_from[path[0]] is not None:
                path.insert(0, came_from[path[0]])
            return path, g_score[goal]

        incident = G.incident_edges(current, outgoing=True)
        if incident is None:
            continue

        for edge in incident:
            neighbor = edge.opposite(current)
            weight = w.get(edge, 1) if w is not None else 1
            tentative = g_score[current] + weight

            if tentative < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f_score = tentative + heuristic(neighbor)
                open_set.add(neighbor, f_score)

    return [], math.inf
