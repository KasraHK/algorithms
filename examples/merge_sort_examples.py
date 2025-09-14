from algorithms.divide_conquer.merge_sort import merge_sort_vector
from data_structures.matrix import Matrix
import random

def merge_sort_examples():
    print("--- Merge Sort Examples ---")

    # Normal case
    print("\n--- Normal Case ---")
    normal_matrix = Matrix(1, 20)
    data = [random.randint(1, 100) for _ in range(20)]
    for i, val in enumerate(data):
        normal_matrix.set(0, i, val)
    print("Original Matrix:", normal_matrix)
    sorted_normal = merge_sort_vector(normal_matrix)
    print("Sorted Matrix:  ", sorted_normal)

    # Edge case: Empty matrix
    print("\n--- Edge Case: Empty Matrix ---")
    empty_matrix = Matrix(1, 0)
    print("Original Matrix:", empty_matrix)
    sorted_empty = merge_sort_vector(empty_matrix)
    print("Sorted Matrix:  ", sorted_empty)

    # Edge case: Single element matrix
    print("\n--- Edge Case: Single Element ---")
    single_matrix = Matrix(1, 1)
    single_matrix.set(0, 0, 42)
    print("Original Matrix:", single_matrix)
    sorted_single = merge_sort_vector(single_matrix)
    print("Sorted Matrix:  ", sorted_single)

if __name__ == "__main__":
    merge_sort_examples()
