from data_structures.matrix import Matrix

def dc_polynomial_multiply(A: Matrix, B: Matrix) -> Matrix:
    if A.len() != B.len():
        raise ValueError("Polynomials must have the same degree")
    
    n = A.len()
    if n == 1:
        return Matrix(1, 1, A.get(0, 0) * B.get(0, 0))
    
    mid = n // 2
    
    A_low = Matrix(mid, 1)
    A_high = Matrix(n - mid, 1)
    B_low = Matrix(mid, 1)
    B_high = Matrix(n - mid, 1)
    
    for i in range(mid):
        A_low.set(i, 0, A.get(i, 0))
        B_low.set(i, 0, B.get(i, 0))
    for i in range(mid, n):
        A_high.set(i - mid, 0, A.get(i, 0))
        B_high.set(i - mid, 0, B.get(i, 0))
    
    Z0 = dc_polynomial_multiply(A_low, B_low)
    Z2 = dc_polynomial_multiply(A_high, B_high)
    A_sum = A_low.add(A_high)
    B_sum = B_low.add(B_high)
    Z1 = dc_polynomial_multiply(A_sum, B_sum).subtract(Z0).subtract(Z2)
    result_size = 2 * n - 1
    result = Matrix(result_size, 1)
    for i in range(Z0.len()):
        result.set(i, 0, result.get(i, 0) + Z0.get(i, 0))
    for i in range(Z1.len()):
        result.set(i + mid, 0, result.get(i + mid, 0) + Z1.get(i, 0))
    for i in range(Z2.len()):
        result.set(i + 2 * mid, 0, result.get(i + 2 * mid, 0) + Z2.get(i, 0))
    
    return result
    