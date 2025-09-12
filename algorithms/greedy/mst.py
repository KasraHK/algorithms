from data_structures.graph import Graph, Edge
from data_structures.heap import MinHeap


def prim_mst(graph: Graph, start: int = 0, inf_value: int = 10**12):
    """Prim's MST algorithm using a min-heap.

    Args:
        graph: Graph instance (undirected expected)
        start: starting vertex id
        inf_value: large number used as infinity
    Returns:
        parent: list where parent[v] is the parent of v in MST (or -1)
        key: list of min edge weight to connect each vertex
        order: list of extraction order from heap
    """
    n = graph.n
    key = [inf_value] * n
    parent = [-1] * n
    in_heap = [True] * n
    key[start] = 0
    heap = MinHeap()
    for v in range(n):
        heap.push((key[v], v))
    order = []

    while not heap.is_empty():
        k, u = heap.pop()
        if not in_heap[u]:
            continue
        in_heap[u] = False
        order.append(u)
        for e in graph.neighbors(u):
            v = e.v
            if in_heap[v] and e.w < key[v]:
                key[v] = e.w
                parent[v] = u
                heap.push((key[v], v))
    return parent, key, order


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


