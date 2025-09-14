from data_structures.matrix import Matrix

def partition(matrix, low: int, high: int, pivot: int | None = None) -> int:
    """Lomuto-style partition on a 1xN Matrix vector.

    Args:
        matrix: Matrix(1, N)
        low: start index
        high: end index (pivot will be moved here)
        pivot: pivot index within [low, high]; defaults to high if None
    Returns:
        final index of the pivot after partitioning
    """
    if pivot is None:
        pivot = high
    # If pivot is not a valid index in [low, high], interpret it as a pivot VALUE
    if not (isinstance(pivot, int) and low <= pivot <= high):
        pivot_value = pivot
        pivot = None
        for idx in range(low, high + 1):
            if matrix.get(0, idx) == pivot_value:
                pivot = idx
                break
        if pivot is None:
            raise ValueError("pivot value not found in the specified range")
    pivot_value = matrix.get(0, pivot)
    matrix.set(0, pivot, matrix.get(0, high))
    matrix.set(0, high, pivot_value)
    j = low
    for i in range(low, high):
        if matrix.get(0, i) < pivot_value:
            temp = matrix.get(0, i)
            matrix.set(0, i, matrix.get(0, j))
            matrix.set(0, j, temp)
            j += 1
    matrix.set(0, high, matrix.get(0, j))
    matrix.set(0, j, pivot_value)
    return j

def quickselect(matrix, low: int, high: int, k: int) -> int:
    """Quickselect to find k-th smallest in Matrix vector.

    Args:
        matrix: Matrix(1, N)
        low: start index
        high: end index
        k: index to select (0-based)
    Returns:
        value of k-th smallest element
    """
    if low == high:
        return matrix.get(0, low)
    pivot_index = partition(matrix, low, high) # can set pivot as rand.randint(low, high)
    if k == pivot_index:
        return matrix.get(0, k)
    elif k < pivot_index:
        return quickselect(matrix, low, pivot_index - 1, k)
    else:
        return quickselect(matrix, pivot_index + 1, high, k)
    
def kth_smallest(matrix, k: int) -> int:
    """Return k-th smallest element (1-based) from Matrix vector."""
    if k < 1 or k > matrix.len():
        raise ValueError("k is out of bounds")
    return quickselect(matrix, 0, matrix.len() - 1, k - 1)

def sel(matrix, l:int, r:int, k: int) -> int:
    """Median of medians selection (deterministic select)."""
    n = r - l + 1
    if n <= 5:
        # Create a sub-matrix and sort it to find the k-th element
        sub_matrix = Matrix(1, n)
        for i in range(n):
            sub_matrix.set(0, i, matrix.get(0, l + i))
        sub_matrix.quick_sort()
        return sub_matrix.get(0, k - 1)

    num_medians = (n + 4) // 5
    medians = Matrix(1, num_medians)
    for i in range(num_medians):
        sub_l = l + 5 * i
        sub_r = min(sub_l + 4, r)
        # The median is the middle element of a small sorted group
        median_k = ((sub_r - sub_l + 1) + 1) // 2
        medians.set(0, i, sel(matrix, sub_l, sub_r, median_k))

    # Find the median of medians
    pivot_val = sel(medians, 0, medians.len() - 1, (medians.len() + 1) // 2)
    
    j = partition(matrix, l, r, pivot_val)
    
    # Number of elements in the low partition + pivot
    i = j - l + 1
    
    if k == i:
        return matrix.get(0, j)
    elif k < i:
        return sel(matrix, l, j - 1, k)
    else:
        return sel(matrix, j + 1, r, k - i)
