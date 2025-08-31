#58.	Write a Python program that will display Calendar of given month using Calendar Module.
import calendar as c
y=int(input("Enter year:"))
m=int(input("Enter Month:"))
print(c.month(y,m))