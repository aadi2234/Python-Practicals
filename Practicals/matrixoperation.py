import numpy as np

matrix1 = np.array([[1, 2, 3],
                    [2, 1, 2],
                    [3, 2, 1]])

matrix2 = np.array([[1, 5, 3],
                    [2, 6, 7],
                    [4, 8, 1]])

add_matrix = np.add(matrix1, matrix2)
print("Addition=\n", add_matrix)

sub_matrix = np.subtract(matrix1, matrix2)
print("Subtraction=\n", sub_matrix)

mul_matrix = np.multiply(matrix1, matrix2)
print("Multiplication=\n", mul_matrix)

div_matrix = np.divide(matrix1, matrix2)
print("Division=\n", div_matrix)
