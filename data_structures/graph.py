"""Lightweight graph representation and utilities.

Graph supports arbitrary vertex ids (ints, strings, etc.). Adjacency is
stored as a dict: vertex -> list of outgoing `Edge` objects. All algorithms
now work with arbitrary vertex types, including matrix-based algorithms like
Floyd-Warshall which automatically handle vertex-to-index mapping.
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
        """String representation of edge.
        
        Returns:
            String in format "u->v:w" for directed or "u{}v:w" for undirected
        """
        br = "->" if self.directed else "{}"
        return f"{self.u}{br}{self.v}:{self.w}"


class Graph:
    """Graph supporting adjacency list and adjacency matrix views.

    Supports arbitrary vertex ids (ints, strings, etc.). Adjacency is stored as
    a dict: vertex -> list of outgoing `Edge` objects.
    """

    def __init__(self, num_vertices: int = 0, directed: bool = True):
        """Initialize a graph.
        
        Args:
            num_vertices: number of vertices (0 for empty graph, allows dynamic addition)
            directed: whether the graph is directed (default: True)
            
        Note:
            If num_vertices > 0, creates vertices 0 to num_vertices-1
            If num_vertices = 0, starts with empty graph (vertices added via add_edge)
        """
        self.n = num_vertices
        self.directed = directed
        # Adjacency now uses a dict mapping vertex ID to a Matrix of edges
        self.adj = {i: Matrix(0, 3) for i in range(num_vertices)} if num_vertices > 0 else {}

    def add_edge(self, u, v, w: int = 1):
        """Add an edge between vertices u and v.
        
        Args:
            u: source vertex id
            v: destination vertex id  
            w: edge weight (default: 1)
            
        Note:
            For undirected graphs, automatically adds reverse edge v->u
        """
        # Ensure vertices exist in adjacency
        if u not in self.adj:
            self.adj[u] = Matrix(0, 3) # Store as (v, w, directed_flag)
        if v not in self.adj:
            self.adj[v] = Matrix(0, 3)
        
        # Append a new row for the edge
        self.adj[u].add_row([v, w, 1 if self.directed else 0])
        if not self.directed:
            # store reverse edge as well for undirected adjacency convenience
            self.adj[v].add_row([u, w, 0])

    def neighbors(self, u):
        """Get all outgoing edges from vertex u.
        
        Args:
            u: vertex id
            
        Returns:
            list of Edge objects outgoing from vertex u
            Each Edge has attributes: u (source), v (destination), w (weight)
        """
        edge_matrix = self.adj.get(u)
        if not edge_matrix or edge_matrix.is_empty():
            return []
        
        edges = []
        for i in range(edge_matrix.rows):
            v, w, directed_val = edge_matrix.get(i, 0), edge_matrix.get(i, 1), edge_matrix.get(i, 2)
            edges.append(Edge(u, v, w, bool(directed_val)))
        return edges

    @classmethod
    def from_adjacency_matrix(cls, matrix: Matrix, directed: bool = True, inf_value: int = 10**12):
        """Create a graph from an n×n adjacency matrix.
        
        Args:
            matrix: n×n Matrix with edge weights (inf_value for no edge)
            directed: whether the graph is directed
            inf_value: value representing no edge
            
        Returns:
            Graph instance with vertices 0 to n-1
        """
        n = matrix.rows
        graph = cls(n, directed)
        
        for i in range(n):
            for j in range(n):
                weight = matrix.get(i, j)
                if weight != inf_value and weight != 0:  # Skip diagonal and non-edges
                    graph.add_edge(i, j, weight)
        
        return graph

    def to_adjacency_matrix(self, inf_value: int = 10**12) -> Matrix:
        """Convert to adjacency matrix. Works with arbitrary vertex types.
        
        For non-integer vertices, creates a mapping and returns a matrix
        with vertices mapped to indices 0 to n-1.
        """
        vertices = list(self.adj.keys())
        n = len(vertices)
        
        if n == 0:
            return Matrix(0, 0, inf_value)
        
        # Create vertex to index mapping
        vertex_to_index = {v: i for i, v in enumerate(vertices)}
        
        m = Matrix(n, n, inf_value)
        
        # Set diagonal to 0
        for i in range(n):
            m.set(i, i, 0)
        
        # Add edges
        for u, edge_matrix in self.adj.items():
            u_idx = vertex_to_index[u]
            for i in range(edge_matrix.rows):
                v, w, _ = edge_matrix.get(i, 0), edge_matrix.get(i, 1), edge_matrix.get(i, 2)
                if v in vertex_to_index:
                    v_idx = vertex_to_index[v]
                    m.set(u_idx, v_idx, w)
        
        return m


