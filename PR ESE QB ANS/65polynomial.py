# 65.	Write a Python program using numpy Poly1d to generate the polynomial equation and to
# use det(), inv() on matrices.
from numpy import poly1d
import numpy
p=poly1d([4,8,9])
print(p)
arr=numpy.array([[3,4,2],[5,7,12],[21,33,11]])
print("Array:\n",arr)
print("Determinant of matrix:",numpy.linalg.det(arr))
print("Inverse of matrix:\n",numpy.linalg.inv(arr))
