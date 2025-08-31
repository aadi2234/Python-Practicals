class MyExp(Exception):
    pass

def divide(num, den):
    try:
        if den == 0:
            raise MyExp("Denominator cannot be zero")
        else:
            print("Division=", num / den)
    except MyExp as e:
        print("Error:", e)
    else:
        print("Division Performed Successfully")

num = int(input("Enter Numerator: "))
den = int(input("Enter Denominator: "))

divide(num, den)
