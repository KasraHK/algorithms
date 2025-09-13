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
    """Simple Union-Find data structure that works with any hashable vertex types."""

    def __init__(self, vertices):
        """Initialize with a list of vertices (can be strings, ints, etc.)."""
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, x):
        """Find the root of vertex x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union two vertices. Returns True if they were in different sets."""
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


def kruskal_mst(graph: Graph):
    """Kruskal's MST algorithm that works with arbitrary vertex types.

    Args:
        graph: Graph instance (undirected expected)
    Returns:
        mst_edges: list of (u, v, w)
        total_weight: sum of weights in MST
    """
    # Get all vertices from the adjacency list
    vertices = list(graph.adj.keys())
    
    # Collect all edges
    edges = []
    for u in vertices:
        for e in graph.neighbors(u):
            if graph.directed:
                edges.append((e.w, e.u, e.v))
            else:
                # For undirected graphs, only add each edge once
                # Use a consistent ordering to avoid duplicates
                if str(e.u) <= str(e.v):  # Compare as strings to handle mixed types
                    edges.append((e.w, e.u, e.v))
    
    # Sort edges by weight
    edges.sort()  # we could also do this with a custom insert function
    
    # Initialize disjoint set with all vertices
    ds = DisjointSet(vertices)
    
    mst = []
    total = 0
    for w, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total += w
    return mst, total


