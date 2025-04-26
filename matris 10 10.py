import numpy as np


national_code = "0521278481"
unique_digits = sorted(set(national_code))  
unique_digits = np.array([int(d) for d in unique_digits]) 


matrix1 = np.random.choice(unique_digits, (10, 10))
matrix2 = np.random.choice(unique_digits, (10, 10))


sum_matrix = matrix1 + matrix2


product_matrix = np.dot(matrix1, matrix2)


print("Matrix 1:\n", matrix1)
print("\nMatrix 2:\n", matrix2)
print("\nSum of Matrices:\n", sum_matrix)
print("\nProduct of Matrices:\n", product_matrix)
