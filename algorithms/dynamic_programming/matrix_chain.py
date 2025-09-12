from data_structures.matrix import Matrix


def matrix_chain_multiplication(dims: Matrix):
    """Matrix Chain Multiplication optimal parenthesization cost.

    Args:
        dims: 1x(N+1) matrix of dimensions p0,p1,...,pN
    Returns:
        m: Matrix NxN of minimal costs
        s: Matrix NxN of split points
    """
    if dims.rows != 1 or dims.cols < 2:
        raise ValueError("dims must be 1x(N+1) with N>=1")
    n = dims.cols - 1
    m = Matrix(n, n, 0)
    s = Matrix(n, n, -1)
    for L in range(2, n + 1):
        for i in range(0, n - L + 1):
            j = i + L - 1
            m.set(i, j, 10**18)
            for k in range(i, j):
                cost = m.get(i, k) + m.get(k + 1, j) + dims.get(0, i) * dims.get(0, k + 1) * dims.get(0, j + 1)
                if cost < m.get(i, j):
                    m.set(i, j, cost)
                    s.set(i, j, k)
    return m, s


