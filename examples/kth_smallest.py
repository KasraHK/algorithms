from data_structures.matrix import Matrix
from algorithms.two_pointers.partition import kth_smallest
from algorithms.two_pointers.partition import sel
if __name__ == "__main__":
    arr = [3, 2, 1, 5, 4]
    matrix = Matrix(1, len(arr))
    for i in range(len(arr)):
        matrix.set(0, i, arr[i])
    print(matrix)
    result = kth_smallest(matrix, 3)
    kth = 3
    print(f"The {kth}-th smallest element is: {result}")  # Expected: 3
    result2 = sel(matrix, 0, matrix.len() - 1, 3)
    print(f"The {kth}-th smallest element using median of medians is: {result2}")  # Expected: 3