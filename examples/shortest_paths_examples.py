from algorithms.other_graph_algorithms.shortest_paths import bellman_ford, dijkstra
from data_structures.graph import Graph

def shortest_paths_examples():
    print("--- Shortest Paths Examples ---")

    # --- Dijkstra's Algorithm ---
    print("\n--- Dijkstra's Algorithm ---")
    # Normal case
    g_dijkstra = Graph(5, directed=True)
    g_dijkstra.add_edge(0, 1, 10)
    g_dijkstra.add_edge(0, 2, 5)
    g_dijkstra.add_edge(1, 2, 2)
    g_dijkstra.add_edge(1, 3, 1)
    g_dijkstra.add_edge(2, 1, 3)
    g_dijkstra.add_edge(2, 3, 9)
    g_dijkstra.add_edge(2, 4, 2)
    g_dijkstra.add_edge(3, 4, 4)
    g_dijkstra.add_edge(4, 3, 6)
    g_dijkstra.add_edge(4, 0, 7)
    
    order, dist, parent = dijkstra(g_dijkstra, 0)
    print("Dijkstra - Normal Case:")
    print("Order of visited nodes:", order)
    print("Distances:", dist)
    print("Parents:", parent)

    # Edge case: Unreachable node
    g_unreachable = Graph(3, directed=True)
    g_unreachable.add_edge(0, 1, 1)
    # Node 2 is unreachable from 0
    _, dist_unreachable, _ = dijkstra(g_unreachable, 0)
    print("\nDijkstra - Edge Case (Unreachable Node):")
    print("Distances:", dist_unreachable)

    # --- Bellman-Ford Algorithm ---
    print("\n--- Bellman-Ford Algorithm ---")
    # Normal case with negative weights
    g_bf = Graph(5, directed=True)
    g_bf.add_edge(0, 1, 6)
    g_bf.add_edge(0, 3, 7)
    g_bf.add_edge(1, 2, 5)
    g_bf.add_edge(1, 3, 8)
    g_bf.add_edge(1, 4, -4)
    g_bf.add_edge(2, 1, -2)
    g_bf.add_edge(3, 2, -3)
    g_bf.add_edge(3, 4, 9)
    g_bf.add_edge(4, 0, 2)
    g_bf.add_edge(4, 2, 7)

    ok, dist_bf, parent_bf = bellman_ford(g_bf, 0)
    print("Bellman-Ford - Normal Case (Negative Weights):")
    print("Success (no negative cycle):", ok)
    print("Distances:", dist_bf)
    print("Parents:", parent_bf)

    # Edge case: Negative weight cycle
    g_neg_cycle = Graph(4, directed=True)
    g_neg_cycle.add_edge(0, 1, 1)
    g_neg_cycle.add_edge(1, 2, 2)
    g_neg_cycle.add_edge(2, 3, -5)
    g_neg_cycle.add_edge(3, 1, 1) # Cycle 1->2->3->1 with weight -2

    ok_neg, dist_neg, _ = bellman_ford(g_neg_cycle, 0)
    print("\nBellman-Ford - Edge Case (Negative Cycle):")
    print("Success (no negative cycle):", ok_neg)
    print("Distances (may be further relaxed):", dist_neg)

if __name__ == "__main__":
    shortest_paths_examples()
