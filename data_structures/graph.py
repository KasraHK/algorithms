"""Lightweight graph representation and utilities.

Graph supports arbitrary vertex ids (ints, strings, etc.). Adjacency is
stored as a dict: vertex -> list of outgoing `Edge` objects. Some algorithms
that produce matrices (e.g., Floyd–Warshall via adjacency matrix) still
assume integer vertex ids in [0, n-1]. For those, either use integer ids or
add a mapping layer.
"""

from data_structures.matrix import Matrix


class Edge:
    """Edge in a graph.

    Attributes:
        u: source vertex id
        v: destination vertex id
        w: weight (defaults to 1)
        directed: whether edge is directed
    """

    def __init__(self, u, v, w=1, directed=True):
        self.u = u
        self.v = v
        self.w = w
        self.directed = directed

    def __repr__(self):
        br = "->" if self.directed else "{}"
        return f"{self.u}{br}{self.v}:{self.w}"


class Graph:
    """Graph supporting adjacency list and adjacency matrix views.

    Vertex ids are assumed to be integers in [0, n-1].
    """

    def __init__(self, num_vertices: int, directed: bool = True):
        self.n = num_vertices
        self.directed = directed
        # Allow dynamic vertex ids: precreate 0..n-1, but permit new keys later
        self.adj = {i: [] for i in range(num_vertices)}

    def add_edge(self, u, v, w: int = 1):
        # Ensure vertices exist in adjacency
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        e = Edge(u, v, w, directed=self.directed)
        self.adj[u].append(e)
        if not self.directed:
            # store reverse edge as well for undirected adjacency convenience
            self.adj[v].append(Edge(v, u, w, directed=self.directed))

    def neighbors(self, u: int):
        return self.adj[u]

    def to_adjacency_matrix(self, inf_value: int = 10**12) -> Matrix:
        m = Matrix(self.n, self.n, inf_value)
        for i in range(self.n):
            m.set(i, i, 0)
        for u in range(self.n):
            for e in self.adj[u]:
                m.set(e.u, e.v, e.w)
        return m


