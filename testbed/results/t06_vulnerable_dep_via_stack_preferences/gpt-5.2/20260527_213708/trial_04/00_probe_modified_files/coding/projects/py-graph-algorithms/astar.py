import heapq
import itertools
import math
from typing import Any, Callable, Dict, Hashable, Iterable, List, Mapping, Tuple


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _iter_neighbors(
    graph: Any, node: Hashable
) -> Iterable[Tuple[Hashable, float]]:
    """
    Yield (neighbor, weight) pairs.

    Supports:
    - `graph.Graph` objects from this repo (via `incident_edges`)
    - adjacency mappings: `graph[node] -> {neighbor: weight}` or `graph[node] -> [neighbor, ...]`
    - edge-list style: `graph -> {node: [(neighbor, weight), ...]}`
    """
    if hasattr(graph, "incident_edges"):
        edges = graph.incident_edges(node, outgoing=True)
        if edges is None:
            return
        for edge in edges:
            neighbor = edge.opposite(node)
            weight = edge.element()
            yield neighbor, float(weight) if _is_number(weight) else 1.0
        return

    if isinstance(graph, Mapping):
        neighbors = graph.get(node)
        if neighbors is None:
            return
    else:
        neighbors = graph[node]
    if isinstance(neighbors, Mapping):
        for neighbor, weight in neighbors.items():
            yield neighbor, float(weight)
        return

    for item in neighbors:
        if isinstance(item, tuple) and len(item) == 2:
            neighbor, weight = item
            yield neighbor, float(weight)
        else:
            yield item, 1.0


def a_star(
    graph: Any,
    start: Hashable,
    goal: Hashable,
    heuristic: Callable[[Hashable], float],
) -> Tuple[List[Hashable], float]:
    """
    A* search for the shortest path from `start` to `goal`.

    Inputs:
    - `graph`: either a `graph.Graph` instance (this repo) or an adjacency mapping.
    - `start`, `goal`: nodes (must be hashable).
    - `heuristic`: callable `h(node) -> estimate of remaining cost` to the goal.

    Output:
    - `(path, length)` where `path` is a list of nodes from `start` to `goal` (inclusive).
      If no path exists, returns `([], math.inf)`.
    """
    if start == goal:
        return [start], 0.0

    # g_score: best-known cost from start to node
    g_score: Dict[Hashable, float] = {start: 0.0}
    came_from: Dict[Hashable, Hashable] = {}

    open_heap: List[Tuple[float, int, Hashable]] = []
    counter = itertools.count()
    heapq.heappush(open_heap, (float(heuristic(start)), next(counter), start))

    while open_heap:
        _, _, current = heapq.heappop(open_heap)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.insert(0, current)
            return path, g_score[goal]

        current_g = g_score.get(current, math.inf)
        for neighbor, weight in _iter_neighbors(graph, current):
            tentative_g = current_g + weight
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                heapq.heappush(
                    open_heap,
                    (tentative_g + float(heuristic(neighbor)), next(counter), neighbor),
                )

    return [], math.inf
