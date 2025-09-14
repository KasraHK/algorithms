from data_structures.graph import Graph
from data_structures.matrix import Matrix


def floyd_warshall(graph: Graph, inf_value: int = 10**12):
    """Floyd-Warshall all-pairs shortest paths.

    Works with arbitrary vertex types by using the adjacency matrix mapping.
    Detects negative cycles by checking if any vertex can reach itself with
    negative cost.

    Args:
        graph: Graph instance
        inf_value: value used to represent infinity
    Returns:
        A: Matrix of shortest path distances
        P: Matrix of intermediate vertices (-1 if none)
        vertex_mapping: dict mapping matrix indices to original vertex ids
        has_negative_cycle: boolean indicating if graph contains a negative cycle
    """
    A = graph.to_adjacency_matrix(inf_value).copy()
    n = A.rows
    
    # Create mapping from matrix indices back to original vertices
    vertices = list(graph.adj.keys())
    vertex_mapping = {i: v for i, v in enumerate(vertices)}
    
    P = Matrix(n, n, -1)
    
    # Main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Only update if both paths exist (not infinity)
                if A.get(i, k) < inf_value and A.get(k, j) < inf_value:
                    new_dist = A.get(i, k) + A.get(k, j)
                    if new_dist < A.get(i, j):
                        A.set(i, j, new_dist)
                        P.set(i, j, k)
    
    # Check for negative cycles
    has_negative_cycle = False
    for i in range(n):
        if A.get(i, i) < 0:
            has_negative_cycle = True
            break
            
    return A, P, vertex_mapping, has_negative_cycle


