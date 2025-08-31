#41.	Create a class Employee with data members: name, department and salary.
#Create suitable methods for reading and printing employee information.
class Employee:
    def getemp(self):
        self.name=input("Enter Name of Employee:")
        self.department=input("Enter Department of Employee:")
        self.salary=float(input("Enter Salary of Employee:"))
    def putemp(self):
        print("Enter Name of Employee:",self.name)
        print("Enter Department of Employee:",self.department)
        print("Enter Salary of Employee:",self.salary)
emp=Employee()
print("Enter Employee Details\n")
emp.getemp()
print("\nEmployee Details\n")
emp.putemp()