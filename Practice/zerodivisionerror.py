no1=int(input("Enter 1st Number:"))
no2=int(input("Enter 2nd Number:"))
try:
    print("Division=",no1/no2)
except ZeroDivisionError as e:
    print("Exception Occurred",e)
else:
    print("Division Performed Successfully")