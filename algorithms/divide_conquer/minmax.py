from data_structures.matrix import Matrix

def formal_min(matrix: Matrix, col: int) -> int:
    if matrix.is_empty() or col < 0:
        raise ValueError("Matrix is empty or column index is out of bounds")
    min_value = matrix[0][col]
    for i in range(col):
        if matrix[0][i] < min_value:
            min_value = matrix[0][i]
    return min_value
def formal_max(matrix: Matrix, col: int) -> int:
    if matrix.is_empty() or col < 0:
        raise ValueError("Matrix is empty or column index is out of bounds")
    max_value = matrix[0][col]
    for i in range(col):
        if matrix[0][i] > max_value:
            max_value = matrix[0][i]
    return max_value

def formal_min_max(matrix: Matrix) -> tuple[int, int]:
    col = len(matrix[0])
    if matrix.is_empty() or col < 0:
        raise ValueError("Matrix is empty or column index is out of bounds")
    min_value = matrix[0][col]
    max_value = matrix[0][col]
    if col == 1:
        return min_value, max_value
    elif col == 2:
        if matrix[0][0] < matrix[0][1]:
            return matrix[0][0], matrix[0][1]
        else:
            return matrix[0][1], matrix[0][0]
    for i in range(1, col):
        if matrix[0][i] < min_value:
            min_value = matrix[0][i]
        if matrix[0][i] > max_value:
            max_value = matrix[0][i]
    return min_value, max_value

def min_max(l: int, r: int, matrix: Matrix) -> tuple[int, int]:
    if l == r:
        return matrix[0][l], matrix[0][l]
    if r == l + 1:
        if matrix[0][l] < matrix[0][r]:
            return matrix[0][l], matrix[0][r]
        else:
            return matrix[0][r], matrix[0][l]
    mid = (l + r) // 2
    min1, max1 = min_max(l, mid, matrix)
    min2, max2 = min_max(mid + 1, r, matrix)
    allmin = min1 if min1 < min2 else min2
    allmax = max1 if max1 > max2 else max2
    return allmin, allmax