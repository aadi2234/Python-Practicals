class Myexp(Exception):
    pass
def divide(num,den):
    try:
        if den==0:
            raise Myexp("Denominator can`t be Zero")
        else:
            print("Division=",num/den)
    except Myexp as e:
        print("Exception Occurred:",e)
    else:
        print("Division Performed Successfully..")
num=int(input("Enter Numerator="))
den=int(input("Enter Denominator="))
divide(num,den)