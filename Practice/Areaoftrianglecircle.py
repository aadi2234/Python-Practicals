#Design a python program to calculate area of triangle and circle and print the result
import math 
def aot(base,height):
    area=0.5*base*height
    print("Area of Triangle=",area)
b=int(input("Enter Base:"))
h=int(input("Enter Height:"))
aot(b,h)
def aoc(radius):
    area=math.pi*radius*radius
    print("Area of Circle=",area)
r=int(input("Enter Radius:"))
aoc(r)
    