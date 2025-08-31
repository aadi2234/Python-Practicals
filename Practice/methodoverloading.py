class Student:
    def disp(self,roll=None,name=None):
        if roll is not None and name is not None:
            print(roll,name)
        else:
            print("Welcome")
s1=Student()
s1.disp(15,"Adi")
s1.disp()
