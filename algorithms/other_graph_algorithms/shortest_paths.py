from data_structures.graph import Graph
from data_structures.heap import MinHeap
from data_structures.matrix import Matrix


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
    
    edge_list = []
    for u in graph.adj.keys():
        for e in graph.neighbors(u):
            edge_list.append((e.u, e.v, e.w))

    if not edge_list:
        return True, d, parent

    edges = Matrix(len(edge_list), 3)
    for i, (u, v, w) in enumerate(edge_list):
        edges.set(i, 0, u)
        edges.set(i, 1, v)
        edges.set(i, 2, w)

    for _ in range(len(graph.adj) - 1):
        for i in range(edges.rows):
            u, v, w = edges.get(i, 0), edges.get(i, 1), edges.get(i, 2)
            if d.get(u, inf_value) < inf_value:
                relax(u, v, w, d, parent)

    for i in range(edges.rows):
        u, v, w = edges.get(i, 0), edges.get(i, 1), edges.get(i, 2)
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
        order: Matrix of vertices in the order they were finalized (heap pops)
        d: dict mapping vertex -> shortest known distance from s
        parent: dict mapping vertex -> predecessor on the shortest path
    """
    d, parent = initialize_single_source(graph, s, inf_value)
    heap = MinHeap()
    visited = {u: False for u in graph.adj.keys()}
    heap.push((0, 0, s))  # (distance, tie-breaker, vertex)
    order_list = []
    tiebreak = 0
    while not heap.is_empty():
        _, _, u = heap.pop()
        if visited.get(u, False):
            continue
        visited[u] = True
        order_list.append(u)
        for e in graph.neighbors(u):
            v = e.v
            if not visited.get(v, False) and d[u] + e.w < d.get(v, inf_value):
                d[v] = d[u] + e.w
                parent[v] = u
                tiebreak += 1
                heap.push((d[v], tiebreak, v))

    order_matrix = Matrix(1, len(order_list))
    for i, vertex in enumerate(order_list):
        order_matrix.set(0, i, vertex)
        
    return order_matrix, d, parent


