from data_structures.matrix import Matrix

def binary_search(matrix: Matrix, target: int) -> bool:  # this matrix is a sorted vector
    """Iterative binary search on a sorted 1xN Matrix vector.

    Args:
        matrix: Matrix(1, N) sorted in non-decreasing order
        target: value to search
    Returns:
        True if target exists, otherwise False
    """
    if matrix.is_empty() or not matrix[0]:
        return False
    cols = len(matrix[0])
    left, right = 0, cols - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[0][mid]
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
    


def recursive_binary_search(matrix: Matrix, left: int, right: int, target: int) -> bool:
    """Recursive binary search on a sorted 1xN Matrix vector.

    Args:
        matrix: Matrix(1, N) sorted in non-decreasing order
        left: left index (inclusive)
        right: right index (inclusive)
        target: value to search
    Returns:
        True if target exists, otherwise False
    """
    if left > right:
        return False
    mid = (left + right) // 2
    mid_value = matrix[0][mid]
    if mid_value == target:
        return True
    elif mid_value < target:
        return recursive_binary_search(matrix, mid + 1, right, target)
    return recursive_binary_search(matrix, left, mid - 1, target)
    
    
# these algorithms return true or false based on whether the target is found in the matrix
# if you want the index of the target, modify the return statements to return mid instead of True