#42.	Python program to read and print students information using two classes using simple inheritance.
class College:
    def getclg(self):
        self.cname=input("Enter College Name:")
    def putclg(self):
        print("College Name:",self.cname)
class Student(College):
    def getstud(self):
        self.roll=int(input("Enter Roll No.:"))
        self.name=input("Enter Name:")
    def putstud(self):
        print("Roll No.:",self.roll)
        print("Name:",self.name)
s1=Student()
s1.getclg()
s1.getstud()
s1.putclg()
s1.putstud()