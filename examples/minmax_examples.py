from algorithms.divide_conquer.minmax import formal_min_max, min_max
from data_structures.matrix import Matrix

def minmax_examples():
    print("--- Min-Max Examples ---")

    # Normal case
    print("\n--- Normal Case ---")
    normal_matrix = Matrix(1, 11)
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    for i, val in enumerate(data):
        normal_matrix.set(0, i, val)
    print("Matrix:", normal_matrix)
    print(f"Min and Max (formal): {formal_min_max(normal_matrix)}")
    print(f"Min and Max (divide and conquer): {min_max(0, normal_matrix.cols - 1, normal_matrix)}")

    # Edge case: single element
    print("\n--- Edge Case: Single Element ---")
    single_matrix = Matrix(1, 1)
    single_matrix.set(0, 0, 42)
    print("Matrix:", single_matrix)
    print(f"Min and Max (formal): {formal_min_max(single_matrix)}")
    print(f"Min and Max (divide and conquer): {min_max(0, single_matrix.cols - 1, single_matrix)}")

    # Edge case: all elements are the same
    print("\n--- Edge Case: All Elements Equal ---")
    equal_matrix = Matrix(1, 8)
    for i in range(8):
        equal_matrix.set(0, i, 7)
    print("Matrix:", equal_matrix)
    print(f"Min and Max (formal): {formal_min_max(equal_matrix)}")
    print(f"Min and Max (divide and conquer): {min_max(0, equal_matrix.cols - 1, equal_matrix)}")

if __name__ == "__main__":
    minmax_examples()
