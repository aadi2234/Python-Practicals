#57.	Write a Python program that will calculate area and circumference of circle using inbuilt Math Module.
import math as m
radius=float(input("Enter radius of circle:"))
area=m.pi*radius**2
circum=2*m.pi*radius
print("Area of circle:",area)
print("Circumference of circle:",circum)
