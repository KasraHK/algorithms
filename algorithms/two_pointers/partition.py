from data_structures.matrix import Matrix

def partition(matrix, low: int, high: int, pivot: int= 0) -> int:
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
    if k < 1 or k > matrix.len():
        raise ValueError("k is out of bounds")
    return quickselect(matrix, 0, matrix.len() - 1, k - 1)

def sel(matrix, l:int, r:int, k: int) -> int:
    n = r - l + 1
    if n <= 5:
        sub = [matrix.get(0, i) for i in range(l, r + 1)]
        sub.sort()
        return sub[k - 1]
    m = (n + 4) // 5
    b = Matrix(1, m)
    for i in range(m):
        b[i] = sel(matrix, 5 * i - 4, 5 * i, 3)
    x = sel(b, 0, m - 1, (m + 1) // 2)
    j = partition(matrix, l, r, x)
    i = j - l + 1
    if k == i:
        return matrix.get(0, j)
    elif k < i:
        return sel(matrix, l, j - 1, k)
    return sel(matrix, j + 1, r, k - i)
