#44.	Write a Python program to Check for ZeroDivisionError Exception.
no1=int(input("Enter Number-1:"))
no2=int(input("Enter Number-2:"))
try:
    print("Division=",no1/no2)
except ZeroDivisionError as ze:
    print("Error Occured:",ze)
else:
    print("Division Performed Successfully..")
