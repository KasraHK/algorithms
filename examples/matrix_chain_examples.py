from algorithms.dynamic_programming.matrix_chain import matrix_chain_multiplication
from data_structures.matrix import Matrix

def matrix_chain_examples():
    print("--- Matrix Chain Multiplication Examples ---")

    # Normal case
    print("\n--- Normal Case ---")
    dims = Matrix(1, 6)
    dims.data[0] = [30, 35, 15, 5, 10, 20]
    print("Dimensions:", dims)
    cost_matrix, split_matrix = matrix_chain_multiplication(dims)
    print("Cost Matrix:\n", cost_matrix)
    print("Split Matrix:\n", split_matrix)
    print(f"Minimum cost: {cost_matrix.get(0, dims.cols - 2)}")

    # Edge case: Only two matrices
    print("\n--- Edge Case: Two Matrices ---")
    dims_two = Matrix(1, 3)
    dims_two.data[0] = [10, 20, 30]
    print("Dimensions:", dims_two)
    cost_matrix_two, split_matrix_two = matrix_chain_multiplication(dims_two)
    print("Cost Matrix:\n", cost_matrix_two)
    print("Split Matrix:\n", split_matrix_two)
    print(f"Minimum cost: {cost_matrix_two.get(0, 0)}")

if __name__ == "__main__":
    matrix_chain_examples()
