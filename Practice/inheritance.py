class College:
    def getclg(self):
        self.clg=input("Enter College Name:")
    def putclg(self):
        print("College Name:",self.clg)
class Student(College):
    def getstud(self):
        self.name=input("Enter Student Name:")
        self.roll=int(input("Enter Student Roll No.:"))
    def putstud(self):
        print("Student Name:",self.name)
        print("Student Roll No.:",self.roll)
s=Student()
print("Enter Student Details")
s.getclg()
s.getstud()
print("Student Details")
s.putclg()
s.putstud()