from priorityQueue import PriorityQueue
import math


def _graph_and_weights(graph):
    if isinstance(graph, tuple) and len(graph) == 2:
        return graph
    return graph, None


def _edge_weight(edge, weight_mapping):
    if weight_mapping is not None:
        return weight_mapping[edge]

    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _construct_path(predecessor, goal):
    path = [goal]
    vertex = predecessor[goal]
    while not (vertex is None):
        path.insert(0, vertex)
        vertex = predecessor[vertex]
    return path


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm for computing the shortest
    path between two vertices.

    Inputs:
    [graph]: graph.Graph object or (graph.Graph, weight_mapping) pair
    [start]: the source vertex
    [goal]: the target vertex
    [heuristic]: callable that maps a vertex to an estimated distance
                 from that vertex to goal

    Outputs:
    [path]: list of vertices from start to goal. Empty if no path exists
    [length]: length of the shortest path. math.inf if no path exists
    '''
    G, weight_mapping = _graph_and_weights(graph)
    distance_est = {vertex: math.inf for vertex in G.vertices()}

    if start not in distance_est or goal not in distance_est:
        return [], math.inf

    distance_est[start] = 0
    predecessor = {vertex: None for vertex in G.vertices()}
    p_queue = PriorityQueue()
    p_queue.add(start, heuristic(start))

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            return [], math.inf

        if source == goal:
            return _construct_path(predecessor, goal), distance_est[goal]

        for edge in G.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            new_distance = distance_est[source] + _edge_weight(edge, weight_mapping)
            if distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                p_queue.add(destination, new_distance + heuristic(destination))
