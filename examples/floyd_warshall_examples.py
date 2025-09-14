from algorithms.dynamic_programming.floyd_warshall import floyd_warshall
from data_structures.graph import Graph

def floyd_warshall_examples():
    print("--- Floyd-Warshall Examples ---")

    # Normal case
    print("\n--- Normal Case ---")
    g = Graph(4, directed=True)
    g.add_edge(0, 1, 5)  # Direct path from 0 to 1
    g.add_edge(0, 2, 8)  # Direct path from 0 to 2
    g.add_edge(1, 2, 3)  # Path from 1 to 2
    g.add_edge(2, 3, 1)  # Path from 2 to 3
    
    dist_matrix, pred_matrix, mapping, has_neg_cycle = floyd_warshall(g)
    print("Distance Matrix:\n", dist_matrix)
    print("Predecessor Matrix:\n", pred_matrix)
    print("Contains negative cycle:", has_neg_cycle)

    # Edge case: Graph with a negative cycle
    print("\n--- Edge Case: Negative Cycle ---")
    g_neg_cycle = Graph(3, directed=True)
    g_neg_cycle.add_edge(0, 1, 1)
    g_neg_cycle.add_edge(1, 2, -1)
    g_neg_cycle.add_edge(2, 1, -1)  # Creates negative cycle: 1 -> 2 -> 1 total cost -2

    dist_matrix_neg, _, _, has_neg_cycle = floyd_warshall(g_neg_cycle)
    print("Distance Matrix (with negative cycle):\n", dist_matrix_neg)
    print("Contains negative cycle:", has_neg_cycle)
    print("Note: When a negative cycle exists, shortest paths through the cycle")
    print("      are undefined as you can achieve arbitrarily small costs")
    
if __name__ == "__main__":
    floyd_warshall_examples()
