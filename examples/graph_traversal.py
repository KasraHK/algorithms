from data_structures.graph import Graph
from algorithms.traversal import dfs, dfs_plus, bfs


def main():
    g = Graph(6, directed=False)
    edges = [(0,1,1),(0,2,1),(1,3,1),(2,3,1),(3,4,1),(4,5,1)]
    for u, v, w in edges:
        g.add_edge(u, v, w)
    color, d, f, parent = dfs(g)
    print("dfs parent:", parent)
    info = dfs_plus(g)
    print("bridges:", info['bridges'], "articulation:", info['articulation'])
    color2, dist, par2, order = bfs(g, 0)
    print("bfs dist:", dist)


if __name__ == "__main__":
    main()


