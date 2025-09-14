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

    # Strassen's Multiplication - Normal Case
    print("\n--- Normal Case: Strassen's Multiplication ---")
    A_sq = Matrix(4, 4)
    B_sq = Matrix(4, 4)
    for i in range(4):
        for j in range(4):
            A_sq.set(i, j, i + j + 1)
            B_sq.set(i, j, i - j + 1)
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

    # Edge case: Strassen with 2x2 matrices (smallest power of 2)
    print("\n--- Edge Case: Strassen 2x2 ---")
    A_2x2 = Matrix(2, 2)
    B_2x2 = Matrix(2, 2)
    A_2x2.data = [[1, 2], [3, 4]]
    B_2x2.data = [[5, 6], [7, 8]]
    print("Matrix A:\n", A_2x2)
    print("Matrix B:\n", B_2x2)
    C_2x2 = A_2x2.strassen_multiply(B_2x2)
    print("Result (Strassen 2x2):\n", C_2x2)

if __name__ == "__main__":
    matrix_multiplication_examples()
