import heapq
import math


def _neighbors(graph, node):
    '''
    Return (neighbor, weight) pairs from common adjacency-list shapes.
    '''
    adjacent = graph.get(node, {})

    if hasattr(adjacent, 'items'):
        return adjacent.items()

    return adjacent


def a_star(graph, start, goal, heuristic):
    '''
    Compute the shortest path from start to goal with A* search.

    Inputs:
    [graph]: mapping of nodes to adjacent weighted edges. Adjacent edges may be
             represented as {neighbor: weight} mappings or as iterable
             (neighbor, weight) pairs.
    [start]: source node.
    [goal]: target node.
    [heuristic]: callable returning an estimated distance from a node to goal.

    Outputs:
    [path]: list of nodes on the shortest path from start to goal.
    [distance]: length of the shortest path. If goal is unreachable, returns
                math.inf with an empty path.
    '''
    if start == goal:
        return [start], 0

    distance_est = {start: 0}
    predecessor = {start: None}
    frontier = []
    heapq.heappush(frontier, (heuristic(start), 0, start))
    counter = 1

    while frontier:
        _, _, source = heapq.heappop(frontier)

        if source == goal:
            path = [source]
            vertex = predecessor[source]
            while vertex is not None:
                path.insert(0, vertex)
                vertex = predecessor[vertex]
            return path, distance_est[source]

        for destination, weight in _neighbors(graph, source):
            candidate_distance = distance_est[source] + weight
            if candidate_distance < distance_est.get(destination, math.inf):
                distance_est[destination] = candidate_distance
                predecessor[destination] = source
                priority = candidate_distance + heuristic(destination)
                heapq.heappush(frontier, (priority, counter, destination))
                counter += 1

    return [], math.inf
