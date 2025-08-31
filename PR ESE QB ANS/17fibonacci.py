#17.	Write a Python program to print Fibonacci series.
def fibonacci(no):
    a=0
    b=1
    for i in range(1,no+1):
        print(a,end=" ")
        next=a+b
        a=b
        b=next
no=int(input("Enter a Number:"))
fibonacci(no)