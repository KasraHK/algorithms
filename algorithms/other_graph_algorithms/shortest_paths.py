from data_structures.graph import Graph
from data_structures.heap import MinHeap


def initialize_single_source(graph: Graph, s: int, inf_value: int = 10**12):
    """Initialize d and parent for shortest-path algorithms."""
    n = graph.n
    d = [inf_value] * n
    parent = [None] * n
    d[s] = 0
    return d, parent


def relax(u: int, v: int, w: int, d, parent):
    """Relax edge (u, v) with weight w."""
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        parent[v] = u


def bellman_ford(graph: Graph, s: int, inf_value: int = 10**12):
    """Bellman-Ford algorithm for graphs with negative weights.

    Returns:
        (ok, d, parent): ok=False if negative cycle detected
    """
    d, parent = initialize_single_source(graph, s, inf_value)
    n = graph.n
    edges = []
    for u in range(n):
        for e in graph.neighbors(u):
            edges.append((e.u, e.v, e.w))
    for _ in range(n - 1):
        for u, v, w in edges:
            if d[u] < inf_value:
                relax(u, v, w, d, parent)
    for u, v, w in edges:
        if d[u] + w < d[v]:
            return False, d, parent
    return True, d, parent


def dijkstra(graph: Graph, s: int, inf_value: int = 10**12):
    """Dijkstra's algorithm using min-heap for non-negative weights.

    Returns:
        order: extraction order, d: distances, parent: parents
    """
    d, parent = initialize_single_source(graph, s, inf_value)
    heap = MinHeap()
    visited = [False] * graph.n
    heap.push((0, s))
    order = []
    while not heap.is_empty():
        du, u = heap.pop()
        if visited[u]:
            continue
        visited[u] = True
        order.append(u)
        for e in graph.neighbors(u):
            v = e.v
            if not visited[v] and d[u] + e.w < d[v]:
                d[v] = d[u] + e.w
                parent[v] = u
                heap.push((d[v], v))
    return order, d, parent


