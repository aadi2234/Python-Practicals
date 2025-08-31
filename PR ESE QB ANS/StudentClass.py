class Student:
    def getData(self):
        print("Enter Student Details:")
        self.name=input("Enter Name:")
        self.roll_no=int(input("Enter Roll Number:"))
        self.department=input("Enter Department:")
        self.mobile_no=int(input("Enter Mobile Number:"))
    def putData(self):
        print("Student Details:")
        print("Name:",self.name)
        print("Roll Number:",self.roll_no)
        print("Department:",self.department)
        print("Mobile Number:",self.mobile_no)
s=Student()
s.getData()
s.putData()