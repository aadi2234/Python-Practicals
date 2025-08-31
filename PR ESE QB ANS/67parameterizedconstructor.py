#67.	Design a class to show the use of parameterized constructor.
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def show(self):
        print("Car Brand:",self.brand)
        print("Car Brand:",self.color)
c=Car("Toyota","Black")
c.show()