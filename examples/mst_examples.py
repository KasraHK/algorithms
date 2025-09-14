from algorithms.greedy.mst import prim_mst, kruskal_mst
from data_structures.graph import Graph

def mst_examples():
    print("--- Minimum Spanning Tree Examples ---")

    # Normal case
    print("\n--- Normal Case ---")
    g = Graph(9, directed=False)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

    print("--- Prim's Algorithm ---")
    _, _, _, prim_edges, prim_cost = prim_mst(g, start=0)
    print("MST Edges (Prim's):\n", prim_edges)
    print("Total Cost (Prim's):", prim_cost)

    print("\n--- Kruskal's Algorithm ---")
    kruskal_edges, kruskal_cost = kruskal_mst(g)
    print("MST Edges (Kruskal's):\n", kruskal_edges)
    print("Total Cost (Kruskal's):", kruskal_cost)

    # Edge case: Disconnected graph
    print("\n--- Edge Case: Disconnected Graph ---")
    g_disconnected = Graph(5, directed=False)
    g_disconnected.add_edge(0, 1, 1)
    g_disconnected.add_edge(1, 2, 2)
    g_disconnected.add_edge(3, 4, 3) # Separate component

    print("--- Prim's Algorithm (Disconnected) ---")
    # Prim's only finds MST for the component of the start node
    _, _, _, prim_edges_dc, prim_cost_dc = prim_mst(g_disconnected, start=0)
    print("MST Edges (Prim's):\n", prim_edges_dc)
    print("Total Cost (Prim's):", prim_cost_dc)

    print("\n--- Kruskal's Algorithm (Disconnected) ---")
    # Kruskal's finds a minimum spanning forest
    kruskal_edges_dc, kruskal_cost_dc = kruskal_mst(g_disconnected)
    print("MST Edges (Kruskal's):\n", kruskal_edges_dc)
    print("Total Cost (Kruskal's):", kruskal_cost_dc)

if __name__ == "__main__":
    mst_examples()
