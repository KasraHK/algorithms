from data_structures.matrix import Matrix

def matrix_multiplication_examples():
    print("--- Matrix Multiplication Examples ---")

    # Normal case (Standard Multiplication)
    print("\n--- Normal Case: Standard Multiplication ---")
    A = Matrix(2, 3)
    A.data = [[1, 2, 3], [4, 5, 6]]
    B = Matrix(3, 2)
    B.data = [[7, 8], [9, 10], [11, 12]]
    print("Matrix A:\n", A)
    print("Matrix B:\n", B)
    C = A.multiply(B)
    print("Result (A * B):\n", C)

    # Strassen's Multiplication - Normal Case (requires square matrices of same size, power of 2 for simplicity)
    print("\n--- Normal Case: Strassen's Multiplication ---")
    A_sq = Matrix(4, 4)
    B_sq = Matrix(4, 4)
    for i in range(4):
        for j in range(4):
            A_sq.set(i, j, i + j)
            B_sq.set(i, j, i - j)
    print("Matrix A (square):\n", A_sq)
    print("Matrix B (square):\n", B_sq)
    C_strassen = A_sq.strassen_multiply(B_sq)
    C_standard = A_sq.multiply(B_sq)
    print("Result (Strassen):\n", C_strassen)
    print("Result (Standard for comparison):\n", C_standard)

    # Edge case: Multiplication by identity matrix
    print("\n--- Edge Case: Multiplication by Identity ---")
    A_rect = Matrix(2, 3)
    A_rect.data = [[1, 2, 3], [4, 5, 6]]
    I = Matrix(3, 3)
    I.identity()
    print("Matrix A:\n", A_rect)
    print("Identity Matrix I:\n", I)
    C_ident = A_rect.multiply(I)
    print("Result (A * I):\n", C_ident)

    # Edge case: Strassen with 1x1 matrices
    print("\n--- Edge Case: Strassen 1x1 ---")
    A_1x1 = Matrix(1, 1, 5)
    B_1x1 = Matrix(1, 1, 10)
    print("Matrix A:\n", A_1x1)
    print("Matrix B:\n", B_1x1)
    C_1x1 = A_1x1.strassen_multiply(B_1x1)
    print("Result (Strassen 1x1):\n", C_1x1)

if __name__ == "__main__":
    matrix_multiplication_examples()
