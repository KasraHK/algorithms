from data_structures.matrix import Matrix
from algorithms.quick_sort import quick_sort_matrix


def main():
    v = Matrix(1, 8)
    for i, val in enumerate([5, 2, 9, 1, 5, 6, 3, 7]):
        v.set(0, i, val)
    quick_sort_matrix(v)
    print([v.get(0, i) for i in range(v.cols)])


if __name__ == "__main__":
    main()


