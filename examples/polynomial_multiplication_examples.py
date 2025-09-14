from algorithms.divide_conquer.polynomial_multiplication import dc_polynomial_multiply
from data_structures.matrix import Matrix

def polynomial_multiplication_examples():
    print("--- Polynomial Multiplication Examples ---")

    # Normal case: P(x) = 3x + 2, Q(x) = 2x + 5
    # Result should be 6x^2 + 19x + 10
    print("\n--- Normal Case ---")
    A = Matrix(1, 2)
    A.data[0] = [2, 3]  # Represents 2 + 3x
    B = Matrix(1, 2)
    B.data[0] = [5, 2]  # Represents 5 + 2x
    print("Polynomial A:", A)
    print("Polynomial B:", B)
    result = dc_polynomial_multiply(A, B)
    print("Result (A * B):", result)  # Should be [10, 19, 6]

    # Test case: Degree 3 polynomials
    print("\n--- Degree 3 Polynomials ---")
    A = Matrix(1, 4)
    A.data[0] = [1, 2, 1, 1]  # Represents 1 + 2x + x^2 + x^3
    B = Matrix(1, 4)
    B.data[0] = [1, 1, 0, 1]  # Represents 1 + x + x^3
    print("Polynomial A:", A)
    print("Polynomial B:", B)
    result = dc_polynomial_multiply(A, B)
    print("Result (A * B):", result)

    # Edge case: One polynomial is zero
    print("\n--- Edge Case: Zero Polynomial ---")
    C = Matrix(1, 4)
    C.data[0] = [1, 2, 3, 4]
    D = Matrix(1, 4) # Zero polynomial
    print("Polynomial C:", C)
    print("Polynomial D:", D)
    result_zero = dc_polynomial_multiply(C, D)
    print("Result (C * D):", result_zero)

if __name__ == "__main__":
    polynomial_multiplication_examples()
