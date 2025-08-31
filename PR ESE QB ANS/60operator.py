#60.	Use operator module & perform all arithmetic operations on given input.
import operator as o
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Addition of number:")
print(o.add(a,b))
print("Subtraction of number:")
print(o.sub(a,b))
print("Multiplication of number:")
print(o.mul(a,b))
print("Division of number:")
print(o.floordiv(a,b))
