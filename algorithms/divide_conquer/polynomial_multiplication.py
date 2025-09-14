from data_structures.matrix import Matrix

def dc_polynomial_multiply(A: Matrix, B: Matrix) -> Matrix:
    """Multiplies two polynomials represented as 1xN coefficient vectors.

    This function implements a divide-and-conquer algorithm (Karatsuba's method)
    for polynomial multiplication. It is more efficient than the naive O(n^2)
    approach for large polynomials.

    Args:
        A: A 1xN Matrix representing the coefficients of the first polynomial.
        B: A 1xN Matrix representing the coefficients of the second polynomial.
           Both matrices must have the same length.

    Returns:
        A 1x(2N-1) Matrix representing the coefficients of the resulting polynomial.
    
    Raises:
        ValueError: If the input matrices are not 1xN or have different lengths.
    """
    if A.rows != 1 or B.rows != 1 or A.cols != B.cols:
        raise ValueError("Polynomials must be represented as 1xN vectors of the same length")
    
    n = A.len()
    if n == 0:
        return Matrix(1, 0)
    if n == 1:
        res = Matrix(1, 1)
        res.set(0, 0, A.get(0, 0) * B.get(0, 0))
        return res
    
    mid = (n + 1) // 2
    
    A_low = A.submatrix(0, 0, 1, mid)
    A_high = A.submatrix(0, mid, 1, n)
    B_low = B.submatrix(0, 0, 1, mid)
    B_high = B.submatrix(0, mid, 1, n)
    
    # Ensure both parts have the same length for recursive calls
    if A_high.cols < mid:
        temp = Matrix(1, mid)
        for i in range(A_high.cols):
            temp.set(0, i, A_high.get(0, i))
        A_high = temp
        
    if B_high.cols < mid:
        temp = Matrix(1, mid)
        for i in range(B_high.cols):
            temp.set(0, i, B_high.get(0, i))
        B_high = temp

    Z0 = dc_polynomial_multiply(A_low, B_low)
    Z2 = dc_polynomial_multiply(A_high, B_high)
    
    A_sum = A_low.add(A_high)
    B_sum = B_low.add(B_high)
    Z1 = dc_polynomial_multiply(A_sum, B_sum)
    Z1 = Z1.subtract(Z0).subtract(Z2)

    result_size = 2 * n - 1
    result = Matrix(1, result_size)

    for i in range(Z0.cols):
        result.set(0, i, result.get(0, i) + Z0.get(0, i))
    for i in range(Z1.cols):
        if (i + mid) < result.cols:
            result.set(0, i + mid, result.get(0, i + mid) + Z1.get(0, i))
    for i in range(Z2.cols):
        if (i + 2 * mid) < result.cols:
            result.set(0, i + 2 * mid, result.get(0, i + 2 * mid) + Z2.get(0, i))
    
    return result
    