#45.	Write a Python program to create user defined exception that will check whether the password is correct or not using direct method.
class Myexp(Exception):
    pass
def checkPass(pwd):
    try:
        passwd="aadi2234"
        if pwd==passwd:
            print("Valid Password")
        else:
            raise Myexp("Incorrect Password")
    except Myexp as e:
        print("Error Occurred:",e)
pwd=input("Enter Password:")
checkPass(pwd)
        
        
