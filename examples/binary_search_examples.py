from algorithms.recursion.binary_search import binary_search, recursive_binary_search
from data_structures.matrix import Matrix

def binary_search_examples():
    print("--- Binary Search Examples ---")
    
    # Normal case
    print("\n--- Normal Case ---")
    normal_matrix = Matrix(1, 10)
    for i in range(10):
        normal_matrix.set(0, i, i * 2)
    print("Matrix:", normal_matrix)
    target = 12
    print(f"Iterative search for {target}: {binary_search(normal_matrix, target)}")
    print(f"Recursive search for {target}: {recursive_binary_search(normal_matrix, 0, normal_matrix.cols - 1, target)}")
    target = 7
    print(f"Iterative search for {target}: {binary_search(normal_matrix, target)}")
    print(f"Recursive search for {target}: {recursive_binary_search(normal_matrix, 0, normal_matrix.cols - 1, target)}")

    # Edge case: empty matrix
    print("\n--- Edge Case: Empty Matrix ---")
    empty_matrix = Matrix(1, 0)
    print("Matrix:", empty_matrix)
    target = 5
    print(f"Iterative search for {target}: {binary_search(empty_matrix, target)}")
    print(f"Recursive search for {target}: {recursive_binary_search(empty_matrix, 0, empty_matrix.cols - 1, target)}")

    # Edge case: single element matrix
    print("\n--- Edge Case: Single Element Matrix ---")
    single_element_matrix = Matrix(1, 1)
    single_element_matrix.set(0, 0, 10)
    print("Matrix:", single_element_matrix)
    target = 10
    print(f"Iterative search for {target}: {binary_search(single_element_matrix, target)}")
    print(f"Recursive search for {target}: {recursive_binary_search(single_element_matrix, 0, single_element_matrix.cols - 1, target)}")
    target = 5
    print(f"Iterative search for {target}: {binary_search(single_element_matrix, target)}")
    print(f"Recursive search for {target}: {recursive_binary_search(single_element_matrix, 0, single_element_matrix.cols - 1, target)}")

if __name__ == "__main__":
    binary_search_examples()
