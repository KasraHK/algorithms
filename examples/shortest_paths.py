from data_structures.graph import Graph
from algorithms.other_graph_algorithms.shortest_paths import bellman_ford, dijkstra


def main():
    g = Graph(5, directed=True)
    edges = [(0, 1, 6), (0, 3, 7), (1, 2, 5), (1, 3, 8), (1, 4, -4), (2, 1, -2), (3, 2, -3), (3, 4, 9), (4, 0, 2), (4, 2, 7)]
    for u, v, w in edges:
        g.add_edge(u, v, w)
    ok, d, _ = bellman_ford(g, 0)
    print("Bellman-Ford ok:", ok, "dist:", d)

    g2 = Graph(5, directed=False)
    edges2 = [(0,1,10),(0,4,5),(1,2,1),(4,1,3),(4,2,9),(4,3,2),(3,2,4)]
    for u, v, w in edges2:
        g2.add_edge(u, v, w)
    order, d2, _ = dijkstra(g2, 0)
    print("Dijkstra order:", order, "dist:", d2)


if __name__ == "__main__":
    main()


