import math as m
no=int(input("Enter Number:"))
def factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    print("Factorial of",no,"=",fact)
factorial(no)