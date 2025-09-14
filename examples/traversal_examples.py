from algorithms.other_graph_algorithms.traversal import bfs, dfs, dfs_plus
from data_structures.graph import Graph

def traversal_examples():
    print("--- Graph Traversal Examples ---")

    # --- BFS ---
    print("\n--- BFS ---")
    g = Graph(8, directed=False)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(3, 6)
    g.add_edge(3, 7)
    g.add_edge(5, 6)
    g.add_edge(6, 7)

    # Normal case
    print("BFS - Normal Case (source=1):")
    _, dist, _, order = bfs(g, 1)
    print("Order:", order)
    print("Distances:", dist)

    # Edge case: Disconnected component
    print("\nBFS - Edge Case (source=0 on disconnected graph):")
    g_dc = Graph(3)
    g_dc.add_edge(0,1)
    # node 2 is not connected
    _, dist_dc, _, order_dc = bfs(g_dc, 0)
    print("Order:", order_dc)
    print("Distances:", dist_dc)

    # --- DFS ---
    print("\n--- DFS ---")
    g_dfs = Graph(6, directed=True)
    g_dfs.add_edge(0, 1)
    g_dfs.add_edge(0, 3)
    g_dfs.add_edge(1, 4)
    g_dfs.add_edge(2, 4)
    g_dfs.add_edge(2, 5)
    g_dfs.add_edge(3, 1)
    g_dfs.add_edge(4, 3)
    g_dfs.add_edge(5, 5)

    # Normal case
    print("DFS - Normal Case:")
    _, d, f, p = dfs(g_dfs)
    print("Discovery times:", d)
    print("Finish times:", f)
    print("Parents:", p)

    # DFS Plus
    print("\nDFS Plus - Analysis:")
    analysis = dfs_plus(g_dfs)
    print("Edge classification:", {k: v.data for k, v in analysis['edges'].items()})
    print("SCCs:", [scc.data for scc in analysis['scc']])

    # Edge case: Undirected graph for bridges/articulation points
    print("\nDFS Plus - Edge Case (Bridges and Articulation Points):")
    g_undirected = Graph(7, directed=False)
    g_undirected.add_edge(0, 1)
    g_undirected.add_edge(1, 2)
    g_undirected.add_edge(2, 0)
    g_undirected.add_edge(1, 3)
    g_undirected.add_edge(1, 4)
    g_undirected.add_edge(1, 6)
    g_undirected.add_edge(3, 5)
    g_undirected.add_edge(4, 5)
    analysis_undirected = dfs_plus(g_undirected)
    print("Bridges:", analysis_undirected['bridges'])
    print("Articulation Points:", analysis_undirected['articulation'])


if __name__ == "__main__":
    traversal_examples()
