#40.	Write a Python program to create a class 'Degree' having a method 'getDegree'
#that prints "I got a degree". It has two subclasses namely 'Undergraduate' and 'Postgraduate'
#each having a method with the same name that prints "I am an Undergraduate" and "I am a
#Postgraduate" respectively. Call the method by creating an object of each of the three classes.
class Degree:
    def getDegree(self):
        print("I got a degree")
class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate")
class Postgraduate(Degree):
    def getDegree(self):
        print("I am an Postgraduate")
d=Degree()
d.getDegree()
ug=Undergraduate()
ug.getDegree()
pg=Postgraduate()
pg.getDegree()