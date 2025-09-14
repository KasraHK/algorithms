from algorithms.two_pointers.partition import kth_smallest, sel
from data_structures.matrix import Matrix

def selection_examples():
    print("--- Selection (k-th smallest) Examples ---")

    # Normal case
    print("\n--- Normal Case ---")
    normal_matrix = Matrix(1, 15)
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    for i, val in enumerate(data):
        normal_matrix.set(0, i, val)
    print("Matrix:", normal_matrix)
    k = 8
    print(f"The {k}-th smallest element (quickselect): {kth_smallest(normal_matrix, k)}")
    # Note: sel is 1-based for k, and uses 0-based l, r for range
    print(f"The {k}-th smallest element (deterministic select): {sel(normal_matrix, 0, normal_matrix.cols - 1, k)}")

    # Edge case: k is 1 (smallest)
    print("\n--- Edge Case: k=1 ---")
    print(f"The 1st smallest element (quickselect): {kth_smallest(normal_matrix, 1)}")
    print(f"The 1st smallest element (deterministic select): {sel(normal_matrix, 0, normal_matrix.cols - 1, 1)}")

    # Edge case: k is n (largest)
    print("\n--- Edge Case: k=n ---")
    n = normal_matrix.cols
    print(f"The {n}-th smallest element (quickselect): {kth_smallest(normal_matrix, n)}")
    print(f"The {n}-th smallest element (deterministic select): {sel(normal_matrix, 0, n - 1, n)}")

    # Edge case: matrix with duplicates
    print("\n--- Edge Case: Matrix with Duplicates ---")
    dup_matrix = Matrix(1, 10)
    dup_data = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    for i, val in enumerate(dup_data):
        dup_matrix.set(0, i, val)
    print("Matrix:", dup_matrix)
    k = 5
    print(f"The {k}-th smallest element (quickselect): {kth_smallest(dup_matrix, k)}")
    print(f"The {k}-th smallest element (deterministic select): {sel(dup_matrix, 0, dup_matrix.cols - 1, k)}")

if __name__ == "__main__":
    selection_examples()
