from data_structures.matrix import Matrix
from algorithms.recursion.binary_search import binary_search, recursive_binary_search

if __name__ == "__main__":
    mat = Matrix(1, 10)
    for i in range(10):
        mat[0][i] = i * 10  # Fill the matrix with sorted values: 0, 10, 20, ..., 90
    target = 55
    print(binary_search(mat, target))  # Output: True
    print(recursive_binary_search(mat, 0, 9, target))  # Output: True