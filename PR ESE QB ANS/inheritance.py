class Parent:
    def pm(self):
        print("Parent Class Method")
class Child(Parent):
    def cm(self):
        print("Child Class Method")
c=Child()
c.pm()
c.cm()