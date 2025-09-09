# example matrix multiplication using strassen's algorithm vs normal multiplication
# from parent_init import parent_init
# parent_init()
from data_structures.matrix import Matrix
if __name__ == "__main__":
    A = Matrix(4, 4)
    B = Matrix(4, 4)
    count = 1
    for i in range(4):
        for j in range(4):
            A.set(i, j, count)
            B.set(i, j, count)
            count += 1
            
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    C_strassen = A.strassen_multiply(B)
    C_normal = A.multiply(B)
    print("\nStrassen's Multiplication Result (C = A * B):")
    print(C_strassen)
    print("\nNormal Multiplication Result (C = A * B):")
    print(C_normal)