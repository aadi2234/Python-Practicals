# 69.	Write a Python program to create a class to print the area of a square and a rectangle.
# The class has two methods with the same name but different number of parameters.
# The method for printing area of rectangle has two parameters which are length and breadth respectively
# while the other method for printing area of square has one parameter which is the side of square.
class AreaCalculator:
    def calculate_area(self, side, breadth=None):
        if breadth is None:
            area = side ** 2 
            print("Area of square:", area)
        else:
            area = side * breadth 
            print("Area of rectangle:", area)

calc = AreaCalculator()

calc.calculate_area(5)  
calc.calculate_area(4, 6)  
