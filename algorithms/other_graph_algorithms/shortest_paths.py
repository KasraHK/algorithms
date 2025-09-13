from data_structures.graph import Graph
from data_structures.heap import MinHeap


def initialize_single_source(graph: Graph, s, inf_value: int = 10**12):
    """Initialize distance and parent dicts keyed by vertex ids.

    Args:
        graph: Graph instance whose vertices are taken from graph.adj keys
        s: source vertex id (must be a key present or later added)
        inf_value: value used to represent infinity

    Returns:
        d: dict mapping vertex -> distance (d[s]=0, others inf_value)
        parent: dict mapping vertex -> predecessor on shortest path (None for s)
    """
    d = {u: inf_value for u in graph.adj.keys()}
    parent = {u: None for u in graph.adj.keys()}
    d[s] = 0
    return d, parent


def relax(u, v, w: int, d, parent):
    """Relax edge (u, v) with weight w.

    Updates d[v] and parent[v] if d[u] + w is an improvement.

    Args:
        u: tail vertex id
        v: head vertex id
        w: edge weight
        d: distance dict (vertex -> current best distance)
        parent: parent dict (vertex -> predecessor)
    """
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        parent[v] = u


def bellman_ford(graph: Graph, s, inf_value: int = 10**12):
    """Bellman–Ford algorithm for graphs with negative weights.

    Supports arbitrary vertex ids (e.g., strings) by using dicts keyed by
    vertex id. Detects negative-weight cycles reachable from the source.

    Args:
        graph: Graph instance (directed or undirected)
        s: source vertex id
        inf_value: infinity sentinel for unreachable vertices

    Returns:
        ok: bool, False if a negative-weight cycle is detected; True otherwise
        d: dict mapping vertex -> shortest known distance from s
        parent: dict mapping vertex -> predecessor on the shortest path
    """
    d, parent = initialize_single_source(graph, s, inf_value)
    edges = []
    for u in graph.adj.keys():
        for e in graph.neighbors(u):
            edges.append((e.u, e.v, e.w))
    for _ in range(len(graph.adj) - 1):
        for u, v, w in edges:
            if d.get(u, inf_value) < inf_value:
                relax(u, v, w, d, parent)
    for u, v, w in edges:
        if d.get(u, inf_value) + w < d.get(v, inf_value):
            return False, d, parent
    return True, d, parent


def dijkstra(graph: Graph, s, inf_value: int = 10**12):
    """Dijkstra's algorithm (non-negative weights) using a min-heap.

    Uses dicts keyed by vertex id and a (distance, tie, vertex) heap tuple to
    avoid comparing unlike vertex types. Stops when all reachable vertices are
    finalized.

    Args:
        graph: Graph instance with non-negative edge weights
        s: source vertex id
        inf_value: infinity sentinel for unreachable vertices

    Returns:
        order: list of vertices in the order they were finalized (heap pops)
        d: dict mapping vertex -> shortest known distance from s
        parent: dict mapping vertex -> predecessor on the shortest path
    """
    d, parent = initialize_single_source(graph, s, inf_value)
    heap = MinHeap()
    visited = {u: False for u in graph.adj.keys()}
    heap.push((0, 0, s))  # (distance, tie-breaker, vertex)
    order = []
    tiebreak = 0
    while not heap.is_empty():
        _, _, u = heap.pop()
        if visited[u]:
            continue
        visited[u] = True
        order.append(u)
        for e in graph.neighbors(u):
            v = e.v
            if not visited[v] and d[u] + e.w < d.get(v, inf_value):
                d[v] = d[u] + e.w
                parent[v] = u
                tiebreak += 1
                heap.push((d[v], tiebreak, v))
    return order, d, parent


