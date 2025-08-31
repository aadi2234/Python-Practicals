#38.	Write a Python program with the user defined function which accepts a number & returns
#Fibonacci series of given numbers.
def fibonacci(no):
    a=0
    b=1
    for i in range(1,no+1):
        print(a,end=" ")
        next=(a+b)
        a=b
        b=next
no=int(input("Enter a number:"))
fibonacci(no)