from data_structures.matrix import Matrix
from algorithms.recursion.binary_search import binary_search, recursive_binary_search


def main():
    v = Matrix(1, 6)
    for i, val in enumerate([1, 3, 5, 7, 9, 11]):
        v.set(0, i, val)
    print(v)
    print("iterative:", binary_search(v, 7))
    print("recursive:", recursive_binary_search(v, 0, v.cols - 1, 8))


if __name__ == "__main__":
    main()

from data_structures.matrix import Matrix
from algorithms.recursion.binary_search import binary_search, recursive_binary_search

if __name__ == "__main__":
    mat = Matrix(1, 10)
    for i in range(10):
        mat[0][i] = i * 10  # Fill the matrix with sorted values: 0, 10, 20, ..., 90
    target = 55
    print(binary_search(mat, target))  # Output: False
    print(recursive_binary_search(mat, 0, 9, target))  # Output: False