def factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    print("Factorial of ",no,"=",fact)
no=int(input("Enter a Number:"))
factorial(no)