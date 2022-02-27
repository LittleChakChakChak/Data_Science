import numpy as np

matrix = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
print(matrix)
print(matrix[3])
print(matrix[[2, 2, 2, 6, 6, 4, 6]])
print(matrix[matrix > 55])
print('-' * 40)

matrix1 = np.arange(16)
print(matrix1)
print('-' * 40)

# двухмерная матрица
matrix2 = matrix1.reshape(4, 4)
print(matrix2)
print(matrix2[2][3])
print('-' * 40)

# трехмерный массив
matrix3 = np.arange(48).reshape(4, 3, 4)
print(matrix3)
print(matrix3[2, 1, 3])

#  тип матрицы
print(matrix.dtype)
print((matrix / 3.12).dtype)