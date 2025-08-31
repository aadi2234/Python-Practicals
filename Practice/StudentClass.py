class Student:
    
    def read_stud(self):
        print("Enter Student Details")
        self.name=input("Enter Student Name:")    
        self.roll=int(input("Enter Student Roll No:"))
        self.marks=[]
        for i in range(1,6):
            mark=int(input(f"Enter Student Mark of {i} Subject:"))
            self.marks.append(mark)
        
    def per(self):
        self.perc=sum(self.marks)/5
        return self.perc 
    
    def disp(self):
        print("\nStudent Details")
        print("Student Name:",self.name)
        print("Student Roll No:",self.roll)
        print("Student Marks of 5 Subject:",self.marks)
        print("Student Percentage=",self.per())
        
s1=Student()
s1.read_stud()
s1.disp()