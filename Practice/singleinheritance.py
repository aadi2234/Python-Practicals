class College:
    def getclg(self):
        self.cname=input("Enter College=")
    def putclg(self):
        print("College Name=",self.cname)
class Student(College):
    def getstud(self):
        self.name=input("Enter Student Name=")
        self.depart=input("Enter Student Department=")
    def putstud(self):
        print("Student Name=",self.name)
        print("Student Department=",self.depart)
s1=Student()
s1.getclg()
s1.getstud()
s1.putclg()
s1.putstud()