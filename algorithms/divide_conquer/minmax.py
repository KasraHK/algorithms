from data_structures.matrix import Matrix

def formal_min(matrix: Matrix, col: int) -> int:
    """Return the minimum of first `col` elements in a 1xN Matrix vector.

    Args:
        matrix: Matrix(1, N) vector
        col: number of elements to consider from start (1..N)
    Returns:
        minimum value among matrix[0][0..col-1]
    """
    if matrix.is_empty() or not (0 < col <= matrix.cols):
        raise ValueError("Matrix is empty or column index is out of bounds")
    min_value = matrix.get(0, 0)
    for i in range(1, col):
        if matrix.get(0, i) < min_value:
            min_value = matrix.get(0, i)
    return min_value
def formal_max(matrix: Matrix, col: int) -> int:
    """Return the maximum of first `col` elements in a 1xN Matrix vector."""
    if matrix.is_empty() or not (0 < col <= matrix.cols):
        raise ValueError("Matrix is empty or column index is out of bounds")
    max_value = matrix.get(0, 0)
    for i in range(1, col):
        if matrix.get(0, i) > max_value:
            max_value = matrix.get(0, i)
    return max_value

def formal_min_max(matrix: Matrix) -> tuple[int, int]:
    """Compute min and max of a 1xN Matrix vector by scanning once."""
    if matrix.is_empty():
        raise ValueError("Matrix is empty")
    col = matrix.cols
    if col == 0:
        raise ValueError("Matrix has no columns")
    min_value = matrix.get(0, 0)
    max_value = matrix.get(0, 0)
    if col == 1:
        return min_value, max_value
    
    # Optimized for pairs
    for i in range(0, col - 1, 2):
        a = matrix.get(0, i)
        b = matrix.get(0, i + 1)
        if a < b:
            if a < min_value: min_value = a
            if b > max_value: max_value = b
        else:
            if b < min_value: min_value = b
            if a > max_value: max_value = a
    
    # Handle odd number of elements
    if col % 2 != 0:
        last_val = matrix.get(0, col - 1)
        if last_val < min_value: min_value = last_val
        if last_val > max_value: max_value = last_val
        
    return min_value, max_value

def min_max(l: int, r: int, matrix: Matrix) -> tuple[int, int]:
    """Divide-and-conquer min/max on subarray [l..r] of Matrix vector.

    Args:
        l: left index inclusive
        r: right index inclusive
        matrix: Matrix(1, N) vector
    Returns:
        tuple(min_value, max_value)
    """
    if l > r:
        raise ValueError("l cannot be greater than r")
    if l == r:
        return matrix.get(0, l), matrix.get(0, l)
    if r == l + 1:
        a, b = matrix.get(0, l), matrix.get(0, r)
        return (a, b) if a < b else (b, a)
    mid = (l + r) // 2
    min1, max1 = min_max(l, mid, matrix)
    min2, max2 = min_max(mid + 1, r, matrix)
    allmin = min1 if min1 < min2 else min2
    allmax = max1 if max1 > max2 else max2
    return allmin, allmax