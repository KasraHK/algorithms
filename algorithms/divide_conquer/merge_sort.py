from data_structures.matrix import Matrix

def merge(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    if matrix1.rows != matrix2.rows:
        raise ValueError("Matrices must have the same number of rows to merge")
    merged = Matrix(matrix1.rows, matrix1.cols + matrix2.cols)
    for i in range(matrix1.rows):
        for j in range(matrix1.cols):
            merged.set(i, j, matrix1.get(i, j))
        for j in range(matrix2.cols):
            merged.set(i, j + matrix1.cols, matrix2.get(i, j))
    return merged

def merge_sort_vector(v: Matrix) -> Matrix:
    """Return a sorted copy of a 1xN vector using merge sort.

    Args:
        v: Matrix with shape 1xN
    Returns:
        new Matrix(1xN) sorted non-decreasing
    """
    return v.merge_sort()


