class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def show(self):
        print("Car Brand-",self.brand)
        print("Car Color-",self.color)
c1=Car("Toyota","Black")
c1.show()