from algorithms.quick_sort import quick_sort_matrix
from data_structures.matrix import Matrix
import random

def quick_sort_examples():
    print("--- Quick Sort Examples ---")

    # Normal case
    print("\n--- Normal Case ---")
    normal_matrix = Matrix(1, 20)
    data = [random.randint(1, 100) for _ in range(20)]
    for i, val in enumerate(data):
        normal_matrix.set(0, i, val)
    print("Original Matrix:", normal_matrix)
    quick_sort_matrix(normal_matrix)
    print("Sorted Matrix:  ", normal_matrix)

    # Edge case: Already sorted matrix
    print("\n--- Edge Case: Already Sorted ---")
    sorted_matrix = Matrix(1, 15)
    for i in range(15):
        sorted_matrix.set(0, i, i * 2)
    print("Original Matrix:", sorted_matrix)
    quick_sort_matrix(sorted_matrix)
    print("Sorted Matrix:  ", sorted_matrix)

    # Edge case: Reverse sorted matrix
    print("\n--- Edge Case: Reverse Sorted ---")
    reverse_matrix = Matrix(1, 15)
    for i in range(15):
        reverse_matrix.set(0, i, (14 - i) * 2)
    print("Original Matrix:", reverse_matrix)
    quick_sort_matrix(reverse_matrix)
    print("Sorted Matrix:  ", reverse_matrix)

    # Edge case: Matrix with all equal elements
    print("\n--- Edge Case: All Elements Equal ---")
    equal_matrix = Matrix(1, 10)
    for i in range(10):
        equal_matrix.set(0, i, 5)
    print("Original Matrix:", equal_matrix)
    quick_sort_matrix(equal_matrix)
    print("Sorted Matrix:  ", equal_matrix)

if __name__ == "__main__":
    quick_sort_examples()
