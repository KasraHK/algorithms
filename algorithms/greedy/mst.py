from data_structures.graph import Graph, Edge
from data_structures.heap import MinHeap


def prim_mst(graph: Graph, start = 0, inf_value: int = 10**12):
    """Prim's MST algorithm using a min-heap.

    This version supports arbitrary vertex ids (e.g., strings) by using
    dictionaries keyed by vertex id and a heap tie-breaker to avoid
    comparing unlike vertex types.

    Args:
        graph: Graph instance (undirected expected)
        start: starting vertex id
        inf_value: large number used as infinity
    Returns:
        parent: dict mapping vertex -> parent in the MST (None for root)
        key: dict mapping vertex -> connecting edge weight in the MST
        order: list of vertices in the order they were finalized
        mst_edges: list of (parent, vertex, weight) selected in the MST
        total_cost: sum of weights in the MST
    """
    # Use dicts keyed by actual vertex ids to support non-integer labels
    vertices = list(graph.adj.keys())
    if start not in graph.adj:
        graph.adj[start] = []
        vertices.append(start)
    key = {u: inf_value for u in vertices}
    parent = {u: None for u in vertices}
    in_heap = {u: True for u in vertices}
    key[start] = 0
    heap = MinHeap()
    tiebreak = 0
    for v in vertices:
        tiebreak += 1
        heap.push((key[v], tiebreak, v))  # (weight, tie, vertex)
    order = []

    while not heap.is_empty():
        _, _, u = heap.pop()
        if not in_heap.get(u, False):
            continue
        in_heap[u] = False
        order.append(u)
        for e in graph.neighbors(u):
            v = e.v
            if in_heap.get(v, False) and e.w < key.get(v, inf_value):
                key[v] = e.w
                parent[v] = u
                tiebreak += 1
                heap.push((key[v], tiebreak, v))
    # Build explicit MST edge list (parent[v] --key[v]--> v)
    mst_edges = [(pu, v, key[v]) for v, pu in parent.items() if pu is not None]
    total_cost = sum(w for _, _, w in mst_edges)
    return parent, key, order, mst_edges, total_cost


class DisjointSet:
    """Union-Find data structure for Kruskal's algorithm."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


def kruskal_mst(graph: Graph):
    """Kruskal's MST algorithm.

    Args:
        graph: Graph instance (undirected expected)
    Returns:
        mst_edges: list of (u, v, w)
        total_weight: sum of weights in MST
    """
    edges = []
    for u in range(graph.n):
        for e in graph.neighbors(u):
            if graph.directed:
                edges.append((e.w, e.u, e.v))
            else:
                if e.u < e.v:  # avoid duplicates
                    edges.append((e.w, e.u, e.v))
    edges.sort()
    ds = DisjointSet(graph.n)
    mst = []
    total = 0
    for w, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total += w
    return mst, total


