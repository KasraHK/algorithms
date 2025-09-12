from data_structures.matrix import Matrix
from algorithms.two_pointers.partition import partition as matrix_partition


def quick_sort_matrix(v: Matrix, low: int = 0, high: int | None = None) -> None:
    """In-place quicksort for a 1xN Matrix using shared partition.

    Args:
        v: Matrix with shape 1xN
        low: starting index
        high: ending index inclusive
    Returns: None (v is sorted in place)
    """
    if v.rows != 1:
        raise ValueError("Quick sort works only for 1xN matrices")
    if high is None:
        high = v.cols - 1
    if low < high:
        p = matrix_partition(v, low, high)
        quick_sort_matrix(v, low, p - 1)
        quick_sort_matrix(v, p + 1, high)