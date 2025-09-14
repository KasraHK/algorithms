from algorithms.dynamic_programming.floyd_warshall import floyd_warshall
from data_structures.graph import Graph

def floyd_warshall_examples():
    print("--- Floyd-Warshall Examples ---")

    # Normal case
    print("\n--- Normal Case ---")
    g = Graph(4, directed=True)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 3, 10)
    g.add_edge(1, 2, 3)
    g.add_edge(2, 3, 1)
    
    dist_matrix, pred_matrix, mapping = floyd_warshall(g)
    print("Distance Matrix:\n", dist_matrix)
    print("Predecessor Matrix:\n", pred_matrix)

    # Edge case: Graph with a negative cycle
    print("\n--- Edge Case: Negative Cycle ---")
    g_neg_cycle = Graph(3, directed=True)
    g_neg_cycle.add_edge(0, 1, 1)
    g_neg_cycle.add_edge(1, 2, -1)
    g_neg_cycle.add_edge(2, 1, -1) # Negative cycle 1 -> 2 -> 1

    dist_matrix_neg, _, _ = floyd_warshall(g_neg_cycle)
    print("Distance Matrix (with negative cycle):\n", dist_matrix_neg)
    # Note: The diagonal will show negative values if a node is part of a negative cycle
    
if __name__ == "__main__":
    floyd_warshall_examples()
