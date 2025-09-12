from data_structures.matrix import Matrix
import random as rand
matrix = Matrix(1, 8)
for i in range(8):
    matrix.set(0, i, rand.randint(0, 100))
    
print(matrix.merge_sort())