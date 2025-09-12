from data_structures.graph import Graph
from algorithms.greedy.mst import prim_mst, kruskal_mst


def main():
    g = Graph(5, directed=False)
    edges = [
        (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)
    ]
    for u, v, w in edges:
        g.add_edge(u, v, w)
    parent, key, order, edges, total = prim_mst(g, start=0)
    print("Prim parent:", parent, "edges:", edges, "\ntotal:", total)  # Expected total: 16
    print("Prim edges:", edges)
    mst, total = kruskal_mst(g)
    print("Kruskal total:", total, "edges:", mst)  # Expected total: 16


if __name__ == "__main__":
    main()


