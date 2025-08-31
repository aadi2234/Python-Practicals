#47.	Write a Python program to create a User Defined Exception to input the age from a person & check whether
#he/she is an adult, if not raise exception.
class PersonExp(Exception):
    pass
def checkAge(age):
    try:
        if age<18:
            print("Person is an Adult")
        else:
            raise PersonExp("Person is not an Adult")
    except ValueError as v:
        print("Plz Enter Valid Age:",v)
    except PersonExp as p:
        print("Error Occurred:",p)
        
age=int(input("Enter Age:"))
checkAge(age)
