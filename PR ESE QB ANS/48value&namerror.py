#48.	Write a Python program to check for value error & name error exception. Input the data from the user.
try:
    no=int(input("Enter a no:"))
    print(no1)
except NameError as n:
    print(n)
except ValueError as v:
    print(v)
finally:
    print("Operation Performed Successfully...")