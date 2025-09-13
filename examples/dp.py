from data_structures.graph import Graph
from data_structures.matrix import Matrix
from algorithms.dynamic_programming.floyd_warshall import floyd_warshall
from algorithms.dynamic_programming.matrix_chain import matrix_chain_multiplication


def main():
    g = Graph(4, directed=True)
    edges = [(0,1,5),(0,3,10),(1,2,3),(2,3,1)]
    for u, v, w in edges:
        g.add_edge(u, v, w)
    A, P, vertex_mapping = floyd_warshall(g)
    print("FW dist[0][3] =", A.get(0,3))  # Expected: 9

    dims = Matrix(1, 5)
    for i, d in enumerate([10, 30, 5, 60, 2]):
        dims.set(0, i, d)
    m, s = matrix_chain_multiplication(dims)
    print("MCM cost =", m.get(0, 3))  # Expected: 700


if __name__ == "__main__":
    main()


